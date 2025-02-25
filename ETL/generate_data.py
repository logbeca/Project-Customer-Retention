from faker import Faker
import random
from datetime import datetime, timedelta



fake = Faker()
data_visits = []

ad_channels = ["Google Ads", "Facebook Ads", "Instagram Ads"]
devices = ["mobile","desktop","tablet"]
event_type =  ["pageview", "click", "purchase"]
coupon = ["FUN2025", "BRAND10", "INFLUENCER20"]
payment_method = ["credit_card", "paypal", "pix"]

def generate_visits_data():
    for i in range(100):
        user_id = fake.uuid4()
        pages = ["/home", "/products", "/checkout", "/blog", "/cart", f"/products/{random.randint(1,1000)}", "/wishlist", "/login","/orders"]
        date_time = fake.date_time_between(start_date="-30d", end_date="now")
        session_id = fake.uuid4()
        device = random.choice(devices)
        location = f"{fake.city()},{fake.country()}"
        source = random.choice(ad_channels)
        pages_visited = random.randint(1, len(pages))
        time_on_site = random.randint(1,10000)
        events = random.choice(event_type)
        transaction = None
        if events == "Purchase":
            items =  [{ "product_id" : random.randint(1,2000),
                        "quantity": random.randint(1,10) ,
                        "price": round(random.uniform(0,10000),2)
                    }
                        for _ in range(random.randint(1, 5))]
            transactions = []
            for item in items:
                transactions.append({
                    "transaction_id": fake.uuid4() ,
                    "shipping": round(random.uniform(20,200),2),
                    "coupon" : random.choice(coupon),
                    "payment_method": random.choice(payment_method) ,
                    "product_id": item["product_id"],
                    "quantity": item["quantity"],
                    "price": item["price"]
                })
        data_visits.append({
            "user_id": user_id,
            "date_time": date_time,
            "session_id": session_id,
            "device": device,
            "location": location,
            "source": source,
            "pages_visited": pages_visited,
            "time_on_site":time_on_site,
            "events": events,
            "transaction": transaction
    })
    return data_visits


# Data adCost

def generate_adcost_data():
    data_ads = []

    for i in range(40):
        date_ad =   (fake.date_time_between(start_date="-30d", end_date="now"))
        channel = random.choice(ad_channels)
        ad_cost = round(random.uniform(20,700), 2)
        impressions = random.randint(5000,50000)
        clicks = random.randint(100, impressions)
        conversions = random.randint(10, clicks)
        data_ads.append({
            "date_ad": date_ad , 
            "channel": channel ,
            "ad_cost": ad_cost,
            "impressions": impressions ,
            "clicks": clicks,
            "conversions": conversions
    })
    return data_ads