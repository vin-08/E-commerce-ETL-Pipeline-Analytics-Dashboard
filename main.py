import time
import os
import shutil

from src.extract import RAW_FOLDER, get_new_files, read_file
from src.transform import clean_order_items
from src.load import load_to_mysql

RAW_FOLDER = "/Users/vinayakkanojia/Desktop/etl project/data/raw"
PROCESSED_FOLDER = "/Users/vinayakkanojia/Desktop/etl project/data/processed"

def run_pipeline():

    files = get_new_files()

    for file in files:
        print(f"processing {file}")

        #Extract 
        df = read_file(file)

        # Transform
        df_clean = clean_order_items(df)

        #Load
        load_to_mysql(df_clean)

        # Move Processed File
        source_path = os.path.join(RAW_FOLDER, file)
        dest_path = os.path.join(PROCESSED_FOLDER, file)

        print("Moving file to processed folder... \n")
        shutil.move(source_path, dest_path)

        print(f"{file} processed successfully \n")

while True:

    run_pipeline()

    print("waiting for new files....\n")
    time.sleep(10)
