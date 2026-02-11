# Internship Scraper - Sources Documentation

Complete list of all internship opportunity sources integrated into the scraper.

## Source Categories

### 1. Job Board Aggregators

#### GitHub Jobs API
- **File**: `sources/github_jobs_source.py`
- **Status**: ✅ Working
- **Authentication**: No
- **Data Coverage**: Tech/Software internships
- **Function**: `fetch_github_jobs()`
- **Notes**: Uses GitHub's official public API, no authentication required

#### Real Python Jobs
- **File**: `sources/github_jobs_source.py`
- **Status**: ✅ Working
- **Authentication**: No
- **Data Coverage**: Python/Tech internships
- **Function**: `fetch_real_python_jobs()`
- **Notes**: HTML scraping, respects robots.txt

#### Internships.com
- **File**: `sources/github_jobs_source.py`
- **Status**: ⚠️ Limited (HTML scraping)
- **Authentication**: No
- **Data Coverage**: General internships
- **Function**: `fetch_internship_com()`
- **Notes**: May have limited results due to dynamic content

#### Indeed Internships
- **File**: `sources/jobboards_source.py`
- **Status**: ✅ Working
- **Authentication**: No
- **Data Coverage**: All fields
- **Function**: `fetch_indeed_internships()`
- **Notes**: Major job board with comprehensive internship listings

#### Intern Queen
- **File**: `sources/jobboards_source.py`
- **Status**: ✅ Working
- **Authentication**: No
- **Data Coverage**: Internships & entry-level
- **Function**: `fetch_internqueen_internships()`
- **Notes**: Specializes in student internships

#### Chegg Internships
- **File**: `sources/jobboards_source.py`
- **Status**: ✅ Working
- **Authentication**: No
- **Data Coverage**: All fields
- **Function**: `fetch_chegg_internships()`
- **Notes**: Student-focused platform

#### Vault Internships
- **File**: `sources/college_finance_source.py`
- **Status**: ✅ Working
- **Authentication**: No
- **Data Coverage**: Finance/Consulting/Various
- **Function**: `fetch_vault_internships()`
- **Notes**: Strong in finance and professional services

#### The Muse
- **File**: `sources/the_muse_source.py`
- **Status**: ✅ API Available
- **Authentication**: No (for basic queries)
- **Data Coverage**: All fields
- **Functions**: 
  - `fetch_the_muse_opportunities()`
  - `fetch_muse_by_level()` (entry-level focused)
- **Notes**: Has free API, popular with startups

### 2. Tech-Specific Sources

#### Built In Tech
- **File**: `sources/builtin_source.py`
- **Status**: ✅ Working
- **Authentication**: No
- **Data Coverage**: Tech/Software internships
- **Functions**:
  - `fetch_builtin_opportunities()`
  - `fetch_builtin_startups()` (startup internships)
- **Notes**: Specialized in tech companies

#### Google Careers
- **File**: `sources/tech_companies_source.py`
- **Status**: ✅ Working
- **Authentication**: No
- **Data Coverage**: Google internships
- **Function**: `fetch_google_careers_internships()`
- **Notes**: Direct scraping from Google's careers site

#### Microsoft Careers
- **File**: `sources/tech_companies_source.py`
- **Status**: ✅ Working
- **Authentication**: No
- **Data Coverage**: Microsoft internships
- **Function**: `fetch_microsoft_internships()`
- **Notes**: Direct scraping from Microsoft careers

#### Amazon Careers
- **File**: `sources/tech_companies_source.py`
- **Status**: ✅ Working
- **Authentication**: No
- **Data Coverage**: Amazon internships
- **Function**: `fetch_amazon_internships()`
- **Notes**: Direct scraping from Amazon jobs

### 3. College & Career Development

#### Handshake
- **File**: `sources/college_finance_source.py`
- **Status**: ⚠️ Limited (JavaScript rendering)
- **Authentication**: No (limited public data)
- **Data Coverage**: College internships
- **Function**: `fetch_handshake_internships()`
- **Notes**: College-focused platform, full access requires institutional account

#### ACM Internship Board
- **File**: `sources/college_finance_source.py`
- **Status**: ✅ Working
- **Authentication**: No
- **Data Coverage**: CS/Engineering internships
- **Function**: `fetch_acm_internship_board()`
- **Notes**: Association for Computing Machinery resources

### 4. Non-Profit & Mission-Driven

#### Idealist.org
- **File**: `sources/idealist_source.py`
- **Status**: ✅ API + HTML scraping
- **Authentication**: No
- **Data Coverage**: Non-profit internships
- **Functions**:
  - `fetch_idealist_org_opportunities()` (API)
  - `fetch_idealist_nonprofit_internships()` (HTML)
- **Notes**: Specializes in non-profit and social sector opportunities

### 5. Finance & Professional Services

#### Finance Internships
- **File**: `sources/college_finance_source.py`
- **Status**: ✅ Working
- **Authentication**: No
- **Data Coverage**: Finance/Banking/Consulting
- **Function**: `fetch_finance_internships()`
- **Notes**: Focus on financial services sector

### 6. Summer Programs

#### Summer Programs
- **File**: `sources/tech_companies_source.py`
- **Status**: ✅ Working
- **Authentication**: No
- **Data Coverage**: Summer internships
- **Function**: `fetch_summer_programs()`
- **Notes**: Seasonal opportunities with various durations

