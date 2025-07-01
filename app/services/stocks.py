import yfinance as yf
import pandas as pd

def get_stock_data(ticker: str, period: str = "6mo") -> pd.DataFrame:
    stock = yf.Ticker(ticker)
    return stock.history(period=period)

def build_prompt_from_data(ticker: str) -> str:
    df = get_stock_data(ticker).tail(10)
    summary = df[['Close']].to_string()
    return f"Based on the following closing prices for {ticker}, tell me if it's a good long-term investment and why:\n\n{summary}"
