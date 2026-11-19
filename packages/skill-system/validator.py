"""Local validator for KAME AION HABITAT skill packages.

Validates SKILL.md YAML frontmatter and the content conventions defined in
docs/skills/SKILL_FORMAT.md. It does not grant or enforce runtime permissions.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - exercised by CLI environment
    yaml = None

SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
SKILL_ID_RE = re.compile(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
STATUSES = {"draft", "testing", "approved", "deprecated", "disabled", "rejected"}
REQUIRED_FIELDS = {
    "skill_id", "name", "version", "description", "category", "status",
    "author", "source", "compatibility", "permissions", "dependencies",
    "execution", "evaluation", "tags", "created_at", "updated_at",
}
REQUIRED_SECTIONS = [
    "Purpose", "When to Use", "When Not to Use", "Inputs",
    "Expected Outputs", "Procedure", "Tool Requirements",
    "Permissions & Safety", "Failure Handling", "Verification",
    "Examples", "References",
]
# High-confidence credential patterns only; this is a heuristic, not DLP.
SECRET_PATTERNS = [
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]
FRONTMATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.S)


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    message: str
    path: str

    def __str__(self) -> str:
        return f"{self.severity} {self.code} {self.path}: {self.message}"


def _issue(items: list[Issue], severity: str, code: str, message: str, path: Path) -> None:
    items.append(Issue(severity, code, message, str(path)))


def _is_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _check_string_map(data: dict, key: str, required: set[str], path: Path,
                      issues: list[Issue]) -> dict:
    value = data.get(key)
    if not isinstance(value, dict):
        _issue(issues, "ERROR", "META_OBJECT", f"'{key}' harus berupa object/map.", path)
        return {}
    for field in required:
        if field not in value:
            _issue(issues, "ERROR", "META_NESTED_REQUIRED",
                   f"Field '{key}.{field}' wajib diisi.", path)
    return value


def _check_string_list(value: Any, field: str, path: Path,
                       issues: list[Issue]) -> None:
    if not isinstance(value, list) or any(not _is_string(item) for item in value):
        _issue(issues, "ERROR", "META_LIST",
               f"'{field}' harus berupa daftar string.", path)


def parse_frontmatter(text: str, path: Path, issues: list[Issue]) -> dict | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        _issue(issues, "ERROR", "FRONTMATTER_MISSING",
               "SKILL.md harus diawali YAML frontmatter yang dibatasi ---.", path)
        return None
    if yaml is None:
        _issue(issues, "ERROR", "DEPENDENCY_MISSING",
               "PyYAML belum terpasang. Jalankan: python -m pip install -r requirements.txt", path)
        return None
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        _issue(issues, "ERROR", "YAML_INVALID", f"YAML tidak valid: {exc}", path)
        return None
    if not isinstance(data, dict):
        _issue(issues, "ERROR", "META_ROOT",
               "Frontmatter YAML harus berupa object/map.", path)
        return None
    return data


def validate_skill_file(skill_file: Path, skills_root: Path,
                        permission_allowlist: set[str] | None = None) -> tuple[list[Issue], str | None]:
    issues: list[Issue] = []
    try:
        text = skill_file.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        _issue(issues, "ERROR", "FILE_READ", f"Tidak dapat membaca file UTF-8: {exc}", skill_file)
        return issues, None

    data = parse_frontmatter(text, skill_file, issues)
    if data is None:
        return issues, None

    for field in sorted(REQUIRED_FIELDS - data.keys()):
        _issue(issues, "ERROR", "META_REQUIRED", f"Field '{field}' wajib diisi.", skill_file)

    for field in ("skill_id", "name", "description", "category", "status"):
        if field in data and not _is_string(data[field]):
            _issue(issues, "ERROR", "META_STRING", f"'{field}' harus berupa string non-kosong.", skill_file)

    skill_id = data.get("skill_id") if isinstance(data.get("skill_id"), str) else None
    if skill_id and not SKILL_ID_RE.fullmatch(skill_id):
        _issue(issues, "ERROR", "SKILL_ID_FORMAT",
               "skill_id harus uppercase dan menggunakan segmen yang dipisahkan tanda '-'.", skill_file)

    version = data.get("version")
    if not isinstance(version, str) or not SEMVER_RE.fullmatch(version):
        _issue(issues, "ERROR", "VERSION_FORMAT",
               "version harus mengikuti Semantic Versioning MAJOR.MINOR.PATCH (contoh 1.0.0).", skill_file)

    status = data.get("status")
    if isinstance(status, str) and status not in STATUSES:
        _issue(issues, "ERROR", "STATUS_INVALID",
               f"status harus salah satu dari: {', '.join(sorted(STATUSES))}.", skill_file)

    author = _check_string_map(data, "author", {"type", "id"}, skill_file, issues)
    for field in ("type", "id"):
        if field in author and not _is_string(author[field]):
            _issue(issues, "ERROR", "AUTHOR_FIELD", f"author.{field} harus berupa string.", skill_file)

    source = _check_string_map(data, "source",
                               {"type", "repository", "original_skill", "license"},
                               skill_file, issues)
    if "type" in source and source["type"] not in {"internal", "adapted", "external"}:
        _issue(issues, "ERROR", "SOURCE_TYPE",
               "source.type harus internal, adapted, atau external.", skill_file)
    if "license" in source and not _is_string(source["license"]):
        _issue(issues, "ERROR", "SOURCE_LICENSE", "source.license harus berupa string non-kosong.", skill_file)
    for field in ("repository", "original_skill"):
        if field in source and source[field] is not None and not isinstance(source[field], str):
            _issue(issues, "ERROR", "SOURCE_FIELD", f"source.{field} harus string atau null.", skill_file)

    compatibility = _check_string_map(data, "compatibility",
                                      {"runtime_min", "providers", "agents"}, skill_file, issues)
    if "runtime_min" in compatibility and (
        not isinstance(compatibility["runtime_min"], str)
        or not SEMVER_RE.fullmatch(compatibility["runtime_min"])
    ):
        _issue(issues, "ERROR", "RUNTIME_VERSION",
               "compatibility.runtime_min harus berupa versi MAJOR.MINOR.PATCH.", skill_file)
    for field in ("providers", "agents"):
        if field in compatibility:
            _check_string_list(compatibility[field], f"compatibility.{field}", skill_file, issues)

    permissions = _check_string_map(data, "permissions",
                                    {"required", "optional", "approval_required"}, skill_file, issues)
    for field in ("required", "optional", "approval_required"):
        if field in permissions:
            _check_string_list(permissions[field], f"permissions.{field}", skill_file, issues)
            if isinstance(permissions[field], list) and permission_allowlist is not None:
                for permission in permissions[field]:
                    if isinstance(permission, str) and permission not in permission_allowlist:
                        _issue(issues, "WARNING", "PERMISSION_UNKNOWN",
                               f"Permission '{permission}' tidak ditemukan dalam allowlist yang diberikan.",
                               skill_file)

    dependencies = data.get("dependencies")
    _check_string_list(dependencies, "dependencies", skill_file, issues)
    if isinstance(dependencies, list):
        for dependency in dependencies:
            if isinstance(dependency, str) and (
                dependency.startswith(("/", "\\"))
                or ".." in Path(dependency.replace("\\", "/")).parts
            ):
                _issue(issues, "ERROR", "PATH_TRAVERSAL",
                       f"Dependency mengandung path traversal: {dependency}", skill_file)

    execution = _check_string_map(data, "execution",
                                  {"context_budget", "timeout_seconds", "retry_policy"},
                                  skill_file, issues)
    if "context_budget" in execution and not _is_string(execution["context_budget"]):
        _issue(issues, "ERROR", "EXECUTION_FIELD", "execution.context_budget harus berupa string.", skill_file)
    if "timeout_seconds" in execution and (
        not isinstance(execution["timeout_seconds"], int)
        or isinstance(execution["timeout_seconds"], bool)
        or execution["timeout_seconds"] <= 0
    ):
        _issue(issues, "ERROR", "TIMEOUT_INVALID", "execution.timeout_seconds harus integer positif.", skill_file)
    if "retry_policy" in execution and not _is_string(execution["retry_policy"]):
        _issue(issues, "ERROR", "EXECUTION_FIELD", "execution.retry_policy harus berupa string.", skill_file)

    evaluation = _check_string_map(data, "evaluation", {"required", "test_suite"}, skill_file, issues)
    if "required" in evaluation and not isinstance(evaluation["required"], bool):
        _issue(issues, "ERROR", "EVALUATION_FIELD", "evaluation.required harus boolean.", skill_file)
    if "test_suite" in evaluation and not _is_string(evaluation["test_suite"]):
        _issue(issues, "ERROR", "EVALUATION_FIELD", "evaluation.test_suite harus string non-kosong.", skill_file)

    _check_string_list(data.get("tags"), "tags", skill_file, issues)

    for field in ("created_at", "updated_at"):
        value = data.get(field)
        if not isinstance(value, str):
            _issue(issues, "ERROR", "DATE_FORMAT", f"{field} harus string ISO-8601 UTC.", skill_file)
            continue
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                raise ValueError("timezone tidak tersedia")
        except ValueError:
            _issue(issues, "ERROR", "DATE_FORMAT",
                   f"{field} harus timestamp ISO-8601 dengan timezone, contoh 2026-11-18T10:00:00Z.", skill_file)

    # Skill directory must be category/skill-name/SKILL.md.
    try:
        relative = skill_file.resolve().relative_to(skills_root.resolve())
        if len(relative.parts) != 3 or relative.name != "SKILL.md":
            _issue(issues, "ERROR", "DIRECTORY_LAYOUT",
                   "Lokasi harus library/skills/<category>/<skill-name>/SKILL.md.", skill_file)
        else:
            category_dir, skill_dir, _ = relative.parts
            if data.get("category") != category_dir:
                _issue(issues, "ERROR", "CATEGORY_PATH",
                       f"category '{data.get('category')}' harus sama dengan folder '{category_dir}'.", skill_file)
            if not SLUG_RE.fullmatch(skill_dir):
                _issue(issues, "ERROR", "DIRECTORY_SLUG",
                       "Nama folder skill harus slug lowercase dengan tanda '-' sebagai pemisah.", skill_file)
    except ValueError:
        _issue(issues, "ERROR", "OUTSIDE_SKILL_ROOT",
               "File skill berada di luar direktori library/skills.", skill_file)

    body = FRONTMATTER_RE.sub("", text, count=1)
    for section in REQUIRED_SECTIONS:
        heading = re.compile(r"^#{1,6}\s+" + re.escape(section) + r"\s*$", re.I | re.M)
        if not heading.search(body):
            _issue(issues, "ERROR", "CONTENT_SECTION",
                   f"Bagian Markdown '## {section}' belum ditemukan.", skill_file)

    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            _issue(issues, "ERROR", "POSSIBLE_SECRET",
                   "Pola credential/private key berisiko terdeteksi; periksa dan rotasi jika nyata.", skill_file)
            break

    return issues, skill_id


def validate_skills(root: Path, permission_allowlist: set[str] | None = None) -> list[Issue]:
    root = root.resolve()
    if not root.exists():
        return [Issue("ERROR", "ROOT_MISSING", f"Direktori tidak ditemukan: {root}", str(root))]
    skill_files = sorted(root.rglob("SKILL.md"))
    if not skill_files:
        return [Issue("WARNING", "NO_SKILLS", "Belum ada file SKILL.md untuk divalidasi.", str(root))]

    all_issues: list[Issue] = []
    seen: dict[str, Path] = {}
    for skill_file in skill_files:
        issues, skill_id = validate_skill_file(skill_file, root, permission_allowlist)
        all_issues.extend(issues)
        if skill_id:
            if skill_id in seen:
                all_issues.append(Issue(
                    "ERROR", "DUPLICATE_SKILL_ID",
                    f"ID '{skill_id}' juga digunakan oleh {seen[skill_id]}.",
                    str(skill_file),
                ))
            else:
                seen[skill_id] = skill_file
    return all_issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validasi metadata dan struktur skill AION.")
    parser.add_argument("--root", type=Path, default=Path("library/skills"),
                        help="Direktori root skill (default: library/skills).")
    parser.add_argument("--permissions-file", type=Path, default=None,
                        help="File teks berisi satu permission resmi per baris (opsional).")
    args = parser.parse_args(argv)

    allowlist = None
    if args.permissions_file:
        try:
            allowlist = {
                line.strip() for line in args.permissions_file.read_text(encoding="utf-8").splitlines()
                if line.strip() and not line.lstrip().startswith("#")
            }
        except OSError as exc:
            print(f"ERROR PERMISSION_FILE: {exc}", file=sys.stderr)
            return 2

    issues = validate_skills(args.root, allowlist)
    errors = sum(issue.severity == "ERROR" for issue in issues)
    warnings = sum(issue.severity == "WARNING" for issue in issues)

    if issues:
        for issue in issues:
            print(issue)
    else:
        print("OK: Semua skill yang ditemukan lolos pemeriksaan.")
    print(f"\nRingkasan: {errors} error, {warnings} warning.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
