from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


USERNAME = "GURUSARAN01"

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = REPOSITORY_ROOT / "data" / "contributions.json"

CONTRIBUTIONS_URL = (
    f"https://github.com/users/{USERNAME}/contributions"
)


def extract_contribution_count(
    day_element: Tag,
    soup: BeautifulSoup,
) -> int:
    """Try to extract the exact contribution count from GitHub's tooltip."""

    possible_texts: list[str] = []

    aria_description = day_element.get("aria-describedby")

    if isinstance(aria_description, str):
        description_element = soup.find(id=aria_description)

        if description_element:
            possible_texts.append(
                description_element.get_text(" ", strip=True)
            )

    element_id = day_element.get("id")

    if isinstance(element_id, str):
        tooltip = soup.find(
            "tool-tip",
            attrs={"for": element_id},
        )

        if tooltip:
            possible_texts.append(
                tooltip.get_text(" ", strip=True)
            )

    aria_label = day_element.get("aria-label")

    if isinstance(aria_label, str):
        possible_texts.append(aria_label)

    for text in possible_texts:
        match = re.search(
            r"([\d,]+)\s+contribution",
            text,
            flags=re.IGNORECASE,
        )

        if match:
            return int(match.group(1).replace(",", ""))

        if "no contributions" in text.lower():
            return 0

    return 0


def fetch_contributions() -> list[dict[str, object]]:
    """Download and parse the public GitHub contribution calendar."""

    headers = {
        "User-Agent": (
            "Mozilla/5.0 GitHub-Profile-README-Generator"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    print(f"Downloading contributions for {USERNAME}...")

    response = requests.get(
        CONTRIBUTIONS_URL,
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    day_elements = soup.select("[data-date][data-level]")

    if not day_elements:
        raise RuntimeError(
            "No contribution days were found. "
            "GitHub may have changed its page structure."
        )

    contributions_by_date: dict[str, dict[str, object]] = {}

    for day_element in day_elements:
        date_value = day_element.get("data-date")
        level_value = day_element.get("data-level", "0")

        if not isinstance(date_value, str):
            continue

        try:
            level = int(str(level_value))
        except ValueError:
            level = 0

        level = max(0, min(level, 4))

        count = extract_contribution_count(
            day_element=day_element,
            soup=soup,
        )

        contributions_by_date[date_value] = {
            "date": date_value,
            "count": count,
            "level": level,
        }

    contributions = sorted(
        contributions_by_date.values(),
        key=lambda item: str(item["date"]),
    )

    return contributions


def save_contributions(
    contributions: list[dict[str, object]],
) -> None:
    """Save the parsed contribution data as JSON."""

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_data = {
        "username": USERNAME,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "source": CONTRIBUTIONS_URL,
        "days": contributions,
    }

    OUTPUT_FILE.write_text(
        json.dumps(
            output_data,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


def main() -> None:
    contributions = fetch_contributions()

    if not contributions:
        raise RuntimeError(
            "GitHub returned no contribution records."
        )

    save_contributions(contributions)

    first_date = contributions[0]["date"]
    last_date = contributions[-1]["date"]

    print("Contribution data downloaded successfully.")
    print(f"Days collected: {len(contributions)}")
    print(f"Date range: {first_date} to {last_date}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()