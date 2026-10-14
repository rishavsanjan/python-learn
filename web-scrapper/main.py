import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url, timeout=10)

print(response.status_code)
print(response.text[:500])

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title)
print(soup.find("h1").text.strip())