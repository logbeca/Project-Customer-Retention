from generate_data import generate_visits_data, generate_adcost_data
from database import SessionLocal, engine
from models import Base, AdCost as AdCostModel, Visits as VisitsModel, Transaction as TransactionModel
from schemas import AdCost, Visits

def insert_data(adcost_data, visits_data):
    db = SessionLocal()
    try:
        # Create tables if they don't exist
        Base.metadata.create_all(bind=engine)
        
        # Insert AdCost data
        for ad in adcost_data:
            validated_ad = AdCost(**ad)  # Validate data using Pydantic
            ad_record = AdCostModel(
                date_ad=validated_ad.date_ad,
                channel=validated_ad.channel,
                ad_cost=validated_ad.ad_cost,
                impressions=validated_ad.impressions,
                clicks=validated_ad.clicks,
                conversions=validated_ad.conversions
            )
            db.add(ad_record)

        # Insert Visits data
        for visit in visits_data:
            validated_visit = Visits(**visit)  # Validate Visits data with Pydantic
            
            # Insert Visit
            visit_entry = VisitsModel(
                user_id=validated_visit.user_id,
                date_time=validated_visit.date_time,
                session_id=validated_visit.session_id,
                device=validated_visit.device,
                location=validated_visit.location,
                source=validated_visit.source,
                pages_visited=validated_visit.pages_visited,
                time_on_site=validated_visit.time_on_site,
                events=validated_visit.events
            )
            db.add(visit_entry)
            db.flush()  # Ensure visit_entry.id is available for transaction linking

            # Insert associated Transaction data if it exists
            if validated_visit.transaction:
                for item in validated_visit.transaction.items:
                    transaction_entry = TransactionModel(
                        transaction_id=validated_visit.transaction.transaction_id,
                        shipping=validated_visit.transaction.shipping,
                        coupon=validated_visit.transaction.coupon,
                        payment_method=validated_visit.transaction.payment_method,
                        product_id=item.product_id,
                        quantity=item.quantity,
                        price=item.price
                    )
                    db.add(transaction_entry)

        # Commit all data once after all inserts
        db.commit()
        print("Data inserted successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")
        db.rollback()  # Rollback in case of error

    finally:
        db.close()
