import requests
import time
from bs4 import BeautifulSoup


def fetch_linkedin_internships():
    """
    Fetch internship opportunities from LinkedIn.
    Note: LinkedIn has robots.txt restrictions, but we respect them.
    """
    opportunities = []
    
    try:
        print("[LinkedIn] Attempting to fetch internship opportunities...")
        
        # LinkedIn is strict with scraping. This is a placeholder.
        # For production, use LinkedIn's Official API or a service that has permission.
        # For now, we'll skip this with a message
        print("[LinkedIn] Note: Direct scraping not recommended due to ToS.")
        print("[LinkedIn] Consider using LinkedIn API or third-party service.")
        
        return []
        
    except Exception as e:
        print(f"[LinkedIn] Skipped: {e}")
        return []


def fetch_indeed_internships():
    """
    Fetch internship opportunities from Indeed.
    Indeed is more scrape-friendly than LinkedIn.
    """
    opportunities = []
    
    try:
        print("[Indeed] Fetching internship opportunities...")
        
        url = "https://www.indeed.com/jobs"
        
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        params = {
            "q": "internship",
            "l": "United States",
            "sort": "date"
        }
        
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find job cards
        job_cards = soup.find_all("div", class_="job-card-container")
        
        for card in job_cards[:20]:
            try:
                # Get job title
                title_elem = card.find("h2", class_="jobCardTitle")
                if not title_elem:
                    title_elem = card.find("a")
                
                # Get company
                company_elem = card.find("span", class_="companyName")
                
                # Get location
                location_elem = card.find("div", class_="js-recJobLoc")
                
                # Get snippet/description
                snippet_elem = card.find("div", class_="job-snippet")
                
                if title_elem:
                    opportunities.append({
                        "title": title_elem.text.strip(),
                        "organization": company_elem.text.strip() if company_elem else "Company",
                        "field": "Various",
                        "description": snippet_elem.text.strip()[:500] if snippet_elem else "",
                        "requirements": "",
                        "citizenship": "",
                        "grade_level": "College/University",
                        "location": location_elem.get("data-rc-loc", "Various") if location_elem else "Various",
                        "deadline": "Ongoing",
                        "url": "https://www.indeed.com/jobs?q=internship",
                    })
            except Exception as e:
                continue
        
        print(f"[Indeed] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Indeed] Error fetching data: {e}")
        return []


def fetch_internqueen_internships():
    """
    Fetch internship opportunities from Intern Queen.
    Intern Queen specializes in internships and entry-level jobs.
    """
    opportunities = []
    
    try:
        print("[Intern Queen] Fetching internship opportunities...")
        
        url = "https://www.internqueen.com"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find internship listings
        listings = soup.find_all("div", class_="internship-listing")
        
        for listing in listings[:15]:
            try:
                title = listing.find("h3") or listing.find("h2")
                company = listing.find("span", class_="company-name")
                description = listing.find("p", class_="description")
                location = listing.find("span", class_="location")
                
                if title:
                    opportunities.append({
                        "title": title.text.strip(),
                        "organization": company.text.strip() if company else "Company",
                        "field": "Various",
                        "description": description.text.strip()[:500] if description else "",
                        "requirements": "",
                        "citizenship": "",
                        "grade_level": "College/University",
                        "location": location.text.strip() if location else "Various",
                        "deadline": "Check website",
                        "url": url,
                    })
            except Exception as e:
                continue
        
        print(f"[Intern Queen] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Intern Queen] Error fetching data: {e}")
        return []


def fetch_chegg_internships():
    """
    Fetch internship opportunities from Chegg Internships.
    """
    opportunities = []
    
    try:
        print("[Chegg Internships] Fetching opportunities...")
        
        url = "https://www.chegg.com/internships"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find job cards
        job_cards = soup.find_all("div", class_="job-card")
        
        for card in job_cards[:20]:
            try:
                title = card.find("h3") or card.find("a", class_="job-title")
                company = card.find("span", class_="company")
                location = card.find("span", class_="location")
                
                if title:
                    opportunities.append({
                        "title": title.text.strip(),
                        "organization": company.text.strip() if company else "Company",
                        "field": "Various",
                        "description": "",
                        "requirements": "",
                        "citizenship": "",
                        "grade_level": "College/University",
                        "location": location.text.strip() if location else "Various",
                        "deadline": "Ongoing",
                        "url": url,
                    })
            except Exception as e:
                continue
        
        print(f"[Chegg Internships] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Chegg Internships] Error: {e}")
        return []
