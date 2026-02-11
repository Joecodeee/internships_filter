"""
Configuration file for the Internship Scraper
Customize these settings to fit your needs
"""

# ============================================
# FILTERING SETTINGS
# ============================================

# Keywords that indicate international students are welcome
INCLUSIVE_CITIZENSHIP_KEYWORDS = [
    "international students welcome",
    "no citizenship required",
    "open to all students",
    "daca",
    "visa sponsorship",
    "eligible regardless of citizenship",
    "international applicants",
    "f-1 students",
    "on optional practical training",
]

# Keywords that block non-US citizens
EXCLUSIVE_CITIZENSHIP_KEYWORDS = [
    "u.s. citizens only",
    "us citizens only",
    "must be a u.s. citizen",
    "must be us citizen",
    "citizenship required",
    "us citizenship required",
]

# Keywords indicating high school eligibility
HIGH_SCHOOL_KEYWORDS = [
    "high school students may apply",
    "open to high school",
    "grades 9-12",
    "secondary school",
    "pre-college",
    "high school students",
    "secondary students",
]

# ============================================
# SCRAPING SETTINGS
# ============================================

# Delay between requests (seconds) - be respectful!
REQUEST_DELAY = 1

# Maximum number of retries for failed requests
MAX_RETRIES = 3

# Request timeout (seconds)
REQUEST_TIMEOUT = 10

# User agent for web requests
USER_AGENT = "InternshipScraper/1.0 (+https://github.com/)"

# ============================================
# OUTPUT SETTINGS
# ============================================

# Output directory for Excel files
OUTPUT_DIRECTORY = "./"

# Excel file names
EXCEL_ALL_OPPORTUNITIES = "internship_opportunities_all.xlsx"
EXCEL_FILTERED_OPPORTUNITIES = "internship_opportunities_filtered.xlsx"

# Columns to include in Excel export
EXCEL_COLUMNS = [
    "title",
    "organization",
    "field",
    "description",
    "requirements",
    "citizenship",
    "grade_level",
    "location",
    "deadline",
    "url",
]

# ============================================
# DATA SOURCE SETTINGS
# ============================================

# Enable/disable specific sources
SOURCES = {
    "github_jobs": True,
    "real_python": True,
    "internships_com": True,
    "sample_api": True,
    "sample_html": True,
    "nasa": False,  # Requires API key
    "usajobs": False,  # Requires API key
    "nih": False,  # Experimental
    "nsf_reu": False,  # Experimental
    "zooniverse": False,  # Experimental
}

# ============================================
# API KEYS (Environment Variables)
# ============================================

# Required environment variables for some sources:
# - NASA_API_KEY (from https://api.nasa.gov/)
# - USAJOBS_EMAIL (your email)
# - USAJOBS_API_KEY (from https://developer.usajobs.gov/)

# Example setup (Linux/Mac):
# export NASA_API_KEY="your_key_here"
# export USAJOBS_EMAIL="your_email@example.com"
# export USAJOBS_API_KEY="your_key_here"
# python scraper_main.py

# ============================================
# LOGGING SETTINGS
# ============================================

# Enable verbose logging
VERBOSE = True

# Log file (optional, leave empty to disable)
LOG_FILE = ""

# ============================================
# ADVANCED SETTINGS
# ============================================

# Maximum opportunities to fetch per source
MAX_PER_SOURCE = None  # None = unlimited

# Deduplication method
DEDUP_BY = ["title", "organization"]  # Tuple of fields to use for deduplication

# Skip filtering (use all opportunities as-is)
SKIP_FILTERING = False

# Minimum description length (characters)
MIN_DESCRIPTION_LENGTH = 10

# ============================================
# CUSTOM FILTERING LOGIC
# ============================================

def custom_filter(opportunity):
    """
    Add your own custom filtering logic here
    Return True to KEEP the opportunity, False to DISCARD it
    
    Example:
        def custom_filter(opportunity):
            # Only keep remote positions
            location = opportunity.get("location", "").lower()
            return "remote" in location
    """
    # By default, keep everything
    return True

# ============================================
# EXAMPLE USAGE IN YOUR CODE
# ============================================

"""
from config import EXCEL_ALL_OPPORTUNITIES, INCLUSIVE_CITIZENSHIP_KEYWORDS, custom_filter

# Use filtered list
if keyword in INCLUSIVE_CITIZENSHIP_KEYWORDS:
    print("International students welcome!")

# Apply custom filter
filtered = [opp for opp in opportunities if custom_filter(opp)]

# Use output settings
df.to_excel(EXCEL_ALL_OPPORTUNITIES)
"""
