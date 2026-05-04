# Personal Operations Harness

## One-line definition

A personal operations harness continuously collects work/life signals and converts them into executable actions, drafts, and reports.

## Role split

| Layer | Responsibility |
|---|---|
| long-term memory | people, relationships, history, decisions, searchable context |
| operations harness | new signal detection, queue updates, drafts, reporting, execution logs |

## Control loop

```text
Observe -> Normalize -> Understand -> Act -> Report -> Learn
```

## Main entities

| Entity | Meaning |
|---|---|
| Source Snapshot | raw collected source state at a point in time |
| Normalized Item | source-agnostic record |
| Action Candidate | an item the system could act on |
| Reminder Action | reminder/task materialized from an item |
| Draft Action | generated reply/follow-up draft |
| Report Profile | morning / progress / daily output lens |
| Fan-out | promotion of durable knowledge into long-term memory |

## Data-flow rule

Reports should never re-collect from live sources if shared artifacts already exist.

```text
collect snapshot
  -> normalize items
  -> classify items
  -> execute actions
  -> compose reports
  -> optional durable fan-out
```

## First implementation priorities

1. snapshot persistence
2. common item schema
3. classifier contract
4. reminder executor with dedupe
5. draft generator with context preservation
6. morning/progress/daily composers over shared artifacts

## Safety rules

- idempotency over cleverness
- degraded mode when a source is unhealthy
- conservative TODO creation at first
- durable-memory fan-out must be strict
