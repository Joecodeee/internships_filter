#!/usr/bin/env python3
"""
HIGH SCHOOL INTERNSHIP & SUMMER PROGRAM SCRAPER
Designed specifically for pre-college students (grades 9-12)
Aggregates internships, summer programs, and STEM opportunities from multiple sources
"""

import pandas as pd
import sys
from datetime import datetime
from pathlib import Path

# Import high school specific sources
from sources.high_school_source import (
    fetch_science_olympiad_opportunities,
    fetch_TASC_opportunities,
    fetch_stem_bootcamp_opportunities,
    fetch_work_learn_hs_programs,
    fetch_pre_college_research,
    fetch_high_school_internships,
)

# Import general sources (filtered for HS appropriateness)
from sources.sample_api_source import fetch_api_opportunities
from sources.sample_html_source import fetch_html_opportunities

# Try to import The Muse (has entry-level opportunities good for HS)
try:
    from sources.the_muse_source import fetch_muse_by_level
    HAS_MUSE = True
except ImportError:
    HAS_MUSE = False

# Import pre-college configuration
try:
    from precollegge_config import (
        is_high_school_appropriate,
        is_international_friendly,
        custom_filter,
    )
except ImportError:
    print("[Warning] precollegge_config not found, using basic filtering")
    
    def is_high_school_appropriate(text):
        if not text:
            return False
        text = text.lower()
        keywords = ["high school", "student", "teen", "youth", "grade", "secondary"]
        return any(k in text for k in keywords)
    
    def is_international_friendly(text):
        if not text:
            return False
        text = text.lower()
        keywords = ["international", "no citizenship", "visa", "welcome"]
        return any(k in text for k in keywords)
    
    def custom_filter(opportunity):
        return True


def collect_high_school_opportunities():
    """
    Collect internship & program opportunities specifically for high school students.
    """
    all_opportunities = []
    
    print("\n" + "="*70)
    print("HIGH SCHOOL INTERNSHIP & SUMMER PROGRAM SCRAPER")
    print("="*70)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # ===== HIGH SCHOOL SPECIFIC SOURCES =====
    print("🎓 FETCHING HIGH SCHOOL SPECIFIC PROGRAMS:")
    print("-" * 70)
    
    # Science Olympiad
    opportunities = fetch_science_olympiad_opportunities()
    if opportunities:
        all_opportunities.extend(opportunities)
        print(f"✓ Science Olympiad: {len(opportunities)} opportunity")
    
    # TASC (Tech Student Association)
    opportunities = fetch_TASC_opportunities()
    if opportunities:
        all_opportunities.extend(opportunities)
        print(f"✓ TASC: {len(opportunities)} opportunity")
    
    # STEM Bootcamps
    opportunities = fetch_stem_bootcamp_opportunities()
    if opportunities:
        all_opportunities.extend(opportunities)
        print(f"✓ STEM Bootcamps: {len(opportunities)} opportunities")
    
    # Work-Learn Programs
    opportunities = fetch_work_learn_hs_programs()
    if opportunities:
        all_opportunities.extend(opportunities)
        print(f"✓ Work-Learn Programs: {len(opportunities)} opportunities")
    
    # Pre-College Research Programs
    opportunities = fetch_pre_college_research()
    if opportunities:
        all_opportunities.extend(opportunities)
        print(f"✓ Pre-College Research: {len(opportunities)} opportunities")
    
    # General High School Internships
    opportunities = fetch_high_school_internships()
    if opportunities:
        all_opportunities.extend(opportunities)
        print(f"✓ High School Internships: {len(opportunities)} opportunities")
    
    # ===== ACCESSIBLE GENERAL SOURCES =====
    print("\n💼 FETCHING FROM ENTRY-LEVEL SOURCES:")
    print("-" * 70)
    
    # The Muse (entry-level)
    if HAS_MUSE:
        try:
            opportunities = fetch_muse_by_level()
            if opportunities:
                all_opportunities.extend(opportunities)
                print(f"✓ The Muse (Entry-Level): {len(opportunities)} opportunities")
        except Exception as e:
            print(f"⚠ The Muse: {e}")
    
    # Sample sources (for testing)
    print("\n📋 DEMO SOURCES:")
    print("-" * 70)
    
    opportunities = fetch_api_opportunities()
    if opportunities:
        # Only include if HS appropriate
        hs_opps = [opp for opp in opportunities 
                   if is_high_school_appropriate(opp.get("description", "") + " " + opp.get("requirements", ""))]
        if hs_opps:
            all_opportunities.extend(hs_opps)
            print(f"✓ Sample API: {len(hs_opps)} appropriate opportunities")
    
    opportunities = fetch_html_opportunities()
    if opportunities:
        hs_opps = [opp for opp in opportunities 
                   if is_high_school_appropriate(opp.get("description", "") + " " + opp.get("requirements", ""))]
        if hs_opps:
            all_opportunities.extend(hs_opps)
            print(f"✓ Sample HTML: {len(hs_opps)} appropriate opportunities")
    
    print("\n" + "="*70)
    print(f"TOTAL OPPORTUNITIES COLLECTED: {len(all_opportunities)}")
    print("="*70 + "\n")
    
    return all_opportunities


