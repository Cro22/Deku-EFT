from app.services.etfs import get_etf_tickers
from app.services.stocks import build_metrics_prompt
from app.services.news import fetch_headlines, build_news_prompt
from app.services.gpt import ask_gpt
from app.services.analysis_storage import save_etf_analysis
from app.services.messenger import send_telegram_message

def main():
    # 1. Load tickers from DB
    tickers = get_etf_tickers()

    # 2. Build quantitative prompt
    q_prompt = build_metrics_prompt(tickers)

    # 3. Fetch news headlines and build qualitative prompt
    articles = fetch_headlines(tickers)
    n_prompt = build_news_prompt(articles)

    # 4. Combine prompts
    full_prompt = f"{q_prompt}\n\n{n_prompt}"

    # 5. Ask GPT
    analysis = ask_gpt(full_prompt)

    # 6. Persist analysis and metrics
    save_etf_analysis(tickers, analysis)

    # 7. Notify via Telegram
    send_telegram_message(f"📈 Combined ETF Analysis:\n\n{analysis}")

if __name__ == "__main__":
    main()
