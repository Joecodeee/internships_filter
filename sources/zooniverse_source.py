import requests


def fetch_zooniverse_opportunities():
    """
    Fetch citizen science projects from Zooniverse.
    These are generally open to all, remote, and great for HS students.
    Docs: https://www.zooniverse.org/api
    """
    url = "https://www.zooniverse.org/api/projects"

    params = {
        "page_size": 50,
        "launch_approved": "true",
        "state": "live",
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"[Zooniverse] Error fetching data: {e}")
        return []

    opportunities = []

    for item in data.get("projects", []):
        title = item.get("display_name", "")
        org = "Zooniverse Project"
        desc = item.get("description", "") or item.get("introduction", "")
        url_proj = "https://www.zooniverse.org/projects/" + item.get("slug", "")

        # Zooniverse is generally open to all, remote, and citizenship-neutral
        citizenship = "Open to all students; no citizenship required (citizen science)."
        requirements = "Internet access; suitable for high school students."
        grade_level = "High school / all ages"
        location = "Remote"
        deadline = "Ongoing"

        opportunities.append({
            "title": title.strip(),
            "organization": org,
            "field": "Various / Citizen Science",
            "description": desc.strip(),
            "requirements": requirements,
            "citizenship": citizenship,
            "grade_level": grade_level,
            "location": location,
            "deadline": deadline,
            "url": url_proj,
        })

    print(f"[Zooniverse] Fetched {len(opportunities)} opportunities")
    return opportunities