from src.extract.csvfile import extract_csv
from src.transform.csv_transform import transform_csv
from src.load.csv_load import load_csv
import logging

processed_records = None
extracted_records = None

logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
    )

logging.info("ETL process is started")

try:
    logging.info("Starting Extract")
    extracted_records = extract_csv() #Extract Process
    logging.info("Extract completed")

except Exception as e:
    logging.error(f"Error in extract {e}")
    

#print(extracted_records)
if extracted_records:
    try:
        processed_records = transform_csv(extracted_records)
        logging.info("Process is completed")

    except Exception as e:
        logging.error(f"Error in process {e}")
        
#print(processed_records)
if processed_records:
    try:
        load_csv(processed_records)
        logging.info("Load is completed")

    except Exception as e:
        logging.error(f"Load is failed {e}")
