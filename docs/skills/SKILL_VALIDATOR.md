# KAME AION HABITAT — Skill Validator

**Document ID:** SKILL-006  
**Version:** 1.0.0  
**Status:** Draft / initial implementation

## Purpose

The local validator checks skill package metadata and Markdown structure against
`SKILL_FORMAT.md`. It is an authoring and quality gate, not a runtime permission
system or a security sandbox.

## Scope

- YAML frontmatter syntax and required metadata fields.
- Semantic version format and allowed lifecycle status.
- Basic nested metadata types.
- Skill ID format and duplicate IDs across the scanned library.
- Category-to-directory consistency and expected folder layout.
- Required Markdown section headings.
- Dependency path traversal patterns.
- A small set of high-confidence embedded-secret patterns.
- Optional permission allowlist supplied by an operator.

## Deliberate limitations

1. The current format document does not define a complete permission catalogue.
   Unknown permissions are therefore only reported when an explicit allowlist is
   supplied with `--permissions-file`.
2. Secret scanning is heuristic and cannot guarantee that a file contains no secrets.
3. Dependency names are checked for obvious traversal patterns; dependency
   resolution and integrity verification are not implemented.
4. This validator does not execute scripts, load skills into agents, approve skills,
   or grant permissions.
5. Content checks currently verify required headings, not semantic quality.

## Install

From the repository root:

```powershell
python -m pip install -r .\packages\skill-system\requirements.txt
```

## Run

```powershell
python .\scripts\validate_skills.py
```

Choose another directory:

```powershell
python .\scripts\validate_skills.py --root .\library\skills
```

Optional permission allowlist (one permission per line):

```powershell
python .\scripts\validate_skills.py --permissions-file .\docs\skills\permissions-allowlist.txt
```

## Tests

```powershell
python -m unittest discover -s .\packages\skill-system\tests -v
```

## Exit codes

- `0`: no validation errors (warnings may still exist).
- `1`: one or more validation errors.
- `2`: command configuration or permission allowlist read error.

## Security boundary

A successful validation result means only that the checked static conventions
passed. Runtime authorization must still be enforced by AION Tool Gateway and
Approval Manager immediately before each protected operation.
