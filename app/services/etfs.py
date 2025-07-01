from app.db.connection import SessionLocal
from app.models.etf import ETF


def get_etf_tickers() -> list[str]:
    """
    Fetch the list of ETF tickers from the database.
    """
    session = SessionLocal()
    try:
        etfs = session.query(ETF).all()
        return [etf.ticker for etf in etfs]
    finally:
        session.close()
