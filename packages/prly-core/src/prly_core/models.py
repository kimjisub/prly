from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class ItemKind(str, Enum):
    MESSAGE = "message"
    EVENT = "event"
    REMINDER = "reminder"
    SESSION = "session"
    HEALTH = "health"


class Urgency(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Actionability(str, Enum):
    USER = "user"
    WAIT = "wait"
    IGNORE = "ignore"


class ReportProfile(str, Enum):
    MORNING = "morning"
    PROGRESS = "progress"
    DAILY = "daily"


@dataclass(frozen=True)
class SourceSnapshot:
    snapshot_id: str
    source: str
    source_account: str
    collected_at: str
    item_count: int
    health: str
    path: str


@dataclass(frozen=True)
class NormalizedItem:
    id: str
    source: str
    kind: ItemKind
    title: str
    summary: str
    timestamp: str
    urgency: Urgency = Urgency.MEDIUM
    actionability: Actionability = Actionability.WAIT
    draftable: bool = False
    todo_candidate: bool = False
    report_fit: tuple[ReportProfile, ...] = field(default_factory=tuple)
    dedupe_key: str = ""


@dataclass(frozen=True)
class ActionCandidate:
    item: NormalizedItem
    action_type: str
    rationale: str


@dataclass(frozen=True)
class DraftAction:
    item_id: str
    draft_type: str
    tone: str
    subject: str
    body: str
    confidence: str
