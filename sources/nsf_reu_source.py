import requests


def fetch_nsf_reu_opportunities():
    """
    Fetch NSF REU sites from a hypothetical NSF API.
    NSF has a developer portal; you’d adapt this to their real schema.
    """
    # Placeholder URL – replace with real NSF REU endpoint.
    url = "https://api.nsf.gov/services/v1/reu.json"

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"[NSF REU] Error fetching data: {e}")
        return []

    opportunities = []

    # Adjust to real structure
    for item in data.get("results", []):
        description = item.get("abstract", "")
        eligibility = item.get("eligibility", "")

        opportunities.append({
            "title": item.get("title", "").strip(),
            "organization": item.get("institution", "").strip(),
            "field": item.get("field", "STEM").strip(),
            "description": description.strip(),
            "requirements": eligibility.strip(),
            "citizenship": item.get("citizenship", "").strip(),
            "grade_level": "Undergrad / sometimes HS",
            "location": item.get("location", "").strip(),
            "deadline": item.get("deadline", "").strip(),
            "url": item.get("url", "").strip(),
        })

    print(f"[NSF REU] Fetched {len(opportunities)} opportunities")
    return opportunities