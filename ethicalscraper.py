import requests
from bs4 import BeautifulSoup
import time

url = "http://books.toscrape.com/"

headers = {
    "User-Agent": "YourName-EthicalScraper/1.0"
}

# 1. Check robots.txt manually before scraping
robots = requests.get(url + "robots.txt")
print(robots.text)

# 2. Fetch page respectfully
time.sleep(1)  # rate limiting
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# 3. Extract data
books = soup.select(".product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text
    print(title, price)