import csv
from pathlib import Path

def extract_csv():
    base_path = Path(__file__).resolve().parents[2]

    file_path = base_path / "data" / "raw" / "employees.csv"

    with open(file_path,"r",newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        extract_rec = []
        for read in reader:
            extract_rec.append(read)

    return extract_rec

