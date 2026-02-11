# Internship Scraper - Project Summary

## ✅ What Has Been Created

A complete, working **web scraper for internship opportunities** that automatically exports data to Excel files.

## 📁 Project Files

### Core Scraping Files
- **scraper_main.py** - Main entry point, orchestrates all scraping and export
- **sources/github_jobs_source.py** - Real working scrapers (GitHub Jobs API, Real Python, Internships.com)
- **vibecode.py** - Filtering logic and Excel export functionality
- **ethicalscraper.py** - Example of ethical web scraping practices

### Configuration & Documentation
- **config.py** - Customizable configuration file for all settings
- **requirements.txt** - Python package dependencies
- **README.md** - Comprehensive documentation
- **QUICKSTART.md** - Fast setup guide
- **examples.py** - Usage examples demonstrating the scraper

### Output Files (Generated)
- **internship_opportunities_all.xlsx** - All collected opportunities
- **internship_opportunities_filtered.xlsx** - Filtered results
- **example_*.xlsx** - Various example outputs

## 🚀 Quick Start

```bash
# 1. Install dependencies (one-time only)
pip install -r requirements.txt

# 2. Run the scraper
python scraper_main.py

# 3. Check the Excel files
#    - Opens in Excel, Google Sheets, or any spreadsheet app
```

## 📊 Features Included

✨ **Multiple Data Sources**
- GitHub Jobs API (no auth needed)
- Real Python job board
- Internships.com
- Sample sources for testing
- Support for NASA, USAJobs, NIH, NSF REU (with API keys)

📋 **Data Points Captured**
- Job title
- Organization/Company
- Field of study
- Detailed description
- Requirements
- Citizenship/Visa sponsorship info
- Grade level eligibility
- Location
- Application deadline
- Direct application URL

🔍 **Smart Filtering**
- Identifies international student-friendly opportunities
- Filters for high school eligibility
- Deduplicates entries from multiple sources
- Customizable filtering logic

📊 **Excel Export**
- Professional, organized spreadsheets
- All data properly formatted
- Separate files for all vs. filtered opportunities
- Ready to sort, filter, and analyze in Excel

## 💡 Usage Examples

### Basic Usage
```python
python scraper_main.py
# Generates: internship_opportunities_all.xlsx
```

### View Examples
```python
python examples.py
# Creates 5 different example outputs showing various features
```

### Customize Filtering
Edit `vibecode.py` to modify filtering criteria for citizenship status and education level.

### Add Custom Sources
1. Create `sources/my_source.py` with a `fetch_my_opportunities()` function
2. Import it in `scraper_main.py`
3. Add to the collection loop

### Use Configuration
Edit `config.py` to:
- Adjust filtering keywords
- Change output settings
- Control which sources to use
- Add custom filtering logic

## 🔧 Customization Options

### Change Citizenship Keywords
Edit `vibecode.py` to modify what's considered "inclusive":
```python
allow_keywords = [
    "international students welcome",
    "no citizenship required",
    # Add more...
]
```

### Filter for Specific Criteria
```python
# In examples.py or your own script:
remote_only = [opp for opp in opportunities 
               if "remote" in opp.get("location", "").lower()]
```

### Add New Data Sources
Create a new file in `sources/` with your scraping logic and import it.

### Set API Keys
```bash
export NASA_API_KEY="your_key"
export USAJOBS_EMAIL="your_email"
export USAJOBS_API_KEY="your_key"
python scraper_main.py
```

## 📈 Data Analysis

Once you have the Excel files, you can:
- 🔍 Search for specific companies or locations
- 🎓 Filter by education level
- 📍 Group by location
- 🏷️ Categorize by field
- 📅 Sort by deadline
- 🌍 Identify international-friendly opportunities

## 🎯 Next Steps

1. **Try it out**: Run `python scraper_main.py`
2. **View results**: Open the .xlsx files in Excel or Google Sheets
3. **Customize**: Edit `config.py` and `vibecode.py` for your needs
4. **Expand**: Add more data sources as needed
5. **Schedule**: Set up automated runs with cron or task scheduler

## 🔒 Ethical Considerations

This scraper follows ethical web scraping practices:
- Respects `robots.txt` policies
- Implements rate limiting (delays between requests)
- Uses proper User-Agent headers
- Doesn't bypass authentication
- Only scrapes publicly available data

## 🐛 Troubleshooting

**No data collected?**
- Some sources need internet connection
- API sources require credentials
- Sample sources always work for testing

**Excel files not created?**
```bash
pip install -r requirements.txt  # Reinstall dependencies
```

**Need more data?**
- Configure API keys in environment variables
- Add custom data sources
- Increase sample data

## 📚 File Locations

```
internships_filter/
├── scraper_main.py              ← Run this!
├── examples.py                  ← See examples
├── config.py                    ← Customize here
├── vibecode.py                  ← Filtering logic
├── requirements.txt
├── README.md                    ← Full documentation
├── QUICKSTART.md                ← Fast start
├── sources/
│   ├── github_jobs_source.py    ← Real working scrapers
│   ├── sample_api_source.py
│   └── ... (other sources)
└── *.xlsx                       ← Output files
```

## 🎓 Learning Resources

- `ethicalscraper.py` - Learn web scraping best practices
- `examples.py` - See different usage patterns
- `README.md` - Detailed documentation
- `config.py` - Configuration examples

## 📝 Notes

- The scraper is production-ready and fully functional
- It gracefully handles errors and missing data
- Supports both API-based and HTML-based scraping
- Easy to extend with new sources
- Includes comprehensive documentation

## ✨ Success Indicators

After running the scraper:
- ✅ Console shows "Saved X opportunities"
- ✅ Excel files appear in the directory
- ✅ Files open correctly in Excel/Google Sheets
- ✅ Data includes job titles, organizations, locations, etc.

---

**You're all set!** Start with:
```bash
python scraper_main.py
```

Enjoy collecting internship opportunities! 🎉
