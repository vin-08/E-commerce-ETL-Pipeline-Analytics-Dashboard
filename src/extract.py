import os
import pandas as pd

RAW_FOLDER = "/Users/vinayakkanojia/Desktop/etl project/data/raw"

def get_new_files():
    files = os.listdir(RAW_FOLDER)
    csv_files = [f for f in files if f.endswith(".csv")]
    return csv_files

def read_file(file_name):
    file_path = os.path.join(RAW_FOLDER, file_name)
    df = pd.read_csv(file_path)
    return df


