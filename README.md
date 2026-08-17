# 🕷️ Web Scraper

A simple Python web scraper that collects quotes, authors, and tags from [Quotes to Scrape](https://quotes.toscrape.com/) and saves the extracted data into a CSV file.

## 📌 Overview

This project demonstrates the fundamentals of web scraping using Python. It automatically visits multiple pages of the website, extracts quote information, and stores the collected data in a structured CSV file.

The scraper continues through the available pages until no more quotes are found.

## ✨ Features

* 🌐 Fetches web pages using `requests`
* 🔍 Parses HTML using `BeautifulSoup`
* 📄 Extracts:

  * Quotes
  * Authors
  * Tags
* 🔄 Automatically scrapes multiple pages
* 📊 Saves results to a CSV file
* ⚠️ Handles request errors gracefully
* ⏱️ Uses a request timeout to prevent hanging requests

## 🛠️ Technologies Used

* **Python**
* **Requests**
* **BeautifulSoup**
* **CSV**

## 📁 Project Structure

```text
Web_Scraper/
│
├── Web_scraper.py
├── quotes.csv
├── README.md
└── .gitignore
```

## ⚙️ Installation

Make sure Python is installed on your system.

Install the required libraries:

```bash
pip install requests beautifulsoup4
```

## ▶️ How to Run

Navigate to the project directory:

```bash
cd Web_Scraper
```

Run the scraper:

```bash
python Web_scraper.py
```

The program will begin scraping the available pages:

```text
Scraping page 1...
Scraping page 2...
Scraping page 3...
...
No more pages found.
Saved 100 quotes to quotes.csv
```

## 📊 Output

The scraper creates `quotes.csv` containing three columns:

| Column   | Description                    |
| -------- | ------------------------------ |
| `text`   | The quote text                 |
| `author` | The author of the quote        |
| `tags`   | Tags associated with the quote |

Example:

```csv
text,author,tags
"The world as we have created it is a process of our thinking...",Albert Einstein,change deep-thoughts thinking world
```

## 🔄 How It Works

1. The program sends an HTTP request to the target website.
2. `BeautifulSoup` parses the returned HTML.
3. Quote blocks are located using their HTML classes.
4. Quote text, author, and tags are extracted.
5. The scraper moves to the next page.
6. The process continues until a page contains no quotes.
7. All collected data is saved to `quotes.csv`.

## 📚 Learning Objectives

This project demonstrates practical concepts including:

* HTTP requests
* HTML parsing
* Web scraping
* Exception handling
* Loops and functions
* Lists and dictionaries
* CSV file handling
* Data extraction and storage

## ⚠️ Disclaimer

This project is intended for educational purposes. When scraping websites, always respect the website's terms of service, robots.txt rules, and applicable laws.

## 👨‍💻 Author

**Mashood Ul Hassan**

Computer Science Student | Python | Data Science & AI Enthusiast
