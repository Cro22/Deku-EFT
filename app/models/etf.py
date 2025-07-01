# app/models.py

from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

# Create the base class for all ORM models
Base = declarative_base()

class ETF(Base):
    """
    Represents the list of ETFs to analyze.
    """
    __tablename__ = 'etfs'

    ticker = Column(String, primary_key=True)  # ETF symbol, e.g. "VTI"
    name = Column(String)                      # Human-readable name
