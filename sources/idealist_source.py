import requests
import time


def fetch_idealist_org_opportunities():
    """
    Fetch non-profit internship opportunities from Idealist.org.
    Idealist specializes in non-profit, social sector jobs and internships.
    """
    opportunities = []
    
    try:
        print("[Idealist.org] Fetching non-profit internship opportunities...")
        
        # Idealist.org API endpoint for internships
        url = "https://api.idealist.org/v2/positions"
        
        # Free tier parameters (adjust as needed)
        params = {
            "internshipOnly": True,
            "page": 0,
            "pageSize": 25
        }
        
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        for page in range(0, 2):  # Fetch 2 pages
            params["page"] = page
            
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            positions = data.get("positions", [])
            if not positions:
                break
            
            for position in positions:
                opportunities.append({
                    "title": position.get("title", "").strip(),
                    "organization": position.get("organization", {}).get("name", "Non-profit").strip(),
                    "field": "Non-profit/Social Sector",
                    "description": position.get("description", "").strip()[:500],
                    "requirements": position.get("requirements", "").strip()[:300],
                    "citizenship": "Varies by organization",
                    "grade_level": "College/University",
                    "location": position.get("location", {}).get("locationName", "Various").strip(),
                    "deadline": position.get("closingDate", "Ongoing").strip(),
                    "url": position.get("url", "").strip(),
                    "organization_type": "Non-Profit",
                })
            
            time.sleep(1)  # Rate limiting
        
        print(f"[Idealist.org] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Idealist.org] Error fetching data: {e}")
        return []


def fetch_idealist_nonprofit_internships():
    """
    Alternative scraping method for Idealist.org internships.
    """
    opportunities = []
    
    try:
        from bs4 import BeautifulSoup
        
        print("[Idealist.org - HTML] Fetching internship listings...")
        
        url = "https://www.idealist.org/en/internship"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find job listings
        listings = soup.find_all("div", class_="posting")
        
        for listing in listings[:15]:
            try:
                title = listing.find("h2") or listing.find("a", class_="posting-title")
                org = listing.find("span", class_="organization-name")
                desc = listing.find("p", class_="posting-description")
                
                if title:
                    opportunities.append({
                        "title": title.text.strip(),
                        "organization": org.text.strip() if org else "Non-profit",
                        "field": "Non-profit/Social Sector",
                        "description": desc.text.strip()[:500] if desc else "",
                        "requirements": "",
                        "citizenship": "",
                        "grade_level": "College/University",
                        "location": "Various",
                        "deadline": "Check website",
                        "url": url,
                        "organization_type": "Non-Profit",
                    })
            except Exception as e:
                continue
        
        print(f"[Idealist.org - HTML] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Idealist.org - HTML] Error: {e}")
        return []
