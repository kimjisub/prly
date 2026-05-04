# Personal Operations Harness

> **gbrain is memory. Prly is execution.**

Prly defines an operational layer that continuously collects work signals and turns them into executable actions, drafts, and reports.

---

## Why this exists

A real day is not composed only of tickets or code changes.

New action items appear through:

- mail
- Slack or chat threads
- calendar changes
- reminders / task state
- recent AI or IDE sessions
- local system / service health

Most software stops at *displaying* these signals. A personal operations harness exists to bridge the gap between **seeing** and **acting**.

---

## Product definition

A personal operations harness is a system that:

1. observes heterogeneous personal-work signals
2. normalizes them into a shared item model
3. classifies urgency, ownership, and report fit
4. executes bounded actions safely
5. composes reusable reports from shared artifacts
6. promotes only durable facts into long-term memory

---

## Role split

| Layer | Responsibility |
|---|---|
| long-term memory | people, organizations, relationships, project history, decisions, searchable context |
| personal operations harness | new-signal detection, action queue updates, drafts, reminders, report generation, execution logs |

### What belongs to long-term memory
- durable people / org / project facts
- decisions worth revisiting later
- relationship or context changes
- reusable insights

### What should stay in the harness
- transient operational noise
- one-off TODO mechanics
- repeated snapshots and intermediate artifacts
- source health status and action logs

---

## Core loop

```text
Observe -> Normalize -> Understand -> Act -> Report -> Learn
```

### Observe
Collectors read source-specific systems:
- mail
- chat
- calendar
- reminders
- session history
- local health

### Normalize
All sources are converted into a common item model so later layers can stay source-agnostic.

### Understand
The understanding layer determines:
- urgency
- importance
- actionability
- draftability
- TODO candidacy
- report fit
- due hints

### Act
The system performs bounded actions such as:
- creating reminder entries
- generating draft replies
- appending execution logs
- notifying the operator of urgent changes

### Report
Reports are views over shared artifacts:
- morning report
- progress / interrupt report
- daily report

### Learn
The system improves over time by tracking:
- repeated patterns
- false positives
- useful drafts vs ignored drafts
- durable vs noisy information

---

## Key problems addressed

### 1. Information exists, but execution queues are stale
People notice action items in inboxes and chats, but often never move them into a trusted queue.

### 2. Briefings exist, but action layers are missing
Summaries are useful but incomplete if they do not connect to reminders, drafts, and follow-up state.

### 3. Long-term memory and short-term execution are separate systems
Memory tools remember context; execution tools need to transform current signals into action.

---

## Data flow

```text
collect snapshots
  -> normalize items
  -> classify items
  -> execute actions
  -> compose reports
  -> optional durable fan-out
```

### Architectural rule

**Reports should never re-collect from live sources when shared artifacts already exist.**

This keeps the system:
- reproducible
- easier to test
- easier to debug
- less wasteful with external integrations

---

## Core entities

| Entity | Meaning |
|---|---|
| Source Snapshot | raw collected source state at a point in time |
| Normalized Item | source-agnostic record ready for classification |
| Action Candidate | a classified item that could be acted on |
| Reminder Action | task/reminder materialized from an item |
| Draft Action | generated reply or follow-up draft |
| Report Profile | morning / progress / daily report lens |
| Fan-out | promotion of durable knowledge into long-term memory |

---

## Safety rules

1. **Idempotency over cleverness**
   - duplicate tasks destroy trust faster than missing one insight
2. **Visible degraded mode**
   - partial source failure should degrade gracefully and explicitly
3. **Conservative action creation**
   - start with a narrow definition of TODO-worthy items
4. **Strict durable-memory promotion**
   - operational noise must not pollute memory systems
5. **Auditability**
   - action logs and dedupe keys should explain what happened and why

---

## Execution layer priorities

### Reminder executor
Turns user-owned TODO candidates into actual reminder entries with dedupe protection.

### Draft generator
Produces operator-editable drafts for:
- mail replies
- chat replies
- follow-up messages
- schedule and priority notes

### Report composers
Build concise report views over shared artifacts.

#### Morning
- today’s schedule
- important new know/do items
- reminder additions
- ready-to-edit drafts
- source health warnings

#### Progress / Interrupt
- new urgent signals since the last snapshot
- new reminders
- new drafts
- source failures or operational changes

#### Daily
- what happened today
- what was handled
- what remains open
- what rolls into tomorrow

---

## Recommended implementation phases

### Phase 1 — shared pipeline foundation
- snapshot persistence
- normalized item schema
- classification contract
- reports over shared artifacts only

### Phase 2 — execution layer
- reminder executor
- draft generator
- action logs
- dedupe state

### Phase 3 — approval and policy layer
- review queue
- confidence thresholds
- auto-vs-manual action policies

### Phase 4 — learning and durable fan-out
- durable fact promotion
- preference learning
- signal/noise optimization

---

## Strategic interpretation

Prly started from the idea of orchestration. This harness applies the same orchestration logic to personal operations:

```text
observe signals
-> understand state
-> create executable work units
-> dispatch action
-> report progress
-> learn from outcomes
```

That is why this project is more than a collection of scripts. It is a candidate execution model for personal operations.
