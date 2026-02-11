import requests
import time
from typing import List, Dict

def fetch_github_jobs():
    """
    Fetch internship opportunities from GitHub Jobs API (public).
    This doesn't require authentication.
    """
    opportunities = []
    base_url = "https://jobs.github.com/positions.json"
    
    try:
        # Search for internship positions
        params = {
            "description": "internship",
            "page": 1
        }
        
        print("[GitHub Jobs] Fetching internship opportunities...")
        
        # GitHub Jobs API returns max 50 per page
        for page in range(1, 3):  # Fetch first 2 pages with rate limiting
            params["page"] = page
            
            response = requests.get(base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if not data:
                break
            
            for job in data:
                opportunities.append({
                    "title": job.get("title", "").strip(),
                    "organization": job.get("company", "").strip(),
                    "field": "Technology/Software",
                    "description": job.get("description", "").strip()[:500],  # Truncate long descriptions
                    "requirements": "",
                    "citizenship": "Check company policy",
                    "grade_level": "College/University",
                    "location": job.get("location", "").strip(),
                    "deadline": "Ongoing",
                    "url": job.get("url", "").strip(),
                    "job_type": job.get("type", "").strip(),
                    "created_at": job.get("created_at", "").strip(),
                })
            
            time.sleep(1)  # Rate limiting
        
        print(f"[GitHub Jobs] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[GitHub Jobs] Error fetching data: {e}")
        return []


def fetch_real_python_jobs():
    """
    Fetch internships from Real Python jobs board (HTML scraping).
    """
    opportunities = []
    url = "https://realpython.com/jobs/"
    
    try:
        from bs4 import BeautifulSoup
        
        print("[Real Python] Fetching job opportunities...")
        
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find job listings (adjust selectors based on actual HTML structure)
        job_cards = soup.find_all("div", class_="card")
        
        for card in job_cards[:10]:  # Limit to first 10
            try:
                title_elem = card.find("h3")
                org_elem = card.find("a", class_="card-link")
                desc_elem = card.find("p")
                
                if title_elem and org_elem:
                    opportunities.append({
                        "title": title_elem.text.strip(),
                        "organization": org_elem.text.strip(),
                        "field": "Programming/Technology",
                        "description": desc_elem.text.strip() if desc_elem else "",
                        "requirements": "",
                        "citizenship": "",
                        "grade_level": "College/University",
                        "location": "Various",
                        "deadline": "Ongoing",
                        "url": org_elem.get("href", "").strip(),
                    })
            except Exception as e:
                continue
        
        print(f"[Real Python] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Real Python] Error fetching data: {e}")
        return []


def fetch_internship_com():
    """
    Fetch internships from internships.com using web scraping.
    """
    opportunities = []
    
    try:
        from bs4 import BeautifulSoup
        
        print("[Internships.com] Fetching internship opportunities...")
        
        url = "https://www.internships.com/"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Note: This might need selector adjustments based on actual website structure
        # The website may have dynamic content, so results might be limited
        job_listings = soup.find_all("div", class_="listing")
        
        for listing in job_listings[:15]:
            try:
                title = listing.find("h2") or listing.find("a")
                org = listing.find("span", class_="company")
                desc = listing.find("p")
                
                if title:
                    opportunities.append({
                        "title": title.text.strip(),
                        "organization": org.text.strip() if org else "Unknown",
                        "field": "Various",
                        "description": desc.text.strip() if desc else "",
                        "requirements": "",
                        "citizenship": "",
                        "grade_level": "College/University",
                        "location": "Various",
                        "deadline": "Check website",
                        "url": url,
                    })
            except Exception as e:
                continue
        
        print(f"[Internships.com] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Internships.com] Error fetching data: {e}")
        return []
