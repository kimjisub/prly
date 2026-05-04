from dataclasses import asdict

from prly_core.models import (
    ActionCandidate,
    Actionability,
    DraftAction,
    ItemKind,
    NormalizedItem,
    ReportProfile,
    SourceSnapshot,
    Urgency,
)


def test_source_snapshot_preserves_core_metadata() -> None:
    snapshot = SourceSnapshot(
        snapshot_id="2026-05-04T21:00:00+09:00",
        source="mail",
        source_account="personal",
        collected_at="2026-05-04T21:00:00+09:00",
        item_count=3,
        health="ok",
        path="data/snapshots/mail.json",
    )

    assert snapshot.source == "mail"
    assert snapshot.health == "ok"
    assert asdict(snapshot)["item_count"] == 3


def test_normalized_item_captures_report_and_action_metadata() -> None:
    item = NormalizedItem(
        id="slack-candid-123",
        source="slack",
        kind=ItemKind.MESSAGE,
        title="Talent Map follow-up",
        summary="Need a reply and a follow-up task",
        timestamp="2026-05-04T11:21:00+09:00",
        urgency=Urgency.HIGH,
        actionability=Actionability.USER,
        draftable=True,
        todo_candidate=True,
        report_fit=(ReportProfile.MORNING, ReportProfile.PROGRESS),
        dedupe_key="slack:candid:thread-abc:followup",
    )

    assert item.kind is ItemKind.MESSAGE
    assert item.urgency is Urgency.HIGH
    assert item.todo_candidate is True
    assert ReportProfile.PROGRESS in item.report_fit


def test_action_candidate_wraps_normalized_item_with_reasoning() -> None:
    item = NormalizedItem(
        id="mail-123",
        source="mail",
        kind=ItemKind.MESSAGE,
        title="Review contract timing",
        summary="Need to respond this week",
        timestamp="2026-05-04T09:00:00+09:00",
        actionability=Actionability.USER,
        todo_candidate=True,
        dedupe_key="mail:123:reply",
    )

    candidate = ActionCandidate(
        item=item,
        action_type="reminder_create",
        rationale="User-owned follow-up with explicit response expectation",
    )

    assert candidate.item.id == "mail-123"
    assert candidate.action_type == "reminder_create"
    assert "response expectation" in candidate.rationale


def test_draft_action_stores_output_shape_for_reports() -> None:
    draft = DraftAction(
        item_id="mail-123",
        draft_type="mail_reply",
        tone="concise-professional",
        subject="Re: Review contract timing",
        body="안녕하세요. 이번 주 안에 검토 후 회신드리겠습니다.",
        confidence="medium",
    )

    assert draft.draft_type == "mail_reply"
    assert draft.subject.startswith("Re:")
    assert draft.confidence == "medium"
