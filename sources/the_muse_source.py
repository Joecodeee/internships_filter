import requests
import time


def fetch_the_muse_opportunities():
    """
    Fetch internship opportunities from The Muse API.
    The Muse provides a free API for job listings.
    API Docs: https://www.themuse.com/developers/api/opportunities
    """
    opportunities = []
    base_url = "https://www.themuse.com/api/public/jobs"
    
    try:
        print("[The Muse] Fetching internship opportunities...")
        
        # Search for internships
        params = {
            "category": "Internship",
            "page": 0,
            "api_key": ""  # The Muse API doesn't require authentication for basic queries
        }
        
        # Fetch first 2 pages with rate limiting
        for page in range(0, 2):
            params["page"] = page
            
            response = requests.get(base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            results = data.get("results", [])
            if not results:
                break
            
            for job in results:
                # Parse location
                locations = job.get("locations", [])
                location = locations[0].get("name", "Remote") if locations else "Remote"
                
                opportunities.append({
                    "title": job.get("name", "").strip(),
                    "organization": job.get("company", {}).get("name", "").strip(),
                    "field": "Various",
                    "description": job.get("short_description", "").strip()[:500],
                    "requirements": job.get("contents", "").strip()[:300],
                    "citizenship": "Check company policy",
                    "grade_level": "College/University",
                    "location": location,
                    "deadline": "Ongoing",
                    "url": job.get("refs", {}).get("landing_page", "").strip(),
                    "job_level": job.get("level_id", ""),
                })
            
            time.sleep(1)  # Rate limiting
        
        print(f"[The Muse] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[The Muse] Error fetching data: {e}")
        return []


def fetch_muse_by_level():
    """
    Fetch entry-level opportunities from The Muse (high school/early college).
    """
    opportunities = []
    base_url = "https://www.themuse.com/api/public/jobs"
    
    try:
        print("[The Muse - Entry Level] Fetching opportunities...")
        
        params = {
            "level": "entry-level",
            "page": 0,
        }
        
        for page in range(0, 2):
            params["page"] = page
            
            response = requests.get(base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            results = data.get("results", [])
            if not results:
                break
            
            for job in results:
                locations = job.get("locations", [])
                location = locations[0].get("name", "Remote") if locations else "Remote"
                
                opportunities.append({
                    "title": job.get("name", "").strip(),
                    "organization": job.get("company", {}).get("name", "").strip(),
                    "field": "Various",
                    "description": job.get("short_description", "").strip()[:500],
                    "requirements": job.get("contents", "").strip()[:300],
                    "citizenship": "Check company policy",
                    "grade_level": "Entry-level/College",
                    "location": location,
                    "deadline": "Ongoing",
                    "url": job.get("refs", {}).get("landing_page", "").strip(),
                })
            
            time.sleep(1)
        
        print(f"[The Muse - Entry Level] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[The Muse - Entry Level] Error: {e}")
        return []
