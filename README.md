# Redrob Intelligent Candidate Ranker

Hybrid, trap-aware ranking system for the **Senior AI Engineer (search / retrieval / ranking)** role in the Redrob Data & AI Challenge.

## Approach

This ranker combines:

1. **Trap and honeypot penalties** — removes keyword stuffers, recycled profiles, title/summary mismatches, and impossible records
2. **Role-fit scoring** — rewards production IR/ranking evidence in career history and titles
3. **Hybrid retrieval** — offline MiniLM embeddings + BM25 lexical match against the JD
4. **Skills trust** — proficiency × endorsements × duration × Redrob assessments
5. **Behavioral modifier** — availability and engagement signals from `redrob_signals`

## Requirements

- Python 3.11+
- 8 GB RAM minimum for ranking (precompute may take longer and benefits from patience)
- No network during `rank.py` execution

## Setup

```bash
cd redrob-ranker
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Precompute (run once offline)

Precompute embeddings and BM25 artifacts from the full candidate pool:

```bash
python scripts/precompute.py --candidates ../India_runs_data_and_ai_challenge/candidates.jsonl
python scripts/verify_artifacts.py
python scripts/repair_embeddings.py --candidates ../India_runs_data_and_ai_challenge/candidates.jsonl  # if verify reports bad rows
```

Quick demo on the 50-candidate sample:

```bash
python scripts/precompute.py --candidates ../India_runs_data_and_ai_challenge/sample_candidates.json --artifacts artifacts_demo --limit 50
```

This writes to `artifacts/`:

- `embeddings.npy`
- `jd_embedding.npy`
- `bm25.pkl`
- `metadata.json`

## Produce submission CSV

```bash
python rank.py --candidates ../India_runs_data_and_ai_challenge/candidates.jsonl --out ./submission.csv
```

Validate format:

```bash
python ../India_runs_data_and_ai_challenge/validate_submission.py submission.csv
```

## Streamlit sandbox (HuggingFace Spaces)

```bash
streamlit run app/app.py
```

Deploy the repo to HuggingFace Spaces with:

- App file: `app/app.py`
- Include `artifacts/` or run precompute in the Space build step
- Python 3.11 + `requirements.txt`

## Project layout

```
rank.py                 # Single reproduce command entrypoint
scripts/precompute.py   # Offline artifact generation
src/                    # Feature, scoring, reasoning modules
artifacts/              # Precomputed embeddings and BM25 index
app/app.py              # Streamlit demo
submission_metadata.yaml
docs/presentation.pdf   # Team deck
```

## Reproduce command

```bash
python rank.py --candidates ./candidates.jsonl --out ./submission.csv
```

## Notes

- `sample_submission.csv` in the bundle is a **format-only anti-pattern**. Do not copy its ranking logic.
- AI tools may be used during development, but ranking must remain fully offline.
- Update `submission_metadata.yaml` with your real team details before portal upload.
