# Architecture Overview

## System shape

Prly is designed as a pipeline, not a single monolith command.

```text
collectors -> snapshots -> normalization -> classification -> actions -> reports -> durable fan-out
```

## Layers

### 1. Collectors

Collectors read source-specific systems:
- mail
- chat
- calendar
- reminders
- session history
- local health

Their job is to capture source state, not to decide what matters.

### 2. Shared artifacts

Collected data is persisted into source snapshots. This is the contract between observation and the rest of the system.

### 3. Understanding layer

The understanding layer turns heterogeneous source data into a source-agnostic item model and classifies:

- urgency
- importance
- actionability
- draftability
- report fit
- due hints

### 4. Action layer

The action layer performs bounded work:

- create reminders
- create drafts
- append action logs
- enforce dedupe / idempotency

### 5. Report layer

Reports should be generated from shared artifacts, not fresh live reads.

Core report profiles:
- morning
- progress / interrupt
- daily

### 6. Durable memory fan-out

Only durable facts should be promoted out of the operational loop into a long-term memory layer.

## Design rules

1. collectors should be dumb and reliable
2. shared schemas should be stable and explicit
3. action execution should be auditable
4. degraded mode should remain usable
5. operational noise should not pollute durable memory
