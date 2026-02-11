# Internship Opportunity Scraper

A Python-based web scraper that collects internship opportunities from multiple sources and exports them to Excel files with optional filtering.

## 🎓 FOR HIGH SCHOOL STUDENTS?

If you're a high school student looking for internships and summer programs, **run this instead:**

```bash
python scraper_highschool.py
```

Then read: **[PRECOLLEGEGE_QUICKSTART.md](PRECOLLEGEGE_QUICKSTART.md)**

This finds programs specifically for grades 9-12, including:
- Summer STEM camps (iD Tech, Kode With Klossy)
- Research programs (MIT RSI, Harvard TASP)
- Paid internships
- Competitions (Science Olympiad, TASC)
- And much more!

**56+ programs in one click!** ⭐

## Features

✨ **Multiple Data Sources** (30+ scrapers!)
- Real Python Jobs (HTML scraping)
- GitHub Jobs API (no authentication required)
- Internships.com (web scraping)
- **NEW:** The Muse API (entry-level internships)
- **NEW:** Indeed (major job board)
- **NEW:** Intern Queen (student-focused)
- **NEW:** Chegg Internships
- **NEW:** Built In (tech companies)
- **NEW:** Idealist.org (non-profit sector)
- **NEW:** Google, Microsoft, Amazon careers
- **NEW:** Handshake (college internships)
- **NEW:** Vault (finance/consulting)
- **NEW:** ACM (CS/Engineering)
- Sample API and HTML sources for demonstration
- Support for NASA, USAJobs, NIH, NSF REU, and Zooniverse (with API keys)

📊 **Smart Excel Export**
- All opportunities exported to `internship_opportunities_all.xlsx`
- Filtered opportunities exported to `internship_opportunities_filtered.xlsx`
- Automatic deduplication of entries
- Organized columns with all relevant information

🔍 **Intelligent Filtering**
- Filter for inclusive citizenship policies
- Identify high school eligible opportunities
- Easily customize filtering logic

## Installation

### 1. Clone or navigate to the project
```bash
cd internships_filter
```

### 2. Create a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Documentation Files

- **README.md** (this file) - General overview
- **QUICKSTART.md** - Fast setup guide
- **SOURCES.md** - Detailed source documentation (NEW!)
- **NEW_SOURCES_SUMMARY.md** - Summary of recently added sources (NEW!)
- **PROJECT_SUMMARY.md** - Complete project overview
- **config.py** - Configuration options
### 🎓 PRE-COLLEGE (HIGH SCHOOL) SPECIFIC:
- **PRECOLLEGEGE_QUICKSTART.md** - Fast start for HS students ⭐
- **HIGH_SCHOOL_GUIDE.md** - Comprehensive guide for teens
- **PRECOLLEGEGE_RESOURCES.md** - Tips, resume templates, resources
- **PRECOLLEGEGE_SUMMARY.md** - Full transformation summary
- **precollegge_config.py** - HS-specific configuration
## Usage

### Quick Start: Run the Scraper
```bash
python scraper_main.py
```

This will:
1. Fetch internship opportunities from multiple sources
2. Deduplicate entries
3. Apply filtering (citizenship and high school eligibility)
4. Export results to two Excel files:
   - `internship_opportunities_all.xlsx` - All collected opportunities
   - `internship_opportunities_filtered.xlsx` - Filtered results

### Output Files

The scraper generates Excel files with the following columns:
- **title** - Job/internship title
- **organization** - Company or organization name
- **field** - Field of study or work category
- **description** - Job description
- **requirements** - Position requirements
- **citizenship** - Citizenship/visa sponsorship information
- **grade_level** - Target education level (high school, college, etc.)
- **location** - Work location
- **deadline** - Application deadline
- **url** - Link to apply or learn more

## Customization

### Modify Filtering Logic
Edit `vibecode.py` to adjust filtering criteria:

