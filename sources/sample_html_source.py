import requests
from bs4 import BeautifulSoup

def fetch_html_opportunities():
    """
    Example HTML scraping source.
    Replace URL with a real page that allows scraping.
    """
    url = "https://example.com/internships"
    opportunities = []

    # Mock HTML (replace with real request)
    html = """
    <div class='opportunity'>
        <h2>AI Research Mentorship</h2>
        <span class='org'>FutureTech Institute</span>
        <p class='desc'>Open to all students globally. High school students may apply.</p>
        <p class='req'>No citizenship required.</p>
        <span class='field'>Computer Science</span>
        <span class='loc'>Remote</span>
        <span class='deadline'>2025-04-10</span>
        <a href='https://example.com/ai-mentorship'>Apply</a>
    </div>
    """

    soup = BeautifulSoup(html, "html.parser")

    for div in soup.select(".opportunity"):
        opportunities.append({
            "title": div.find("h2").text.strip(),
            "organization": div.find(class_="org").text.strip(),
            "field": div.find(class_="field").text.strip(),
            "description": div.find(class_="desc").text.strip(),
            "requirements": div.find(class_="req").text.strip(),
            "citizenship": div.find(class_="req").text.strip(),
            "grade_level": "High school",
            "location": div.find(class_="loc").text.strip(),
            "deadline": div.find(class_="deadline").text.strip(),
            "url": div.find("a")["href"]
        })

    return opportunities