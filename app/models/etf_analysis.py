from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

# Create the base class for all ORM models
Base = declarative_base()

class ETFAnalysis(Base):
    """
    Stores the metrics and GPT response for each ETF analysis.
    """
    __tablename__ = 'etf_analysis'

    id = Column(String, primary_key=True)         # UUID for this analysis record
    ticker = Column(String)                       # Which ETF was analyzed
    total_return = Column(Float)                  # Total return % over the period
    volatility = Column(Float)                    # Annualized volatility %
    dividend_yield = Column(Float)                # Dividend yield %
    gpt_response = Column(String)                 # GPT's textual recommendation
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    # When the analysis was performed
