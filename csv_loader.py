from datetime import datetime
import csv
from model.raw_person import RawPerson

def load_raw_person(csv_file, session):
    buffer = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["dob"] = datetime.strptime(row["dob"], "%m/%d/%Y")

            raw_person = RawPerson(**row)
            buffer.append(raw_person)
            if len(buffer) % 5000 == 0:
                session.bulk_save_objects(buffer)
                buffer = []
        session.bulk_save_objects(buffer)
        buffer = []
        session.commit()