# prly

Prly is an open-source **personal operations harness**.

It continuously observes personal work signals — mail, chat, calendar, reminders, session history, and system health — then turns them into:

- actionable queue entries
- draft replies and follow-ups
- morning / progress / daily reports
- durable fact fan-out into long-term memory systems

## Core idea

> gbrain is memory. Prly is execution.

Long-term memory systems are good at remembering people, projects, decisions, and relationships.
Prly is the operational layer on top: it notices new signals, classifies what matters, creates actions safely, and presents concise reports.

## Product loop

```text
Observe -> Normalize -> Understand -> Act -> Report -> Learn
```

## Initial scope

### Inputs
- mail metadata
- Slack / chat signals
- calendar events
- reminders state
- session history
- local machine / service health

### Outputs
- TODO candidates
- reminder actions
- draft replies
- progress updates
- daily summaries

## Principles

1. collect once
2. normalize into a common item model
3. separate understanding from execution
4. make actions idempotent
5. send only durable facts to long-term memory

## Repository structure

```text
.github/                 GitHub workflows and contribution templates
/docs/                   product and architecture docs
```

## Roadmap

### Phase 1 — shared pipeline
- snapshot storage
- normalized item model
- classified outputs
- reports read shared artifacts instead of live sources

### Phase 2 — execution layer
- reminder executor
- draft generator
- action logs
- dedupe / idempotency

### Phase 3 — approval policies
- auto vs approval-gated execution
- review queue
- source-specific policies

### Phase 4 — learning and memory fan-out
- durable fact extraction
- user preference learning
- signal/noise improvement loop

## Status

Early repository bootstrap. The current focus is open-source framing, workflow scaffolding, and architecture definition.

## License

MIT
