import requests
from bs4 import BeautifulSoup

URL = "https://www.linkedin.com/in/muhammad-ahmad-aftab-85a635315/?trk=opento_sprofile_topcard"

def fetch_headlines():
    # 1. Fetch the HTML page
    response = requests.get(URL)
    if response.status_code != 200:
        print("❌ Failed to fetch page")
        return []

    # 2. Parse HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # 3. Extract headlines (they're inside <a class="storylink"> or <span class="titleline"> in new HN)
    headlines = []
    for item in soup.select(".titleline a"):
        headlines.append(item.get_text())

    return headlines

def main():
    headlines = fetch_headlines()
    if not headlines:
        print("No headlines found.")
        return

    print("\n📰 Hacker News Headlines:\n")
    for i, headline in enumerate(headlines, start=1):
        print(f"{i}. {headline}")

if __name__ == "__main__":
    main()
