import os
import requests
import base64


def fetch_usajobs_opportunities():
    """
    Fetch student / internship roles from USAJobs.
    You need:
      - USAJOBS_EMAIL
      - USAJOBS_API_KEY
    Docs: https://developer.usajobs.gov/
    """
    email = os.getenv("USAJOBS_EMAIL", "")
    api_key = os.getenv("USAJOBS_API_KEY", "")

    if not email or not api_key:
        print("[USAJOBS] Missing USAJOBS_EMAIL or USAJOBS_API_KEY, skipping USAJobs source.")
        return []

    url = "https://data.usajobs.gov/api/search"

    headers = {
        "Host": "data.usajobs.gov",
        "User-Agent": email,
        "Authorization-Key": api_key,
    }

    # Filter for internships / student programs
    params = {
        "Keyword": "internship student pathways",
        "ResultsPerPage": "50",
    }

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"[USAJOBS] Error fetching data: {e}")
        return []

    opportunities = []

    search_result_items = data.get("SearchResult", {}).get("SearchResultItems", [])

    for item in search_result_items:
        pos = item.get("MatchedObjectDescriptor", {})
        title = pos.get("PositionTitle", "")
        org = pos.get("OrganizationName", "")
        desc = pos.get("UserArea", {}).get("Details", {}).get("JobSummary", "")
        reqs = pos.get("QualificationSummary", "")
        locs = pos.get("PositionLocationDisplay", "")
        url_job = pos.get("PositionURI", "")

        # Citizenship info often in "WhoMayApply" or description
        citizenship = pos.get("UserArea", {}).get("Details", {}).get("WhoMayApply", {}).get("Name", "")

        opportunities.append({
            "title": title.strip(),
            "organization": org.strip(),
            "field": "Various",
            "description": desc.strip(),
            "requirements": reqs.strip(),
            "citizenship": citizenship.strip(),
            "grade_level": "Student / Pathways",
            "location": locs.strip(),
            "deadline": pos.get("ApplicationCloseDate", "").strip(),
            "url": url_job.strip(),
        })

    print(f"[USAJOBS] Fetched {len(opportunities)} opportunities")
    return opportunities