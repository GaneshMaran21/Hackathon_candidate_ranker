"""Text construction helpers for candidates and JD."""

from __future__ import annotations

from typing import Any


def build_candidate_text(candidate: dict[str, Any]) -> str:
    profile = candidate.get("profile", {})
    parts = [
        profile.get("headline", ""),
        profile.get("summary", ""),
        profile.get("current_title", ""),
        profile.get("current_company", ""),
        profile.get("current_industry", ""),
    ]
    for role in candidate.get("career_history", []):
        parts.extend([
            role.get("title", ""),
            role.get("company", ""),
            role.get("industry", ""),
            role.get("description", ""),
        ])
    for skill in candidate.get("skills", []):
        parts.append(skill.get("name", ""))
    for edu in candidate.get("education", []):
        parts.extend([
            edu.get("institution", ""),
            edu.get("degree", ""),
            edu.get("field_of_study", ""),
        ])
    return " ".join(p for p in parts if p).strip()


def build_career_text(candidate: dict[str, Any]) -> str:
    profile = candidate.get("profile", {})
    parts = [profile.get("summary", ""), profile.get("current_title", "")]
    for role in candidate.get("career_history", []):
        parts.extend([role.get("title", ""), role.get("description", "")])
    return " ".join(p for p in parts if p).lower()


def tokenize(text: str) -> list[str]:
    return [tok for tok in text.lower().split() if len(tok) > 2]