```python
def is_inclusive_citizenship(text: str) -> bool:
    """Return True if the opportunity explicitly welcomes non‑US citizens."""
    # Add or modify keywords as needed

def is_high_school_eligible(text: str) -> bool:
    """Return True if the opportunity is open to high school students."""
    # Add or modify keywords as needed
```

### Add New Web Sources
Create a new source file in the `sources/` directory:

```python
# sources/custom_source.py
import requests

def fetch_custom_opportunities():
    """Fetch opportunities from your custom source."""
    opportunities = []
    
    # Your scraping logic here
    
    return opportunities
```

Then import and use it in `scraper_main.py`:

```python
from sources.custom_source import fetch_custom_opportunities

# In collect_all_opportunities():
opportunities = fetch_custom_opportunities()
if opportunities:
    all_opportunities.extend(opportunities)
```

### Enable API-Based Sources

To use sources that require API keys:

1. **NASA Internships**
   - Get an API key from https://api.nasa.gov/
   - Set environment variable: `NASA_API_KEY`

2. **USAJobs**
   - Get credentials from https://developer.usajobs.gov/
   - Set environment variables: `USAJOBS_EMAIL` and `USAJOBS_API_KEY`

Example (Linux/Mac):
```bash
export NASA_API_KEY="your_api_key_here"
export USAJOBS_EMAIL="your_email@example.com"
export USAJOBS_API_KEY="your_api_key_here"
python scraper_main.py
```

## Project Structure

```
internships_filter/
├── scraper_main.py              # Main entry point
├── ethicalscraper.py            # Example of ethical scraping
├── vibecode.py                  # Filtering and export logic
├── requirements.txt             # Python dependencies
└── sources/
    ├── __init__.py
    ├── github_jobs_source.py     # Real working sources
    ├── sample_api_source.py      # Sample API source
    ├── sample_html_source.py     # Sample HTML source
    ├── nasa_source.py            # NASA opportunities (requires API key)
    ├── nih_source.py             # NIH opportunities
    ├── nsf_reu_source.py         # NSF REU opportunities
    ├── usajobs_source.py         # USA Jobs (requires API key)
    └── zooniverse_source.py      # Zooniverse opportunities
```

## Ethical Scraping Guidelines

This project follows ethical web scraping practices:

1. **Respect robots.txt** - Checks website scraping policies
2. **Rate Limiting** - Adds delays between requests (minimum 1 second)
3. **User-Agent Headers** - Identifies the scraper properly
4. **No Session Hijacking** - Uses standard HTTP requests
5. **Data Usage** - Respect the source website's terms of service

See `ethicalscraper.py` for an example of responsible scraping.

## Troubleshooting

### No data being scraped
- Check your internet connection
- Verify websites are accessible
- Some websites' HTML structure may have changed - update selectors in the source files

### ImportError when running
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Make sure you're in the correct directory

### API sources not working
- Check that environment variables are set correctly
- Verify API keys are valid
- Check API quotas/rate limits

### Excel files not created
- Ensure pandas and openpyxl are installed correctly
- Check that you have write permissions in the directory
- Verify the DataFrame is not empty

## Performance Tips

- First run will take longer as it fetches data from multiple sources
- Add time delays if scraping many pages
- Use filtering to reduce Excel file size
- Consider running the scraper during off-peak hours to avoid rate limiting

## Future Enhancements

Potential improvements:
- [ ] Add more job board sources (LinkedIn, Indeed, etc.)
- [ ] Implement scheduled scraping with task scheduler
- [ ] Add email notifications for new opportunities
- [ ] Create a web interface for viewing results
- [ ] Add salary information parsing
- [ ] Implement machine learning for relevance scoring

## License

This project is provided as-is for educational and research purposes.

## Contributing

Feel free to:
- Add new data sources
- Improve scraping logic
- Enhance filtering capabilities
- Fix bugs and improve documentation

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the source files for specific API documentation
3. Examine the error messages carefully for clues
