# QUICKSTART GUIDE

## One-Minute Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the scraper
python scraper_main.py

# 3. Open the Excel files
#    - internship_opportunities_all.xlsx
#    - internship_opportunities_filtered.xlsx
```

## What You Get

Two Excel files with internship opportunities:
- **All opportunities** - Complete list of everything collected
- **Filtered opportunities** - Only high-school-eligible opportunities with inclusive citizenship policies

## File Structure

```
Title              | Organization        | Field    | Location | Deadline | ...
-------------------|---------------------|----------|----------|----------|-----
Software Internship| Tech Company        | Tech     | Remote   | 2025-03-15|...
```

## Common Tasks

### Run Full Scraper
```bash
python scraper_main.py
```

### View Examples
```bash
python examples.py
```

### Custom Filtering
Edit `vibecode.py` to change filtering logic for citizenship and education level.

### Add New Sources
1. Create file: `sources/my_source.py`
2. Add function: `def fetch_my_opportunities():`
3. Import in `scraper_main.py` and add to `collect_all_opportunities()`

### Use API Sources
```bash
export NASA_API_KEY="your_key"
export USAJOBS_EMAIL="your_email"
export USAJOBS_API_KEY="your_key"
python scraper_main.py
```

## Output Files

| File | Purpose |
|------|---------|
| `internship_opportunities_all.xlsx` | All opportunities |
| `internship_opportunities_filtered.xlsx` | Filtered results |
| `example_*.xlsx` | Various examples |

## Troubleshooting

**No Excel files created?**
- Check internet connection (for external sources)
- Verify pandas/openpyxl installed: `pip install -r requirements.txt`

**No data in results?**
- Some sources require API keys (see README.md)
- Sample sources always work for testing

**Want more opportunities?**
- Internet connection needed for real sources
- Configure API keys for enhanced sources

## Next Steps

1. ✅ Run `python scraper_main.py`
2. ✅ Open generated Excel files
3. ✅ Customize filtering in `vibecode.py`
4. ✅ Add your own data sources
5. ✅ Set up API keys for enhanced sources

## Support

See [README.md](README.md) for detailed documentation and troubleshooting.
