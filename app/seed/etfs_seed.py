from app.db.connection import SessionLocal
from app.models.etf import ETF


def run():
    """
    Seed the ETF table with initial data.
    """
    session = SessionLocal()
    try:
        etfs = [
            ETF(ticker="VTI", name="Total Stock Market ETF"),
            ETF(ticker="SCHD", name="Schwab U.S. Dividend Equity ETF"),
            ETF(ticker="VXUS", name="Total International Stock ETF"),
            ETF(ticker="BND", name="Total Bond Market ETF")
        ]

        existing = {etf.ticker for etf in session.query(ETF).all()}
        new_etfs = [etf for etf in etfs if etf.ticker not in existing]

        session.add_all(new_etfs)
        session.commit()
        print(f"✅ Seeded {len(new_etfs)} ETF(s).")
    finally:
        session.close()

if __name__ == "__main__":
    run()
