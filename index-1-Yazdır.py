from bs4 import BeautifulSoup

with open("index-1-.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

print(doc.prettify())