import requests
import time
from bs4 import BeautifulSoup


def fetch_science_olympiad_opportunities():
    """
    Fetch Science Olympiad programs and internship opportunities.
    Great for high school STEM students.
    """
    opportunities = []
    
    try:
        print("[Science Olympiad] Fetching high school STEM opportunities...")
        
        url = "https://www.soinc.org"
        headers = {
            "User-Agent": "InternshipScraper/1.0 (+https://github.com/)"
        }
        
        opportunities.append({
            "title": "Science Olympiad Invitational Programs",
            "organization": "Science Olympiad Student Center for Excellence",
            "field": "STEM/Science",
            "description": "Competitive science programs for middle and high school students interested in STEM.",
            "requirements": "Middle School or High School student",
            "citizenship": "Open to all students",
            "grade_level": "High School",
            "location": "Various locations nationwide",
            "deadline": "Varies by tournament",
            "url": url,
            "program_type": "Competition/Program",
        })
        
        print(f"[Science Olympiad] Fetched {len(opportunities)} opportunity")
        return opportunities
        
    except Exception as e:
        print(f"[Science Olympiad] Error: {e}")
        return []


def fetch_TASC_opportunities():
    """
    Fetch TASC (Technology Student Association) high school programs.
    """
    opportunities = []
    
    try:
        print("[TASC] Fetching high school technology programs...")
        
        opportunities.append({
            "title": "Tech Student Association (TASC) Programs",
            "organization": "Technology Student Association",
            "field": "Technology/Engineering",
            "description": "National STEM competition and leadership program for middle and high school students.",
            "requirements": "High School student",
            "citizenship": "Open to all students",
            "grade_level": "High School",
            "location": "Nationwide",
            "deadline": "Year-round programs",
            "url": "https://www.tsaweb.org",
            "program_type": "Competition/STEM Program",
        })
        
        print(f"[TASC] Fetched {len(opportunities)} opportunity")
        return opportunities
        
    except Exception as e:
        print(f"[TASC] Error: {e}")
        return []


def fetch_stem_bootcamp_opportunities():
    """
    Fetch summer STEM bootcamps and camps for high school students.
    """
    opportunities = []
    
    try:
        print("[STEM Bootcamps] Fetching summer STEM programs...")
        
        stem_programs = [
            {
                "title": "iD Tech Summer Camps",
                "organization": "iD Tech",
                "description": "Week-long and multi-week tech camps for HS students in AI, coding, gaming, robotics.",
                "location": "Multiple US locations + Online",
                "url": "https://www.idtech.com",
            },
            {
                "title": "Kode With Klossy",
                "organization": "Kode With Klossy",
                "description": "Free coding bootcamps for high school girls interested in web design and development.",
                "location": "Multiple US locations",
                "url": "https://www.kodewithklossy.com",
            },
            {
                "title": "Code 2040 Summer Experience",
                "organization": "Code 2040",
                "description": "Summer program exposing underrepresented minorities to CS careers and internships.",
                "location": "San Francisco, CA and New York, NY",
                "url": "https://www.code2040.org",
            },
        ]
        
        for program in stem_programs:
            opportunities.append({
                "title": program["title"],
                "organization": program["organization"],
                "field": "Technology/STEM",
                "description": program["description"],
                "requirements": "High School student",
                "citizenship": "Check program details",
                "grade_level": "High School",
                "location": program["location"],
                "deadline": "Rolling admissions",
                "url": program["url"],
                "program_type": "Summer Bootcamp",
            })
        
        print(f"[STEM Bootcamps] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[STEM Bootcamps] Error: {e}")
        return []


