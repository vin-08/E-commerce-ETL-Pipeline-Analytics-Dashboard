import os
import shutil
import time

BATCH_FOLDER = "/Users/vinayakkanojia/Desktop/etl project/data/batches"
RAW_FOLDER = "/Users/vinayakkanojia/Desktop/etl project/data/raw"

# list all the batch files
batch_files = sorted(os.listdir(BATCH_FOLDER))

for file in batch_files:
    source_path = os.path.join(BATCH_FOLDER, file)
    destination_path = os.path.join(RAW_FOLDER, file)

    # move file to raw folder
    shutil.move(source_path, destination_path)

    print(f"{file} released to raw folder")

    # wait for 10 seconds
    time.sleep(10)
