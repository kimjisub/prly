# Data Model

This document defines the initial shared schema vocabulary for Prly.

## SourceSnapshot

Represents the result of a single collection event.

### Fields
- `snapshot_id`: unique snapshot identifier
- `source`: source type such as `mail` or `slack`
- `source_account`: account / workspace / tenant identifier
- `collected_at`: ISO timestamp
- `item_count`: number of source records collected
- `health`: collector health summary
- `path`: persisted artifact path

## NormalizedItem

Represents a source-agnostic operational item.

### Required fields
- `id`
- `source`
- `kind`
- `title`
- `summary`
- `timestamp`

### Classification-related fields
- `urgency`
- `actionability`
- `draftable`
- `todo_candidate`
- `report_fit`
- `dedupe_key`

## ActionCandidate

Wraps a normalized item with an intended action and the reasoning behind it.

## DraftAction

Represents generated operator-editable output for reports and follow-up workflows.

## Near-term model expansion candidates

- due hints
- participants
- URLs and deep links
- confidence fields
- source snapshot backlinks
- action result references
