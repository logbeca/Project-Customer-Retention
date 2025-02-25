from generate_data import generate_visits_data
from generate_data import generate_adcost_data
from database import  engine
import models
from models import Base
from insert_data import insert_data


# Create tables if they don't exist
models.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    # Generate sample data
    adcost = generate_adcost_data()
    visits = generate_visits_data()

    # Insert data into the database
    insert_data(adcost, visits)
