from sqlalchemy import Column, Integer, String, Date, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class AdCost(Base):
    __tablename__ = "adcost"
    id = Column(Integer, primary_key=True, index=True)
    date_ad = Column(DateTime, index=True)
    channel = Column(String, index=True)
    ad_cost = Column(Float, index=True)
    impressions = Column(Integer, index=True)
    clicks = Column(Integer, index=True)
    conversions = Column(Integer, index=True)


class Visits(Base):
    __tablename__ = "ecommerce_visits"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    date_time = Column(DateTime, index=True)
    session_id = Column(String, index=True)
    device = Column(String, index=True)
    location = Column(String, index=True)
    source = Column(String, index=True)
    pages_visited = Column(Integer, index=True)
    time_on_site = Column(Integer, index=True)
    events = Column(String, index=True)
    transaction_id = Column(Integer, index=True)  # ForeignKey to the Transaction table



class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    shipping = Column(Float, index=True)
    coupon = Column(String, index=True)
    payment_method = Column(String, index=True)
    product_id = Column(Integer,  index=True)  # ForeignKey to products table
    quantity = Column(Integer, index=True)
    price = Column(Float, index=True)

