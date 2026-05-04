# Contributing to prly

Thanks for your interest in Prly.

## Project direction

Prly is building an open-source personal operations harness:

- collect signals once
- normalize them into shared artifacts
- classify what matters
- execute safe actions with dedupe
- compose reports from shared outputs

## Development setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m ensurepip --upgrade
python -m pip install --upgrade pip
pip install -e .[dev]
pytest -q
```

## Contribution guidelines

1. prefer small, focused changes
2. keep schemas explicit and source-agnostic
3. prioritize idempotency and auditability in action execution
4. document assumptions in `docs/`
5. add or update tests for behavior changes

## Pull requests

Please include:

- what changed
- why it changed
- how it was validated
- any docs or roadmap implications

## Good first contribution areas

- source adapters and fixture design
- normalized schema improvements
- report composition logic
- action safety / dedupe logic
- docs and examples
