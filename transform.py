import pandas as pd

def clean_order_items(df):
    df = df.drop_duplicates()

    df = df[df['price'] > 0]

    df = df.dropna(subset=["order_id", "product_id"])

    df["shipping_limit_date"] = pd.to_datetime(df["shipping_limit_date"])
    
    df["total_price"] = df["price"] + df["freight_value"]

    return df

