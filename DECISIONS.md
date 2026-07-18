# Decision Log

An append-only, chronological record of decisions shaping this eval: what was decided, why, and what alternatives were considered. Maintained continuously via the repo's `decision-log` skill (see `.claude/skills/decision-log/`). Entries are never rewritten; reversals get new entries and a Status update on the old one. Tradeoffs are cross-referenced in [LIMITATIONS.md](LIMITATIONS.md).

---

## D-001 — Maintain continuous decision and limitations logs
- **Date:** 2026-07-18
- **Status:** active
- **Decided by:** Emily
- **Decision:** Keep an append-only decision log (this file) and a known-limitations log (LIMITATIONS.md), updated automatically during development via a repo-local Claude Code skill, with all eval-building work done in Claude Code.
- **Why:** So there is a transparent, auditable record of why each scope/design/implementation decision was made and what alternatives were considered — and so limitations are captured as they arise during the build rather than reconstructed from memory afterwards.
- **Alternatives considered:** Writing up limitations retrospectively at the end (rejected: relies on remembering every tradeoff; undermines the auditability the project's honesty guardrails call for). None others discussed.
- **Limitations:** none known