def filter_for_high_school(opportunities):
    """
    Filter opportunities to ensure they're appropriate for high school students.
    """
    filtered = []
    
    for opp in opportunities:
        # Check basic HS appropriateness
        desc_text = (opp.get("description", "") or "") + " " + (opp.get("requirements", "") or "")
        
        if not is_high_school_appropriate(desc_text):
            # Still keep if explicitly marked as high school
            if "high school" not in opp.get("grade_level", "").lower():
                continue
        
        filtered.append(opp)
    
    return filtered


def deduplicate_opportunities(opportunities):
    """Remove duplicate opportunities."""
    seen = set()
    unique = []
    
    for opp in opportunities:
        key = (opp.get("title", "").lower().strip(), opp.get("organization", "").lower().strip())
        if key not in seen:
            seen.add(key)
            unique.append(opp)
    
    print(f"✓ Deduplicated: {len(unique)} unique opportunities (removed {len(opportunities) - len(unique)} duplicates)")
    return unique


def categorize_opportunities(opportunities):
    """
    Categorize opportunities for better organization in Excel.
    """
    categories = {
        "STEM Programs": [],
        "Paid Internships": [],
        "Summer Programs": [],
        "Research Programs": [],
        "Leadership Programs": [],
        "General Internships": [],
    }
    
    for opp in opportunities:
        program_type = opp.get("program_type", "").lower()
        field = opp.get("field", "").lower()
        title = opp.get("title", "").lower()
        
        if "stem" in field or "science" in field or "tech" in field:
            categories["STEM Programs"].append(opp)
        elif "paid" in title or "paid" in program_type or program_type == "Paid Internship":
            categories["Paid Internships"].append(opp)
        elif "summer" in title or "camp" in program_type or "bootcamp" in program_type:
            categories["Summer Programs"].append(opp)
        elif "research" in program_type:
            categories["Research Programs"].append(opp)
        elif "leadership" in field or "leadership" in program_type:
            categories["Leadership Programs"].append(opp)
        else:
            categories["General Internships"].append(opp)
    
    return categories


def save_to_excel_categorized(opportunities, filename="high_school_internship_programs.xlsx"):
    """Save opportunities to Excel with multiple sheets by category."""
    try:
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            # Main sheet - all opportunities
            df_all = pd.DataFrame(opportunities)
            df_all = df_all[['title', 'organization', 'field', 'grade_level', 
                            'program_type', 'location', 'deadline', 'url', 'description']]
            df_all.to_excel(writer, sheet_name='All Opportunities', index=False)
            
            # Categorized sheets
            categories = categorize_opportunities(opportunities)
            for category, opps in categories.items():
                if opps:
                    df_cat = pd.DataFrame(opps)
                    sheet_name = category[:31]  # Excel sheet name limit
                    df_cat = df_cat[['title', 'organization', 'location', 'deadline', 'url']]
                    df_cat.to_excel(writer, sheet_name=sheet_name, index=False)
            
            # Summary sheet
            summary_data = {
                'Category': list(categories.keys()),
                'Count': [len(opps) for opps in categories.values()]
            }
            df_summary = pd.DataFrame(summary_data)
            df_summary.to_excel(writer, sheet_name='Summary', index=False)
        
        print(f"✓ Saved {len(opportunities)} opportunities to {filename}")
        
        # Print summary
        print("\n📊 PROGRAM BREAKDOWN:")
        for category, opps in categories.items():
            if opps:
                print(f"  • {category}: {len(opps)}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error saving to Excel: {e}")
        return False


def main():
    """Main execution function."""
    
    # Collect opportunities
    all_opportunities = collect_high_school_opportunities()
    
    if not all_opportunities:
        print("⚠ No opportunities were collected.")
        sys.exit(1)
    
    # Deduplicate
    unique_opportunities = deduplicate_opportunities(all_opportunities)
    
    # Filter for high school appropriateness
    print("\n🔍 Filtering for high school appropriateness...")
    filtered_opportunities = filter_for_high_school(unique_opportunities)
    print(f"✓ Filtered: {len(filtered_opportunities)} appropriate opportunities")
    
    # Export to Excel
    filename = "high_school_internship_programs.xlsx"
    save_to_excel_categorized(unique_opportunities, filename)
    
    # Export filtered to second file
    if len(filtered_opportunities) < len(unique_opportunities):
        filename_verified = "high_school_verified_programs.xlsx"
        save_to_excel_categorized(filtered_opportunities, filename_verified)
        print(f"✓ Verified opportunities also saved to {filename_verified}")
    
    # Print final summary
    print("\n" + "="*70)
    print("📝 EXPORT SUMMARY")
    print("="*70)
    print(f"✓ Main file: {filename}")
    if len(filtered_opportunities) < len(unique_opportunities):
        print(f"✓ Verified file: {filename_verified}")
    print(f"✓ Total opportunities: {len(unique_opportunities)}")
    print(f"✓ Verified for HS: {len(filtered_opportunities)}")
    print(f"✓ Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    # Preview
    if unique_opportunities:
        print("\n📋 TOP OPPORTUNITIES PREVIEW:")
        print("-" * 70)
        df_preview = pd.DataFrame(unique_opportunities[:5])
        print(df_preview[['title', 'organization', 'program_type', 'location']].to_string())


if __name__ == "__main__":
    main()
