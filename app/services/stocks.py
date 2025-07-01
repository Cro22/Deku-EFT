# app/services/stocks.py

import yfinance as yf
import pandas as pd
import numpy as np

def get_stock_data(ticker: str, period: str = "6mo") -> pd.DataFrame:
    """
    Fetch historical price data for the given ticker and period.
    Returns a DataFrame with Open/High/Low/Close/Volume.
    """
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    return df

def calculate_metrics(ticker: str, period: str = "6mo") -> dict:
    """
    Calculate key financial metrics for a ticker:
      - Total return over the period (in %)
      - Annualized volatility (standard deviation, in %)
      - Dividend yield (in %)
    """
    df = get_stock_data(ticker, period)
    if df.empty:
        return {"error": "no data"}

    # Price series and returns
    prices = df["Close"]
    returns = prices.pct_change().dropna()

    # Total return: (last / first - 1) * 100
    total_return = (prices.iloc[-1] / prices.iloc[0] - 1) * 100

    # Annualized volatility: std * sqrt(252) * 100
    volatility = returns.std() * np.sqrt(252) * 100

    # Dividend yield fetched from yfinance info (if available)
    info = yf.Ticker(ticker).info
    dividend_yield = info.get("dividendYield", 0) or 0
    dividend_yield *= 100  # convert to percentage

    return {
        "ticker": ticker,
        "total_return": round(total_return, 2),
        "volatility": round(volatility, 2),
        "dividend_yield": round(dividend_yield, 2),
    }

def build_metrics_prompt(tickers: list[str], period: str = "6mo") -> str:
    """
    Build a single prompt string that lists metrics for each ticker
    and asks GPT to recommend the best long-term investment.
    """
    prompt = (
        "Based on the following ETF metrics, recommend the best long-term investment:\n\n"
    )

    for ticker in tickers:
        metrics = calculate_metrics(ticker, period)
        if "error" in metrics:
            prompt += f"{ticker}: data unavailable\n\n"
            continue

        prompt += (
            f"{metrics['ticker']}:\n"
            f"- Total Return (last {period}): {metrics['total_return']}%\n"
            f"- Volatility (annualized): {metrics['volatility']}%\n"
            f"- Dividend Yield: {metrics['dividend_yield']}%\n\n"
        )

    prompt += "Please explain your reasoning clearly and give your final recommendation."
    return prompt