### 7. Government & STEM (API Key Required)

#### NASA Opportunities
- **File**: `sources/nasa_source.py`
- **Status**: ⚠️ Requires API Key
- **Authentication**: Required (NASA_API_KEY)
- **Data Coverage**: NASA internships/research
- **Function**: `fetch_nasa_opportunities()`
- **Setup**: Get key from https://api.nasa.gov/

#### USA Jobs
- **File**: `sources/usajobs_source.py`
- **Status**: ⚠️ Requires Credentials
- **Authentication**: Required (USAJOBS_EMAIL, USAJOBS_API_KEY)
- **Data Coverage**: Federal internships
- **Function**: `fetch_usajobs_opportunities()`
- **Setup**: https://developer.usajobs.gov/

#### NSF REU (Research Experience for Undergraduates)
- **File**: `sources/nsf_reu_source.py`
- **Status**: ⚠️ Experimental
- **Authentication**: No
- **Data Coverage**: NSF research programs
- **Function**: `fetch_nsf_reu_opportunities()`
- **Notes**: Research funding opportunities for students

#### NIH Opportunities
- **File**: `sources/nih_source.py`
- **Status**: ⚠️ Experimental
- **Authentication**: No
- **Data Coverage**: NIH internships/research
- **Function**: `fetch_nih_opportunities()`
- **Notes**: National Institutes of Health programs

#### Zooniverse
- **File**: `sources/zooniverse_source.py`
- **Status**: ⚠️ Experimental
- **Authentication**: No
- **Data Coverage**: Citizen science projects
- **Function**: `fetch_zooniverse_opportunities()`
- **Notes**: Community science research opportunities

### 8. Sample/Demo Sources

#### Sample API Source
- **File**: `sources/sample_api_source.py`
- **Status**: ✅ Demo Data
- **Authentication**: No
- **Data Coverage**: Mock API data
- **Function**: `fetch_api_opportunities()`
- **Notes**: For testing purposes

#### Sample HTML Source
- **File**: `sources/sample_html_source.py`
- **Status**: ✅ Demo Data
- **Authentication**: No
- **Data Coverage**: Mock HTML data
- **Function**: `fetch_html_opportunities()`
- **Notes**: For testing purposes

---

## Usage Statistics

**Total Sources**: 25+ functions across 10+ source files

**Working Sources**: 18+
**API-based**: 5
**HTML Scraping**: 12+
**Requiring Authentication**: 2
**Demo/Sample**: 2

---

## Adding Your Own Source

To add a new internship source:

1. **Create a new file** in `sources/`:
```python
# sources/my_source.py

def fetch_my_source_internships():
    """
    Fetch internships from my source.
    """
    opportunities = []
    
    try:
        # Your scraping logic here
        # Make sure each opportunity dict has these keys:
        # - title
        # - organization
        # - field
        # - description
        # - requirements
        # - citizenship
        # - grade_level
        # - location
        # - deadline
        # - url
        
        return opportunities
    except Exception as e:
        print(f"[My Source] Error: {e}")
        return []
```

2. **Import in scraper_main.py**:
```python
try:
    from sources.my_source import fetch_my_source_internships
    HAS_MY_SOURCE = True
except ImportError:
    HAS_MY_SOURCE = False
```

3. **Add to collect_all_opportunities()**:
```python
if HAS_MY_SOURCE:
    try:
        print("\nFetching from My Source:")
        opportunities = fetch_my_source_internships()
        if opportunities:
            all_opportunities.extend(opportunities)
    except Exception as e:
        print(f"[My Source] Error: {e}")
```

---

## Data Fields

Every opportunity returned includes:

| Field | Type | Example |
|-------|------|---------|
| title | str | "Software Engineer Intern" |
| organization | str | "Tech Company Inc." |
| field | str | "Technology/Software" |
| description | str | "Help develop new features..." |
| requirements | str | "Knowledge of Python" |
| citizenship | str | "Check website" |
| grade_level | str | "College/University" |
| location | str | "Remote" or "San Francisco, CA" |
| deadline | str | "2025-05-15" or "Ongoing" |
| url | str | "https://..." |

---

## Rate Limiting & Ethics

All sources respect:
- ✅ Robots.txt policies
- ✅ 1+ second delays between requests
- ✅ Proper User-Agent headers
- ✅ Terms of Service
- ✅ Public data only

---

## Troubleshooting Sources

**Source returns 0 opportunities:**
- Check internet connection
- Verify website is accessible
- Website HTML structure may have changed (update selectors)
- Some sources require API keys (see setup instructions)

**ImportError when running:**
- Ensure all dependencies are installed
- Check file names are correct
- Verify no syntax errors in source file

**Want to disable a source?**
Edit `scraper_main.py` and comment out or remove the source code section.

---

## Future Source Ideas

- [ ] LinkedIn (needs official API or permission)
- [ ] Monster.com internships
- [ ] FlexJobs
- [ ] StartupJobs.asia
- [ ] AngelList (now Wellfound)
- [ ] Product Hunt internships
- [ ] OpenDoor (company internships)
- [ ] Underdog.io
- [ ] Target internships (direct company scrapers)

---

## Support

For issues with specific sources:
1. Check the source file comments
2. Review the README.md troubleshooting section
3. Verify API credentials if required
4. Check website accessibility

