import pandas as pd
from sources.sample_api_source import fetch_api_opportunities
from sources.sample_html_source import fetch_html_opportunities


# ---------------------------------------------------------
# Filtering Logic
# ---------------------------------------------------------

def is_inclusive_citizenship(text: str) -> bool:
    """Return True if the opportunity explicitly welcomes non‑US citizens."""
    if not text:
        return False

    text = text.lower()

    allow_keywords = [
        "international students welcome",
        "no citizenship required",
        "open to all students",
        "daca",
        "visa sponsorship",
        "eligible regardless of citizenship"
    ]

    block_keywords = [
        "u.s. citizens only",
        "us citizens only",
        "must be a u.s. citizen",
        "must be us citizen",
        "citizenship required"
    ]

    if any(bad in text for bad in block_keywords):
        return False

    return any(good in text for good in allow_keywords)


def is_high_school_eligible(text: str) -> bool:
    """Return True if the opportunity is open to high school students."""
    if not text:
        return False

    text = text.lower()

    hs_keywords = [
        "high school students may apply",
        "open to high school",
        "grades 9-12",
        "secondary school",
        "pre-college"
    ]

    return any(k in text for k in hs_keywords)


def filter_opportunities(opps):
    """Apply all filtering rules."""
    filtered = []

    for opp in opps:
        citizenship_text = (opp.get("citizenship") or "") + " " + (opp.get("description") or "")
        eligibility_text = (opp.get("requirements") or "") + " " + (opp.get("description") or "")

        # Citizenship filter
        if not is_inclusive_citizenship(citizenship_text):
            continue

        # High school eligibility filter
        if not is_high_school_eligible(eligibility_text):
            continue

        filtered.append(opp)

    return filtered


# ---------------------------------------------------------
# Export to Excel
# ---------------------------------------------------------

def save_to_excel(opportunities, filename="vibecode_results.xlsx"):
    df = pd.DataFrame(opportunities)
    df.to_excel(filename, index=False)
    print(f"Saved {len(opportunities)} opportunities to {filename}")


# ---------------------------------------------------------
# Helper: Return only high‑school‑eligible opportunities
# ---------------------------------------------------------

def get_high_school_only(opportunities):
    """Return only opportunities explicitly open to high school students."""
    return [opp for opp in opportunities if is_high_school_eligible(
        (opp.get("requirements") or "") + " " + (opp.get("description") or "")
    )]


# ---------------------------------------------------------
# Main Pipeline
# ---------------------------------------------------------

def main():
    print("Collecting opportunities...")

    all_opportunities = []

    # Add new sources here
    all_opportunities.extend(fetch_api_opportunities())
    all_opportunities.extend(fetch_html_opportunities())

    print(f"Fetched {len(all_opportunities)} raw opportunities")

    filtered = filter_opportunities(all_opportunities)

    print(f"Matched {len(filtered)} opportunities after filtering")

    save_to_excel(filtered)

    print("\nSummary:")
    for opp in filtered:
        print(f"- {opp['title']} ({opp['organization']})")


if __name__ == "__main__":
    main()