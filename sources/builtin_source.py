import requests
import time
from bs4 import BeautifulSoup


def fetch_builtin_opportunities():
    """
    Fetch tech internships from Built In.
    Built In is a platform for tech jobs and internships.
    """
    opportunities = []
    
    try:
        from bs4 import BeautifulSoup
        
        print("[Built In] Fetching tech internship opportunities...")
        
        # Try to fetch from Built In (they have internship listings)
        url = "https://builtin.com/internships"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find job cards - adjust selectors based on actual site structure
        job_cards = soup.find_all("div", class_="job-card")
        
        for card in job_cards[:20]:  # Limit to first 20
            try:
                title_elem = card.find("h3")
                company_elem = card.find("span", class_="company")
                desc_elem = card.find("p", class_="description")
                location_elem = card.find("span", class_="location")
                
                if title_elem:
                    opportunities.append({
                        "title": title_elem.text.strip(),
                        "organization": company_elem.text.strip() if company_elem else "Tech Company",
                        "field": "Technology/Software",
                        "description": desc_elem.text.strip()[:500] if desc_elem else "",
                        "requirements": "",
                        "citizenship": "",
                        "grade_level": "College/University",
                        "location": location_elem.text.strip() if location_elem else "Various",
                        "deadline": "Check website",
                        "url": url,
                    })
            except Exception as e:
                continue
        
        print(f"[Built In] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Built In] Error fetching data: {e}")
        return []


def fetch_builtin_startups():
    """
    Fetch internships from startup companies on Built In.
    """
    opportunities = []
    
    try:
        print("[Built In - Startups] Fetching startup internship opportunities...")
        
        url = "https://builtin.com/startups/internships"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        job_cards = soup.find_all("div", class_="job-card")
        
        for card in job_cards[:15]:
            try:
                title_elem = card.find("h3")
                company_elem = card.find("span", class_="company")
                
                if title_elem:
                    opportunities.append({
                        "title": title_elem.text.strip(),
                        "organization": company_elem.text.strip() if company_elem else "Startup",
                        "field": "Startup/Technology",
                        "description": "",
                        "requirements": "",
                        "citizenship": "",
                        "grade_level": "College/University", 
                        "location": "Various",
                        "deadline": "Check website",
                        "url": url,
                    })
            except Exception as e:
                continue
        
        print(f"[Built In - Startups] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Built In - Startups] Error: {e}")
        return []
