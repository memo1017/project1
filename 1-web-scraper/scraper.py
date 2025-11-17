import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select(".product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text
    link = url + book.h3.a["href"]
    
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Link: {link}")
    print("-" * 40)