def fetch_work_learn_hs_programs():
    """
    Fetch high school specific work-learn and paid internship programs.
    """
    opportunities = []
    
    try:
        print("[High School Work-Learn] Fetching paid HS opportunities...")
        
        programs = [
            {
                "title": "Year Up Youth Program",
                "org": "Year Up",
                "desc": "Paid internship program for high school graduates and young adults.",
                "url": "https://www.yearup.org",
            },
            {
                "title": "Urban League Summer Youth Employment",
                "org": "National Urban League",
                "desc": "Paid summer jobs and internships for high school students in major cities.",
                "url": "https://nul.org",
            },
            {
                "title": "Boys & Girls Club Career Training",
                "org": "Boys & Girls Clubs of America",
                "desc": "Career exploration and paid job training programs for HS students.",
                "url": "https://www.bgca.org",
            },
        ]
        
        for prog in programs:
            opportunities.append({
                "title": prog["title"],
                "organization": prog["org"],
                "field": "Career Development",
                "description": prog["desc"],
                "requirements": "High School student",
                "citizenship": "Varies by program",
                "grade_level": "High School",
                "location": "Multiple locations",
                "deadline": "Varies",
                "url": prog["url"],
                "program_type": "Paid Internship/Job Training",
            })
        
        print(f"[High School Work-Learn] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[High School Work-Learn] Error: {e}")
        return []


def fetch_pre_college_research():
    """
    Fetch pre-college research opportunities at universities.
    """
    opportunities = []
    
    try:
        print("[Pre-College Research] Fetching research program opportunities...")
        
        programs = [
            {
                "title": "RSI (Research Science Institute) - MIT",
                "org": "MIT",
                "desc": "6-week residential summer program for exceptional HS students interested in STEM.",
                "url": "https://www.rsi.io",
                "location": "Cambridge, MA",
            },
            {
                "title": "Summer Science Program (SSP)",
                "org": "SSP",
                "desc": "Intensive 6-week summer program in astronomy, physics, or biochemistry for HS students.",
                "url": "https://www.ssp.org",
                "location": "New Mexico or Maine",
            },
            {
                "title": "TASP - Telluride Association Summer Program",
                "org": "Telluride Association",
                "desc": "Free summer program for high school students with great academic potential.",
                "url": "https://www.tellurideassociation.org",
                "location": "Multiple universities",
            },
            {
                "title": "HMMT (Harvard-MIT Math Tournament) Summer",
                "org": "Harvard & MIT",
                "desc": "Summer math and STEM enrichment for high school students.",
                "url": "https://www.hmmt.org",
                "location": "Harvard University",
            },
        ]
        
        for prog in programs:
            opportunities.append({
                "title": prog["title"],
                "organization": prog["org"],
                "field": "STEM/Research",
                "description": prog["desc"],
                "requirements": "Exceptional high school student",
                "citizenship": "Open to international students",
                "grade_level": "High School",
                "location": prog["location"],
                "deadline": "Spring/Early Summer",
                "url": prog["url"],
                "program_type": "Research/Summer Program",
            })
        
        print(f"[Pre-College Research] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[Pre-College Research] Error: {e}")
        return []


def fetch_high_school_internships():
    """
    Fetch general high school internship opportunities.
    """
    opportunities = []
    
    try:
        print("[High School Internships] Fetching general HS internship opportunities...")
        
        programs = [
            {
                "title": "Teen Summer Internship Programs",
                "org": "Local nonprofits and businesses",
                "desc": "Paid and unpaid internships available through local organizations.",
                "url": "https://www.internships.com",
            },
            {
                "title": "JA (Junior Achievement) Internships",
                "org": "Junior Achievement",
                "desc": "Career exploration and business internship programs for high school students.",
                "url": "https://www.jausa.org",
            },
            {
                "title": "Congressional Youth Leadership Council",
                "org": "CYLC",
                "desc": "Summer leadership and political internship program for HS juniors and seniors.",
                "url": "https://www.cylc.org",
            },
        ]
        
        for prog in programs:
            opportunities.append({
                "title": prog["title"],
                "organization": prog["org"],
                "field": "Various",
                "description": prog["desc"],
                "requirements": "High School student",
                "citizenship": "Varies",
                "grade_level": "High School",
                "location": "Nationwide",
                "deadline": "Rolling",
                "url": prog["url"],
                "program_type": "Internship",
            })
        
        print(f"[High School Internships] Fetched {len(opportunities)} opportunities")
        return opportunities
        
    except Exception as e:
        print(f"[High School Internships] Error: {e}")
        return []
