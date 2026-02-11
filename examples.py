#!/usr/bin/env python3
"""
Quick Example: How to use the Internship Scraper
This demonstrates the basic usage of the scraper
"""

import pandas as pd
from sources.sample_api_source import fetch_api_opportunities
from sources.sample_html_source import fetch_html_opportunities
from vibecode import filter_opportunities, save_to_excel

def example_basic_usage():
    """
    Example 1: Basic scraping and export
    """
    print("=" * 60)
    print("EXAMPLE 1: Basic Scraping and Export")
    print("=" * 60)
    
    # Collect opportunities from sources
    opportunities = []
    opportunities.extend(fetch_api_opportunities())
    opportunities.extend(fetch_html_opportunities())
    
    print(f"Collected {len(opportunities)} opportunities")
    
    # Export to Excel
    save_to_excel(opportunities, "example_basic.xlsx")
    print("✓ Saved to example_basic.xlsx\n")


def example_with_filtering():
    """
    Example 2: Scraping with filtering
    """
    print("=" * 60)
    print("EXAMPLE 2: Scraping with Filtering")
    print("=" * 60)
    
    # Collect opportunities
    opportunities = []
    opportunities.extend(fetch_api_opportunities())
    opportunities.extend(fetch_html_opportunities())
    
    print(f"Collected {len(opportunities)} total opportunities")
    
    # Apply filtering
    filtered = filter_opportunities(opportunities)
    print(f"After filtering: {len(filtered)} opportunities")
    
    # Export filtered results
    save_to_excel(filtered, "example_filtered.xlsx")
    print("✓ Saved to example_filtered.xlsx\n")


def example_custom_filtering():
    """
    Example 3: Custom filtering logic
    """
    print("=" * 60)
    print("EXAMPLE 3: Custom Filtering Logic")
    print("=" * 60)
    
    opportunities = []
    opportunities.extend(fetch_api_opportunities())
    opportunities.extend(fetch_html_opportunities())
    
    print(f"Collected {len(opportunities)} total opportunities")
    
    # Custom filter: only remote positions
    remote_only = [opp for opp in opportunities 
                   if "remote" in opp.get("location", "").lower()]
    
    print(f"Remote positions: {len(remote_only)}")
    
    save_to_excel(remote_only, "example_remote.xlsx")
    print("✓ Saved to example_remote.xlsx\n")


def example_pandas_analysis():
    """
    Example 4: Analyze results with pandas
    """
    print("=" * 60)
    print("EXAMPLE 4: Data Analysis with Pandas")
    print("=" * 60)
    
    opportunities = []
    opportunities.extend(fetch_api_opportunities())
    opportunities.extend(fetch_html_opportunities())
    
    # Convert to DataFrame for analysis
    df = pd.DataFrame(opportunities)
    
    print(f"Total opportunities: {len(df)}")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nFields represented:")
    print(df['field'].value_counts())
    
    print(f"\nLocations:")
    print(df['location'].value_counts())
    
    # Save summary
    df.to_excel("example_analysis.xlsx", index=False)
    print("\n✓ Saved detailed analysis to example_analysis.xlsx\n")


def example_deduplicate():
    """
    Example 5: Handle duplicate opportunities
    """
    print("=" * 60)
    print("EXAMPLE 5: Deduplication")
    print("=" * 60)
    
    # Simulate collecting from multiple sources with duplicates
    set1 = fetch_api_opportunities()
    set2 = fetch_api_opportunities()  # Same data again
    
    all_opps = set1 + set2
    print(f"Total before dedup: {len(all_opps)}")
    
    # Deduplicate
    seen = set()
    unique = []
    for opp in all_opps:
        key = (opp.get("title"), opp.get("organization"))
        if key not in seen:
            seen.add(key)
            unique.append(opp)
    
    print(f"Total after dedup: {len(unique)}")
    save_to_excel(unique, "example_deduped.xlsx")
    print("✓ Saved to example_deduped.xlsx\n")


if __name__ == "__main__":
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "    INTERNSHIP SCRAPER - USAGE EXAMPLES".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    # Run all examples
    example_basic_usage()
    example_with_filtering()
    example_custom_filtering()
    example_pandas_analysis()
    example_deduplicate()
    
    print("=" * 60)
    print("ALL EXAMPLES COMPLETED!")
    print("=" * 60)
    print("\nGenerated files:")
    print("  • example_basic.xlsx")
    print("  • example_filtered.xlsx")
    print("  • example_remote.xlsx")
    print("  • example_analysis.xlsx")
    print("  • example_deduped.xlsx")
    print("\nFor full scraping from all sources, run:")
    print("  python scraper_main.py")
    print()
