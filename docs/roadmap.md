# Roadmap

## Phase 1 — Shared pipeline foundation

**Goal:** Build the data contracts that let reports and actions share the same source artifacts.

### Deliverables
- source snapshot model
- normalized item schema
- initial classification contract
- report composers read shared artifacts only
- basic fixtures and tests

## Phase 2 — Execution layer

**Goal:** Turn classified items into safe, deduplicated actions.

### Deliverables
- reminder executor
- draft generator
- action log schema
- dedupe state management
- degraded-mode behavior when sources are partially unavailable

## Phase 3 — Policy and review

**Goal:** Make automation tunable and safe.

### Deliverables
- approval queue
- source-level and action-level policies
- confidence thresholds
- manual override / replay model

## Phase 4 — Learning and durable fan-out

**Goal:** Improve prioritization and memory quality over time.

### Deliverables
- durable-fact promotion rules
- preference learning hooks
- false-positive / noise analysis loop
- action outcome feedback model
