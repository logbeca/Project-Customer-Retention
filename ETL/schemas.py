from pydantic import BaseModel
from datetime import datetime, date
from typing import List, Optional, Dict

class AdCost(BaseModel):
    date_ad: date
    channel: str
    ad_cost: float
    impressions: int
    clicks: int
    conversions: int

class Item (BaseModel):
    product_id: int
    quantity: int
    price:  float

class Transaction(BaseModel):
    transaction_id: str
    shipping: float
    coupon: Optional[str]
    payment_method: str
    items: List[Item]
  

class Visits(BaseModel):
    user_id: str
    date_time: datetime
    session_id: str
    device: str
    location: str
    source: str
    pages_visited: int
    time_on_site: int
    events: str
    transaction: Optional[Transaction]