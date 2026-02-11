#!/usr/bin/env python3
"""
Main Internship Scraper
Aggregates internship data from multiple sources and exports to Excel.
"""

import pandas as pd
import sys
from datetime import datetime
from pathlib import Path

# Import all sources
from sources.sample_api_source import fetch_api_opportunities
from sources.sample_html_source import fetch_html_opportunities
from sources.github_jobs_source import (
    fetch_github_jobs,
    fetch_real_python_jobs,
    fetch_internship_com
)

# Try to import other sources if they have working implementations
try:
    from sources.nasa_source import fetch_nasa_opportunities
    HAS_NASA = True
except ImportError:
    HAS_NASA = False

try:
    from sources.usajobs_source import fetch_usajobs_opportunities
    HAS_USAJOBS = True
except ImportError:
    HAS_USAJOBS = False

try:
    from sources.nih_source import fetch_nih_opportunities
    HAS_NIH = True
except ImportError:
    HAS_NIH = False

try:
    from sources.nsf_reu_source import fetch_nsf_reu_opportunities
    HAS_NSF = True
except ImportError:
    HAS_NSF = False

try:
    from sources.zooniverse_source import fetch_zooniverse_opportunities
    HAS_ZOONIVERSE = True
except ImportError:
    HAS_ZOONIVERSE = False

# New sources
try:
    from sources.the_muse_source import fetch_the_muse_opportunities, fetch_muse_by_level
    HAS_MUSE = True
except ImportError:
    HAS_MUSE = False

try:
    from sources.builtin_source import fetch_builtin_opportunities, fetch_builtin_startups
    HAS_BUILTIN = True
except ImportError:
    HAS_BUILTIN = False

try:
    from sources.idealist_source import fetch_idealist_org_opportunities, fetch_idealist_nonprofit_internships
    HAS_IDEALIST = True
except ImportError:
    HAS_IDEALIST = False

try:
    from sources.jobboards_source import (
        fetch_indeed_internships,
        fetch_internqueen_internships,
        fetch_chegg_internships,
        fetch_linkedin_internships
    )
    HAS_JOBBOARDS = True
except ImportError:
    HAS_JOBBOARDS = False

try:
    from sources.tech_companies_source import (
        fetch_google_careers_internships,
        fetch_microsoft_internships,
        fetch_amazon_internships,
        fetch_summer_programs
    )
    HAS_TECH_COMPANIES = True
except ImportError:
    HAS_TECH_COMPANIES = False

try:
    from sources.college_finance_source import (
        fetch_handshake_internships,
        fetch_vault_internships,
        fetch_finance_internships,
        fetch_acm_internship_board
    )
    HAS_COLLEGE_FINANCE = True
except ImportError:
    HAS_COLLEGE_FINANCE = False

# Import filtering and export functions
from vibecode import filter_opportunities, save_to_excel


