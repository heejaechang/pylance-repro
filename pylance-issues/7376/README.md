# Issue #7376 — Completion sort order: own properties before inherited methods

**Issue**: https://github.com/microsoft/pylance-release/issues/7376  
**Type**: Enhancement request  
**Reporter**: @dahnny012

## Repro Steps (from issue body)

1. Open `models.py` which defines `EvaluationBatchOutput(BaseModel)` with fields: `job_id`, `status`, `results`, `error`
2. In `main.py`, type `output.` to trigger completions on an instance of `EvaluationBatchOutput`
3. Observe the completion list order

## Expected (verbatim from issue)

> I would expect to see [job_id, status, results, error] as the first few options when using my model

## Actual

All normal (non-dunder, non-private) symbols are sorted alphabetically within the `NormalSymbol` category. The user's own fields (`job_id`, `status`, `results`, `error`) are interleaved with inherited BaseModel methods (e.g., `copy`, `dict`, `json`, `model_computed_fields`, `model_config`, etc.) in purely alphabetical order.

## Verification Checklist

- [ ] Trigger completions at `output.` in `main.py`
- [ ] Confirm that own fields (`job_id`, `status`, `results`, `error`) do NOT appear grouped before inherited methods
- [ ] This confirms the enhancement request is valid — no existing mechanism sorts own fields first

## Notes

- `requirements.txt` declares `pydantic>=2.0` since the reporter uses Pydantic BaseModel
- This is an enhancement, not a bug — the current alphabetical sorting is by design
- Related issues: #3925 (smart ordering), #3575 (outline sorting)
