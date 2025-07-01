import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = os.getenv("NEWS_API_URL")


def fetch_headlines(keywords: list[str], source: str = "newsapi") -> list[dict]:
    """
    Fetch the latest headlines for a list of keywords.
    Returns a list of dicts: [{'title': ..., 'url': ...}, …]
    """
    all_articles = []

    # Example with NewsAPI.org
    for kw in keywords:
        params = {
            "q": kw,
            "apiKey": NEWS_API_KEY,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 5
        }
        resp = requests.get(NEWS_API_URL, params=params)
        data = resp.json()
        if data.get("status") == "ok":
            for art in data["articles"]:
                all_articles.append({
                    "keyword": kw,
                    "title": art["title"],
                    "url": art["url"]
                })
    return all_articles


def build_news_prompt(articles: list[dict]) -> str:
    """
    Build a prompt summarizing headlines for GPT analysis.
    """
    prompt = "Here are the latest headlines for your target ETFs:\n\n"
    for art in articles:
        prompt += f"- [{art['keyword']}] {art['title']} ({art['url']})\n"
    prompt += (
        "\nConsidering these news items, tell me if any of these ETFs "
        "might be affected positively or negatively in the short term."
    )
    return prompt
