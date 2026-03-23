import pandas as pd
import os

SOURCE_FILE = "/Users/vinayakkanojia/Desktop/etl project/data/source/olist_order_items_dataset.csv"
BATCH_FOLDER = "data/batches"

df = pd.read_csv(SOURCE_FILE)

batch_size = 100

#split data into batches
for i in range(0, len(df), batch_size):

    batch = df.iloc[i:i+batch_size]

    batch_file = f"{BATCH_FOLDER}/order_items_batch_{i//batch_size}.csv"

    batch.to_csv(batch_file, index=False)

print("Batches created successfully")
