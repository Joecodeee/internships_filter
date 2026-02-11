"""
Pre-College Configuration
Customized settings for high school internship scraper
"""

# ============================================
# PRE-COLLEGE FILTERING SETTINGS
# ============================================

# High school specific eligibility keywords
HIGH_SCHOOL_KEYWORDS = [
    "high school students",
    "high school may apply",
    "freshman",
    "sophomore",
    "junior",
    "senior",
    "grades 9-12",
    "secondary school",
    "pre-college",
    "teen",
    "youth",
    "under 18",
    "14-18",
    "15-18",
    "16-18",
]

# Keywords indicating programs designed for young people
YOUTH_PROGRAM_KEYWORDS = [
    "youth program",
    "student program",
    "summer camp",
    "bootcamp",
    "young people",
    "young adults",
    "first generation",
    "underserved",
    "underrepresented",
]

# Keywords indicating international/no citizenship barriers
INTERNATIONAL_FRIENDLY_KEYWORDS = [
    "international students welcome",
    "no citizenship required",
    "open to all",
    "international applicants",
    "f-1 students",
    "visa sponsorship",
]

# Block keywords - exclude opportunities clearly for college+ only
COLLEGE_ONLY_KEYWORDS = [
    "college degree required",
    "must be enrolled in college",
    "graduates only",
    "bachelor's degree",
    "phd",
    "master's degree",
    "professional experience required",
    "3 years experience",
    "5 years experience",
]

# ============================================
# PRE-COLLEGE SPECIFIC SETTINGS
# ============================================

# Focus on these program types for high school
PREFERRED_PROGRAM_TYPES = [
    "Summer Program",
    "STEM Camp",
    "Research Program",
    "Internship",
    "Competition",
    "Bootcamp",
    "Job Training",
    "Paid Internship",
    "Work-Learn Program",
]

# ============================================
# GEOGRAPHIC PREFERENCES (Optional)
# ============================================

# Locations with many HS programs
POPULAR_LOCATIONS = [
    "Remote",
    "Online",
    "Nationwide",
    "California",
    "New York",
    "Massachusetts",
    "Illinois",
    "Texas",
]

# ============================================
# OUTPUT SETTINGS
# ============================================

OUTPUT_DIRECTORY = "./"

# Excel file names for pre-college
EXCEL_HS_PROGRAMS = "high_school_internship_programs.xlsx"
EXCEL_FILTERED_PROGRAMS = "high_school_verified_programs.xlsx"

# Columns to display for pre-college students
EXCEL_COLUMNS = [
    "title",
    "organization",
    "field",
    "grade_level",
    "program_type",
    "description",
    "location",
    "deadline",
    "citizenship",
    "url",
]

# ============================================
# DATA SOURCE SETTINGS FOR PRE-COLLEGE
# ============================================

# Enable/disable sources (high school focused)
PRECOLLEGGE_SOURCES = {
    "high_school_source": True,  # NEW HS-specific source
    "stem_bootcamps": True,
    "the_muse": True,           # Has entry-level
    "sample_api": True,
    "sample_html": True,
    # Disable college-only sources
    "github_jobs": False,
    "real_python": False,
    "builtin": False,
    "tech_companies": False,
    "college_finance": False,
}

# ============================================
# FILTERING LOGIC
# ============================================

def is_high_school_appropriate(text: str) -> bool:
    """Return True if opportunity is appropriate for high school students."""
    if not text:
        return False
    
    text = text.lower()
    
    # Check for college-only requirements
    for bad in COLLEGE_ONLY_KEYWORDS:
        if bad in text:
            return False
    
    # Check for high school indicators
    for good in HIGH_SCHOOL_KEYWORDS + YOUTH_PROGRAM_KEYWORDS:
        if good in text:
            return True
    
    # Check for explicitly youth-focused
    if any(k in text for k in ["young people", "youth", "teen", "student"]):
        return True
    
    return False


def is_international_friendly(text: str) -> bool:
    """Return True if opportunity welcomes international/diverse students."""
    if not text:
        return False
    
    text = text.lower()
    return any(k in text for k in INTERNATIONAL_FRIENDLY_KEYWORDS)


def custom_filter(opportunity):
    """
    Apply pre-college specific filtering.
    Return True to KEEP the opportunity, False to DISCARD it.
    """
    # Ensure it's for high school students
    desc = opportunity.get("description", "") + " " + opportunity.get("requirements", "")
    
    if not is_high_school_appropriate(desc):
        # Only keep if explicitly labeled as high school
        grade_level = opportunity.get("grade_level", "").lower()
        if "high school" not in grade_level:
            return False
    
    return True


# ============================================
# ADVANCED SETTINGS
# ============================================

# Maximum opportunities to fetch per source
MAX_PER_SOURCE = 50

# Deduplication method
DEDUP_BY = ["title", "organization"]

# Skip filtering to see all opportunities
SKIP_FILTERING = False

# Minimum description length (characters)
MIN_DESCRIPTION_LENGTH = 10

# ============================================
# PRIORITY RANKING
# ============================================

# Boost priority for these fields
HIGH_VALUE_KEYWORDS = {
    "paid": 10,
    "stipend": 10,
    "free": 8,
    "remote": 5,
    "online": 5,
    "stem": 8,
    "leadership": 6,
    "international": 6,
}

# ============================================
# DISPLAY SETTINGS
# ============================================

# Show more details for pre-college students
VERBOSE_DESCRIPTIONS = True

# Include application tips for each opportunity
INCLUDE_TIPS = True

# ============================================
# EXAMPLE USAGE
# ============================================

"""
from precollegge_config import is_high_school_appropriate, custom_filter

# Use in your scraper:
if is_high_school_appropriate(opportunity["description"]):
    # Good for high school students
    pass

# Apply custom filter
filtered = [opp for opp in opportunities if custom_filter(opp)]
"""
