import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:root%401234@localhost/ecommerce")

customers = pd.read_csv("/Users/vinayakkanojia/Desktop/etl project/data/source/olist_customers_dataset.csv")
products = pd.read_csv("/Users/vinayakkanojia/Desktop/etl project/data/source/olist_products_dataset.csv")
sellers = pd.read_csv("/Users/vinayakkanojia/Desktop/etl project/data/source/olist_sellers_dataset.csv")

customers.to_sql("customers", engine, if_exists="append", index=False)
products.to_sql("products", engine, if_exists="append", index=False)
sellers.to_sql("sellers", engine, if_exists="append", index=False)
