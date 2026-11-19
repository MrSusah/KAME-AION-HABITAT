# KAME AION HABITAT

**Product:** AION Habitat  
**Interface:** AION Office  
**Slogan:** The Living AI Office

KAME AION HABITAT is a supervised-autonomy AI office platform.
It coordinates specialized AI agents, projects, tools, memory,
quality assurance, and user-approved actions.

## Project principles

- Supervised autonomy: the user retains control over consequential actions.
- Modular architecture: components remain independently testable.
- Local-first: minimize resource usage and unnecessary cloud dependencies.
- Provider-independent AI Gateway.
- Permission-controlled Tool Gateway.
- Quality assurance for every completed task.
- Auditable actions and recoverable project state.
- Private agent memory and permission-based shared knowledge.

## Repository structure

- `apps/` — user-facing applications and API.
- `packages/` — reusable runtime and platform modules.
- `database/` — schema and migration-related assets.
- `infrastructure/` — deployment and infrastructure configuration.
- `docs/` — specifications, architecture, decisions, and audits.
- `tests/` — automated tests.
- `scripts/` — development and maintenance scripts.
- `storage/` — local runtime storage; user data is not committed.

## Current status

Workspace foundation initialized.

No production application implementation is implied by this
initial structure. Refer to the approved specifications and
Build Blueprint before implementing components.

## Security

Never commit API keys, passwords, tokens, private certificates,
or real user data. Use environment variables and local secret
storage. Consequential external actions require authorization.
