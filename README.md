# prly

Prly is an open-source **personal operations harness**: a system that observes the signals around your work and turns them into actionable queues, drafts, and reports.

> **Prly turns signals into execution.**

Long-term context helps you recall people, projects, conversations, and decisions. Prly sits on top of that context layer and handles the operational loop:

- detect new signals
- normalize them into a common model
- decide what matters now
- create safe, deduplicated actions
- generate drafts and operator-facing reports

## What problem it solves

Modern personal work is fragmented across:

- mail
- chat / Slack / Discord
- calendar
- reminders / task managers
- recent AI or IDE sessions
- local machine and service health

Most tools stop at *showing* information. Prly is about turning that information into an execution layer.

## Core loop

```text
Observe -> Normalize -> Understand -> Act -> Report -> Learn
```

## Repository goals

This repository aims to become a practical, open-source foundation for:

- personal operations pipelines
- common item schemas for heterogeneous sources
- safe action execution with idempotency
- report composition from shared artifacts
- durable-memory fan-out into knowledge systems

## Scope

### Inputs
- mail metadata
- chat signals
- calendar events
- reminders / task state
- session history
- local health and runtime state

### Outputs
- TODO candidates
- reminder actions
- reply / follow-up drafts
- morning reports
- progress / interrupt reports
- daily wrap-up reports

## Principles

1. **collect once** — shared artifacts beat repeated live reads
2. **normalize early** — use a common item model across sources
3. **separate understanding from execution** — classification and actioning are different responsibilities
4. **prefer idempotency over cleverness** — duplicate actions destroy trust
5. **fan out durable facts only** — not every operational event belongs in long-term memory
6. **degrade visibly** — source failures should be explicit, not silent

## Initial repository layout

```text
.github/                     GitHub workflows, templates, and project hygiene
/docs/                       Product, architecture, roadmap, and contributor docs
+/packages/prly-core/         Core Python package for shared schemas and orchestration primitives (`import prly_core`)
+/tests/                      Repository-level tests
```

## Quick start

```bash
git clone https://github.com/kimjisub/prly.git
cd prly
python3 -m venv .venv
source .venv/bin/activate
python -m ensurepip --upgrade
python -m pip install --upgrade pip
pip install -e .[dev]
pytest -q
```

## What exists today

- repository bootstrap and CI
- initial product framing
- starter Python core package structure
- starter schema tests
- roadmap and issue scaffolding

## Documentation

- [Personal Operations Harness spec](docs/personal-operations-harness.md)
- [Architecture overview](docs/architecture.md)
- [Roadmap](docs/roadmap.md)
- [Contributing guide](CONTRIBUTING.md)

## Roadmap snapshot

### Phase 1 — Shared pipeline
- source snapshots
- normalized item schema
- classified artifacts
- reports built from shared artifacts only

### Phase 2 — Execution layer
- reminder executor
- draft generator
- action log and dedupe state

### Phase 3 — Policy layer
- approval queue
- auto-vs-manual action policies
- source health and degraded mode semantics

### Phase 4 — Learning layer
- durable fact promotion
- preference learning
- signal/noise optimization

## Contributing

Contributions are welcome, especially around:

- source adapters
- shared schemas
- action safety / dedupe design
- report composition
- local-first workflow tooling

Please start with [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
