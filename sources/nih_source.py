import requests


def fetch_nih_opportunities():
    """
    Fetch NIH training / internship programs from a hypothetical NIH API.
    NIH has multiple APIs; you’d adapt this to the real one you choose.
    """
    # Placeholder URL – replace with real NIH training / internships endpoint.
    url = "https://api.nih.gov/example/training-programs"

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"[NIH] Error fetching data: {e}")
        return []

    opportunities = []

    for item in data.get("results", []):
        opportunities.append({
            "title": item.get("program_name", "").strip(),
            "organization": item.get("institute", "NIH").strip(),
            "field": item.get("field", "Biomedical").strip(),
            "description": item.get("description", "").strip(),
            "requirements": item.get("eligibility", "").strip(),
            "citizenship": item.get("citizenship", "").strip(),
            "grade_level": item.get("grade_level", "").strip(),
            "location": item.get("location", "").strip(),
            "deadline": item.get("deadline", "").strip(),
            "url": item.get("url", "").strip(),
        })

    print(f"[NIH] Fetched {len(opportunities)} opportunities")
    return opportunities