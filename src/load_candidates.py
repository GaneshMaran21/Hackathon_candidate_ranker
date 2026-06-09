"""Candidate loading utilities."""

from __future__ import annotations

import gzip
import json
from pathlib import Path
from typing import Any, Generator, Iterable

try:
    import orjson
except ImportError:  # pragma: no cover
    orjson = None


def _parse_line(line: str) -> dict[str, Any]:
    if orjson is not None:
        return orjson.loads(line)
    return json.loads(line)


def open_candidates(path: Path):
    path = Path(path)
    if path.suffix == ".gz" or path.name.endswith(".jsonl.gz"):
        return gzip.open(path, "rt", encoding="utf-8")
    return open(path, "r", encoding="utf-8")


def iter_candidates(path: Path) -> Generator[dict[str, Any], None, None]:
    path = Path(path)
    if path.suffix == ".json" and not path.name.endswith(".jsonl"):
        text = path.read_text(encoding="utf-8")
        data = orjson.loads(text) if orjson is not None else json.loads(text)
        if isinstance(data, list):
            for item in data:
                yield item
            return
        if isinstance(data, dict):
            yield data
            return
        raise ValueError(f"Unsupported JSON structure in {path}")

    with open_candidates(path) as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield _parse_line(line)


def load_candidates(path: Path) -> list[dict[str, Any]]:
    return list(iter_candidates(path))


def count_candidates(path: Path) -> int:
    count = 0
    with open_candidates(path) as handle:
        for line in handle:
            if line.strip():
                count += 1
    return count


def load_job_description(path: Path | None = None) -> str:
    jd_path = path or Path(__file__).resolve().parent.parent / "data" / "job_description.txt"
    return jd_path.read_text(encoding="utf-8")
