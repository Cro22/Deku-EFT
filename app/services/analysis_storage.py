import uuid
from datetime import datetime

from app.db.connection import SessionLocal
from app.models.etf_analysis import ETFAnalysis
from app.services.stocks import calculate_metrics

def save_etf_analysis(tickers: list[str], gpt_response: str) -> None:
    """
    Save the ETF metrics and GPT response into the database.

    Args:
        tickers (list[str]): List of ETF symbols to process.
        gpt_response (str): Full textual analysis returned by GPT.
    """
    # Open a new database session
    session = SessionLocal()
    try:
        for ticker in tickers:
            # Calculate metrics for this ticker
            metrics = calculate_metrics(ticker)
            if "error" in metrics:
                # Skip if no data was returned
                continue

            # Build a new ORM object
            record = ETFAnalysis(
                id=str(uuid.uuid4()),            # Unique identifier
                ticker=ticker,                   # e.g. "VTI"
                total_return=metrics["total_return"],
                volatility=metrics["volatility"],
                dividend_yield=metrics["dividend_yield"],
                gpt_response=gpt_response,       # Store the same GPT text for each row
                timestamp=datetime.utcnow()      # Record when this was saved
            )
            session.add(record)

        # Commit all changes in one transaction
        session.commit()
    finally:
        # Always close the session to release connections
        session.close()
