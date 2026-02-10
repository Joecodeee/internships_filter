import requests

def fetch_api_opportunities():
    """
    Example API-style source.
    Replace the URL with a real API endpoint when available.
    """
    opportunities = []

    # Example mock data (replace with real API call)
    mock_data = [
        {
            "title": "STEM Research Internship",
            "organization": "Open Science Lab",
            "field": "Biology",
            "description": "Hands-on lab research. International students welcome.",
            "requirements": "High school students may apply.",
            "citizenship": "International students welcome.",
            "grade_level": "High school",
            "location": "Remote",
            "deadline": "2025-03-01",
            "url": "https://example.com/opportunity1"
        }
    ]

    opportunities.extend(mock_data)
    return opportunities