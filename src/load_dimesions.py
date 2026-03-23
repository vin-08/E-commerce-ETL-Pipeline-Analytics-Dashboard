import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Fetch values from .env
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")

# Create engine
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

customers = pd.read_csv(r"data/source/olist_customers_dataset.csv")
products = pd.read_csv(r"data/source/olist_products_dataset.csv")
sellers = pd.read_csv(r"data/source/olist_sellers_dataset.csv")
orders_data = pd.read_csv(r"data/source/olist_orders_dataset.csv")

customers.to_sql("customers", engine, if_exists="append", index=False)
products.to_sql("products", engine, if_exists="append", index=False)
sellers.to_sql("sellers", engine, if_exists="append", index=False)
orders_data.to_sql("orders_data", engine, if_exists="append", index=False)
