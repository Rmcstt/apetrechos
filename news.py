import requests
from bs4 import BeautifulSoup

def get_bbc_news_headlines():
    url = "https://www.bbc.com/news"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = []

        news_articles = soup.find_all("div", class_="gs-c-promo")
        for article in news_articles:
            headline = article.find("h3", class_="gs-c-promo-heading__title").text.strip()
            headlines.append(headline)

        return headlines
    else:
        print("Não foi possível obter as manchetes da BBC News.")
        return []

if __name__ == "__main__":
    headlines = get_bbc_news_headlines()

    if headlines:
        print("Principais Manchetes da BBC News:")
        for idx, headline in enumerate(headlines, 1):
            print(f"{idx}. {headline}")
    else:
        print("Nenhuma manchete encontrada.")

