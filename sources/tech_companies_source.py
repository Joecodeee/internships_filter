import requests
import time
from bs4 import BeautifulSoup


def fetch_summer_programs():
    """
    Fetch summer internship and research programs.
    Sources might include summer.com or generic searches.
    """
    opportunities = []
    
    try:
        print("[Summer Programs] Fetching summer internship opportunities...")
        
        url = "https://www.summer.com/internships"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find program listings
        listings = soup.find_all("div", class_="program-card")
        
        for listing in listings[:20]:
            try:
                title = listing.find("h3") or listing.find("h2")
                org = listing.find("span", class_="organization")
                desc = listing.find("p", class_="description")
                duration = listing.find("span", class_="duration")
                deadline = listing.find("span", class_="deadline")
                
                if title:
                    opportunities.append({
                        "title": title.text.strip(),
                        "organization": org.text.strip() if org else "Organization",
                        "field": "Various",
                        "description": desc.text.strip()[:500] if desc else "",
                        "requirements": "",
                        "citizenship": "Check individual program",
                        "grade_level": "High School/College",
                        "location": "Various",
                        "deadline": deadline.text.strip() if deadline else "Check website",
                        "url": url,
                        "program_type": "Summer Program",
                    })
            except Exception as e:
                continue
        
        print(f"[Summer Programs] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Summer Programs] Error: {e}")
        return []


def fetch_google_careers_internships():
    """
    Fetch Google internship opportunities from their careers site.
    """
    opportunities = []
    
    try:
        print("[Google Careers] Fetching internship opportunities...")
        
        # Google.com/careers internships page
        url = "https://www.google.com/careers/students/internships"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find internship listings
        internships = soup.find_all("div", class_="internship-card")
        
        for internship in internships[:10]:
            try:
                title = internship.find("h3") or internship.find("a")
                desc = internship.find("p")
                
                if title:
                    opportunities.append({
                        "title": title.text.strip(),
                        "organization": "Google",
                        "field": "Technology/Software",
                        "description": desc.text.strip()[:500] if desc else "",
                        "requirements": "Check website",
                        "citizenship": "Check eligibility",
                        "grade_level": "College/University",
                        "location": "Various",
                        "deadline": "Check website",
                        "url": url,
                    })
            except Exception as e:
                continue
        
        print(f"[Google Careers] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Google Careers] Error: {e}")
        return []


def fetch_microsoft_internships():
    """
    Fetch Microsoft internship opportunities from their careers site.
    """
    opportunities = []
    
    try:
        print("[Microsoft Careers] Fetching internship opportunities...")
        
        url = "https://careers.microsoft.com/students/internships"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find job listings
        listings = soup.find_all("div", class_="job-card")
        
        for listing in listings[:10]:
            try:
                title = listing.find("h3") or listing.find("a", class_="job-title")
                desc = listing.find("p")
                location = listing.find("span", class_="location")
                
                if title:
                    opportunities.append({
                        "title": title.text.strip(),
                        "organization": "Microsoft",
                        "field": "Technology/Software",
                        "description": desc.text.strip()[:500] if desc else "",
                        "requirements": "",
                        "citizenship": "Check eligibility",
                        "grade_level": "College/University",
                        "location": location.text.strip() if location else "Various",
                        "deadline": "Check website",
                        "url": url,
                    })
            except Exception as e:
                continue
        
        print(f"[Microsoft Careers] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Microsoft Careers] Error: {e}")
        return []


def fetch_amazon_internships():
    """
    Fetch Amazon internship opportunities from their careers site.
    """
    opportunities = []
    
    try:
        print("[Amazon Careers] Fetching internship opportunities...")
        
        url = "https://www.amazon.jobs/en/jobs/internship"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find job listings
        listings = soup.find_all("div", class_="job-card-container")
        
        for listing in listings[:10]:
            try:
                title = listing.find("h3") or listing.find("a")
                location = listing.find("span", class_="location")
                
                if title:
                    opportunities.append({
                        "title": title.text.strip(),
                        "organization": "Amazon",
                        "field": "Technology/Software",
                        "description": "Software internship at Amazon",
                        "requirements": "",
                        "citizenship": "Check eligibility",
                        "grade_level": "College/University",
                        "location": location.text.strip() if location else "Various",
                        "deadline": "Ongoing",
                        "url": url,
                    })
            except Exception as e:
                continue
        
        print(f"[Amazon Careers] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Amazon Careers] Error: {e}")
        return []
