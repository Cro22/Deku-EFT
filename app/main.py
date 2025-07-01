from services.etfs import get_etf_tickers
from services.stocks import build_metrics_prompt, calculate_metrics
from services.gpt import ask_gpt
from services.storage import save_analysis
from services.messenger import send_telegram_message

def main():
    tickers = get_etf_tickers()
    prompt = build_metrics_prompt(tickers)
    gpt_response = ask_gpt(prompt)

    save_analysis(tickers, gpt_response)
    send_telegram_message(f"📈 GPT ETF Metrics Analysis:\n\n{gpt_response}")

if __name__ == "__main__":
    main()