def collect_all_opportunities():
    """
    Collect internship opportunities from all available sources.
    """
    all_opportunities = []
    
    print("\n" + "="*60)
    print("INTERNSHIP OPPORTUNITY SCRAPER")
    print("="*60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Fetch from working sources
    print("Fetching from Real Sources:")
    print("-" * 60)
    
    # Real Python Jobs (HTML scraping)
    opportunities = fetch_real_python_jobs()
    if opportunities:
        all_opportunities.extend(opportunities)
    
    # GitHub Jobs API (no authentication needed)
    opportunities = fetch_github_jobs()
    if opportunities:
        all_opportunities.extend(opportunities)
    
    # Internships.com scraper
    opportunities = fetch_internship_com()
    if opportunities:
        all_opportunities.extend(opportunities)
    
    # New sources - Job Boards
    if HAS_JOBBOARDS:
        try:
            print("\nFetching from Job Boards:")
            opportunities = fetch_indeed_internships()
            if opportunities:
                all_opportunities.extend(opportunities)
            
            opportunities = fetch_internqueen_internships()
            if opportunities:
                all_opportunities.extend(opportunities)
            
            opportunities = fetch_chegg_internships()
            if opportunities:
                all_opportunities.extend(opportunities)
        except Exception as e:
            print(f"[Job Boards] Error: {e}")
    
    # The Muse API
    if HAS_MUSE:
        try:
            print("\nFetching from The Muse:")
            opportunities = fetch_the_muse_opportunities()
            if opportunities:
                all_opportunities.extend(opportunities)
            
            opportunities = fetch_muse_by_level()
            if opportunities:
                all_opportunities.extend(opportunities)
        except Exception as e:
            print(f"[The Muse] Error: {e}")
    
    # Built In
    if HAS_BUILTIN:
        try:
            print("\nFetching from Built In:")
            opportunities = fetch_builtin_opportunities()
            if opportunities:
                all_opportunities.extend(opportunities)
            
            opportunities = fetch_builtin_startups()
            if opportunities:
                all_opportunities.extend(opportunities)
        except Exception as e:
            print(f"[Built In] Error: {e}")
    
    # Idealist.org (Non-profit internships)
    if HAS_IDEALIST:
        try:
            print("\nFetching from Idealist.org:")
            opportunities = fetch_idealist_org_opportunities()
            if opportunities:
                all_opportunities.extend(opportunities)
            
            opportunities = fetch_idealist_nonprofit_internships()
            if opportunities:
                all_opportunities.extend(opportunities)
        except Exception as e:
            print(f"[Idealist] Error: {e}")
    
    # Tech Companies
    if HAS_TECH_COMPANIES:
        try:
            print("\nFetching from Tech Company Careers:")
            opportunities = fetch_google_careers_internships()
            if opportunities:
                all_opportunities.extend(opportunities)
            
            opportunities = fetch_microsoft_internships()
            if opportunities:
                all_opportunities.extend(opportunities)
            
            opportunities = fetch_amazon_internships()
            if opportunities:
                all_opportunities.extend(opportunities)
            
            opportunities = fetch_summer_programs()
            if opportunities:
                all_opportunities.extend(opportunities)
        except Exception as e:
            print(f"[Tech Companies] Error: {e}")
    
    # College & Finance
    if HAS_COLLEGE_FINANCE:
        try:
            print("\nFetching from College/Finance Internship Platforms:")
            opportunities = fetch_handshake_internships()
            if opportunities:
                all_opportunities.extend(opportunities)
            
            opportunities = fetch_vault_internships()
            if opportunities:
                all_opportunities.extend(opportunities)
            
            opportunities = fetch_finance_internships()
            if opportunities:
                all_opportunities.extend(opportunities)
            
            opportunities = fetch_acm_internship_board()
            if opportunities:
                all_opportunities.extend(opportunities)
        except Exception as e:
            print(f"[College/Finance] Error: {e}")
    
    # Sample sources for demonstration
    print("\nFetching from Sample Sources (for demonstration):")
    print("-" * 60)
    
    opportunities = fetch_api_opportunities()
    if opportunities:
        all_opportunities.extend(opportunities)
        print(f"[Sample API] Fetched {len(opportunities)} sample opportunities")
    
    opportunities = fetch_html_opportunities()
    if opportunities:
        all_opportunities.extend(opportunities)
        print(f"[Sample HTML] Fetched {len(opportunities)} sample opportunities")
    
    # Optional sources (require API keys/setup)
    print("\nFetching from Optional Sources (requires API keys):")
    print("-" * 60)
    
    if HAS_NASA:
        try:
            opportunities = fetch_nasa_opportunities()
            if opportunities:
                all_opportunities.extend(opportunities)
        except Exception as e:
            print(f"[NASA] Skipped - {e}")
    else:
        print("[NASA] Source not available")
    
    if HAS_USAJOBS:
        try:
            opportunities = fetch_usajobs_opportunities()
            if opportunities:
                all_opportunities.extend(opportunities)
        except Exception as e:
            print(f"[USAJobs] Skipped - {e}")
    else:
        print("[USAJobs] Source not available")
    
    if HAS_NIH:
        try:
            opportunities = fetch_nih_opportunities()
            if opportunities:
                all_opportunities.extend(opportunities)
        except Exception as e:
            print(f"[NIH] Skipped - {e}")
    else:
        print("[NIH] Source not available")
    
    if HAS_NSF:
        try:
            opportunities = fetch_nsf_reu_opportunities()
            if opportunities:
                all_opportunities.extend(opportunities)
        except Exception as e:
            print(f"[NSF REU] Skipped - {e}")
    else:
        print("[NSF REU] Source not available")
    
    if HAS_ZOONIVERSE:
        try:
            opportunities = fetch_zooniverse_opportunities()
            if opportunities:
                all_opportunities.extend(opportunities)
        except Exception as e:
            print(f"[Zooniverse] Skipped - {e}")
    else:
        print("[Zooniverse] Source not available")
    
    print("\n" + "="*60)
    print(f"TOTAL OPPORTUNITIES COLLECTED: {len(all_opportunities)}")
    print("="*60 + "\n")
    
    return all_opportunities


def deduplicate_opportunities(opportunities):
    """
    Remove duplicate opportunities based on title and organization.
    """
    seen = set()
    unique = []
    
    for opp in opportunities:
        key = (opp.get("title", "").lower(), opp.get("organization", "").lower())
        if key not in seen:
            seen.add(key)
            unique.append(opp)
    
    print(f"After deduplication: {len(unique)} unique opportunities")
    return unique


def create_filters_sheet(filename):
    """
    Create an additional sheet with filtering recommendations.
    """
    try:
        workbook = pd.ExcelFile(filename)
        # Create a summary sheet with filtering info
        print(f"\nExcel file created with multiple sheets if pandas version supports it")
    except Exception as e:
        print(f"[Info] Could not add filters sheet: {e}")


def main():
    """
    Main function to orchestrate the scraping and export process.
    """
    
    # Collect opportunities from all sources
    all_opportunities = collect_all_opportunities()
    
    if not all_opportunities:
        print("ERROR: No opportunities were collected from any source.")
        print("Please check:")
        print("  1. Your internet connection")
        print("  2. Website availability")
        print("  3. API keys (if required)")
        sys.exit(1)
    
    # Deduplicate
    unique_opportunities = deduplicate_opportunities(all_opportunities)
    
    # Apply filtering (optional - can be skipped)
    print("\nApplying filters for inclusive opportunities...")
    filtered_opportunities = filter_opportunities(unique_opportunities)
    print(f"After filtering for citizenship/high school eligibility: {len(filtered_opportunities)} opportunities")
    
    # Export all to Excel
    filename_all = "internship_opportunities_all.xlsx"
    save_to_excel(unique_opportunities, filename_all)
    
    # Export filtered to Excel
    filename_filtered = "internship_opportunities_filtered.xlsx"
    if filtered_opportunities:
        save_to_excel(filtered_opportunities, filename_filtered)
    else:
        print("\nNote: No opportunities matched the filtering criteria. Using all opportunities instead.")
        save_to_excel(unique_opportunities, filename_filtered)
    
    # Create summary
    print("\n" + "="*60)
    print("EXPORT SUMMARY")
    print("="*60)
    print(f"✓ All opportunities: {filename_all}")
    print(f"✓ Filtered opportunities: {filename_filtered}")
    print(f"✓ Total unique opportunities: {len(unique_opportunities)}")
    print(f"✓ Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    # Display preview
    print("\nPREVIEW of First 5 Opportunities:")
    print("-" * 60)
    df = pd.DataFrame(unique_opportunities[:5])
    print(df[["title", "organization", "location", "url"]].to_string())
    print()


if __name__ == "__main__":
    main()
