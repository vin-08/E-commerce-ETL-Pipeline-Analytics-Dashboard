from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def load_to_mysql(df):

    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    database = os.getenv("DB_NAME")

    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}/{database}"
    )

    df.to_sql(
        name = "order_items",
        con = engine,
        if_exists = "append",
        index = False,
        method="multi"
    )

    print("Data loaded to MySQL")
