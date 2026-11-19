# AGENTS.md — KAME AION HABITAT

## Project identity

- Project: KAME AION HABITAT
- Product: AION Habitat
- Desktop/dashboard: AION Office
- Slogan: The Living AI Office

## Mandatory working rules

1. Read relevant project specifications before implementation.
2. Do not invent requirements when specifications are silent.
   Record assumptions and request a decision when necessary.
3. Preserve existing work. Inspect before modifying or deleting.
4. Do not access sibling projects unless explicitly authorized.
5. Never expose, commit, or log secrets and credentials.
6. Do not perform financial, destructive, public, or consequential
   external actions without the required user approval.
7. Write tests for implemented behavior.
8. Run relevant tests and report actual results.
9. Keep changes modular, documented, and reviewable.
10. Do not claim that a feature is implemented or tested unless
    evidence supports that claim.

## Architecture principles

- Modular monolith as the initial architecture.
- React + TypeScript for the web interface.
- FastAPI for the backend.
- PostgreSQL as the primary relational database.
- Provider-independent AI Gateway.
- Permission-controlled Tool Gateway.
- Local-first file storage in the initial deployment.
- Optional desktop shell after the web MVP is validated.

## Resource constraints

The initial development machine is a modest Windows PC with
approximately 8 GB RAM available to the Linux environment.
Prefer lightweight services and avoid unnecessary containers
or always-running heavyweight models.

## Required workflow

For significant changes:

1. Inspect relevant files and dependencies.
2. Explain the intended change.
3. Implement the smallest coherent change.
4. Run tests, type checks, and relevant security checks.
5. Review the diff for unintended changes.
6. Report changed files, test results, risks, and next steps.

## Documentation

Record architectural decisions in `docs/decisions/`.
Keep specifications in `docs/specifications/`.
Keep audit reports in `docs/audits/`.
