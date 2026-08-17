import requests
from bs4 import BeautifulSoup
import csv


def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()   # raises an error if status code is 400/500
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None


def parse_quotes(html):
    soup = BeautifulSoup(html, "html.parser")
    quote_blocks = soup.find_all("div", class_="quote")

    quotes = []
    for block in quote_blocks:
        text = block.find("span", class_="text").get_text(strip=True)
        author = block.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in block.find_all("a", class_="tag")]

        quotes.append({
            "text": text,
            "author": author,
            "tags": ", ".join(tags)
        })

    return quotes


def scrape_all_pages(base_url):
    all_quotes = []
    page = 1

    while True:
        url = f"{base_url}/page/{page}/"
        print(f"Scraping page {page}...")

        html = fetch_page(url)
        if html is None:
            break

        soup = BeautifulSoup(html, "html.parser")
        quote_blocks = soup.find_all("div", class_="quote")

        if not quote_blocks:   # no more quotes = no more pages
            print("No more pages found.")
            break

        all_quotes.extend(parse_quotes(html))
        page += 1

    return all_quotes


def save_to_csv(quotes, filename="quotes.csv"):
    if not quotes:
        print("No quotes to save.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["text", "author", "tags"])
        writer.writeheader()
        writer.writerows(quotes)

    print(f"Saved {len(quotes)} quotes to {filename}")


# Run it
base_url = "https://quotes.toscrape.com"
quotes = scrape_all_pages(base_url)
save_to_csv(quotes)