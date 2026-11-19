# KAME AION HABITAT — Stage 10 Core Skills

This package adds seven AION-native skill specifications to `library/skills/`.

## Included skills

| Skill ID | Category | Purpose |
|---|---|---|
| AION-PLAN-001 | planning | Task planning and decomposition |
| AION-EXEC-001 | execution | Controlled task execution |
| AION-TDD-001 | development | Test-driven development |
| AION-VERIFY-001 | quality-assurance | Verification and evidence report |
| AION-SEC-001 | security | Security review |
| AION-RECOVERY-001 | recovery | Task state, recovery and cancellation |
| AION-REVIEW-001 | quality-assurance | Independent code and work review |

## Installation

Extract the ZIP. Copy the contents of its `KAME-AION-HABITAT` directory into the root of your existing workspace. Do not overwrite existing files; this package only adds new skill folders and this README.

## Validation

From the project root, run:

```powershell
.\.venv\Scripts\python.exe .\scripts\validate_skills.py --root .\library\skills
```

## Lifecycle

All included skills are `draft`. They are specifications, not executable plugins or autonomous permissions. Review, test, and approve each skill through the AION skill governance process before enabling runtime routing.

The `permissions` arrays are intentionally empty until AION's authoritative permission registry and allowlist are finalized. Operational safety constraints are documented in each skill body; they do not grant tool access.

## Important limits

- These files do not implement the Skill Registry, Loader, Router, Evaluator, or runtime.
- The listed references are expected project documents from Stage 9.4; if any are absent, resolve the references before approval.
- No third-party skill code or assets are included.
