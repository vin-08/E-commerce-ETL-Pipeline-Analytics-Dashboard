from sqlalchemy import create_engine

def load_to_mysql(df):

    username = "root"
    password = "root%401234"
    host = "localhost"
    database = "ecommerce"

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