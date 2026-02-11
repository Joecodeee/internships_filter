import requests
import time
from bs4 import BeautifulSoup


def fetch_handshake_internships():
    """
    Fetch internships from Handshake - a college-focused internship platform.
    Note: Handshake requires authentication for full API access.
    This attempts HTML scraping of public listings.
    """
    opportunities = []
    
    try:
        print("[Handshake] Fetching college internship opportunities...")
        
        url = "https://joinhandshake.com"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        # Note: Direct scraping of Handshake may be limited due to JavaScript rendering
        # Consider using their official API if you have institutional access
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find opportunities (CSS selectors may vary)
        listings = soup.find_all("div", class_="opportunity")
        
        for listing in listings[:20]:
            try:
                title = listing.find("h3") or listing.find("a", class_="title")
                company = listing.find("span", class_="company")
                desc = listing.find("p", class_="description")
                
                if title:
                    opportunities.append({
                        "title": title.text.strip(),
                        "organization": company.text.strip() if company else "Company",
                        "field": "Various",
                        "description": desc.text.strip()[:500] if desc else "",
                        "requirements": "",
                        "citizenship": "Check posting",
                        "grade_level": "College/University",
                        "location": "Various",
                        "deadline": "Check website",
                        "url": url,
                        "platform": "Handshake",
                    })
            except Exception as e:
                continue
        
        print(f"[Handshake] Fetched {len(opportunities)} opportunities (Note: May be limited)")
        return opportunities
        
    except Exception as e:
        print(f"[Handshake] Error: {e}")
        return []


def fetch_vault_internships():
    """
    Fetch internship opportunities from Vault.
    Vault specializes in internships and early career roles.
    """
    opportunities = []
    
    try:
        print("[Vault] Fetching internship opportunities...")
        
        url = "https://www.vault.com/internships"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find internship listings
        listings = soup.find_all("div", class_="job-result")
        
        for listing in listings[:20]:
            try:
                title = listing.find("h2") or listing.find("a", class_="jobLink")
                company = listing.find("span", class_="company")
                location = listing.find("span", class_="location")
                
                if title:
                    opportunities.append({
                        "title": title.text.strip(),
                        "organization": company.text.strip() if company else "Company",
                        "field": "Finance/Consulting/Various",
                        "description": "",
                        "requirements": "",
                        "citizenship": "",
                        "grade_level": "College/University",
                        "location": location.text.strip() if location else "Various",
                        "deadline": "Check website",
                        "url": url,
                    })
            except Exception as e:
                continue
        
        print(f"[Vault] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Vault] Error: {e}")
        return []


def fetch_finance_internships():
    """
    Fetch finance and consulting internships.
    """
    opportunities = []
    
    try:
        print("[Finance Internships] Fetching financial services internships...")
        
        url = "https://www.vault.com/internships/vault-the-vault"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find financial services companies and their internships
        company_listings = soup.find_all("div", class_="company-result")
        
        for company in company_listings[:15]:
            try:
                name = company.find("h3") or company.find("a", class_="company-name")
                profile = company.find("p", class_="profile")
                
                if name:
                    opportunities.append({
                        "title": f"{name.text.strip()} - Financial Internship",
                        "organization": name.text.strip(),
                        "field": "Finance/Banking/Consulting",
                        "description": profile.text.strip()[:500] if profile else "Finance sector internship opportunity",
                        "requirements": "",
                        "citizenship": "Check requirements",
                        "grade_level": "College/University",
                        "location": "NYC/London/Various",
                        "deadline": "Year-round recruiting",
                        "url": url,
                    })
            except Exception as e:
                continue
        
        print(f"[Finance Internships] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Finance Internships] Error: {e}")
        return []


def fetch_acm_internship_board():
    """
    Fetch internships from ACM (Association for Computing Machinery) resources.
    """
    opportunities = []
    
    try:
        print("[ACM Internships] Fetching engineering/CS internships...")
        
        # ACM Career Resources
        url = "https://www.acm.org/careers"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find job postings
        postings = soup.find_all("div", class_="job-posting")
        
        for posting in postings[:15]:
            try:
                title = posting.find("h3") or posting.find("a")
                company = posting.find("span", class_="company")
                desc = posting.find("p", class_="description")
                
                if title:
                    opportunities.append({
                        "title": title.text.strip(),
                        "organization": company.text.strip() if company else "Tech Company",
                        "field": "Computer Science/Engineering",
                        "description": desc.text.strip()[:500] if desc else "",
                        "requirements": "CS/Engineering background preferred",
                        "citizenship": "",
                        "grade_level": "College/University",
                        "location": "Various",
                        "deadline": "Check website",
                        "url": url,
                    })
            except Exception as e:
                continue
        
        print(f"[ACM Internships] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[ACM Internships] Error: {e}")
        return []
