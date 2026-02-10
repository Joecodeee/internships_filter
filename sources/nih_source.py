import os
import requests


def fetch_nasa_opportunities():
    """
    Fetch NASA internships / programs from a hypothetical NASA endpoint.
    You must:
      1. Get an API key from https://api.nasa.gov/
      2. Set it as an environment variable: NASA_API_KEY
    """
    api_key = os.getenv("NASA_API_KEY", "")
    if not api_key:
        # Beginner-friendly: just return empty if no key set
        print("[NASA] No NASA_API_KEY set, skipping NASA source.")
        return []

    # NOTE: This is a placeholder URL – replace with the real internships endpoint.
    url = "https://api.nasa.gov/example/internships"
    params = {"api_key": api_key}

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"[NASA] Error fetching data: {e}")
        return []

    opportunities = []

    # Adjust this loop to match the real JSON structure
    for item in data.get("results", []):
        opportunities.append({
            "title": item.get("title", "").strip(),
            "organization": item.get("center", "NASA").strip(),
            "field": item.get("field", "STEM").strip(),
            "description": item.get("description", "").strip(),
            "requirements": item.get("requirements", "").strip(),
            "citizenship": item.get("citizenship", "").strip(),
            "grade_level": item.get("grade_level", "").strip(),
            "location": item.get("location", "").strip(),
            "deadline": item.get("deadline", "").strip(),
            "url": item.get("url", "").strip(),
        })

    print(f"[NASA] Fetched {len(opportunities)} opportunities")
    return opportunities