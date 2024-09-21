from app.database import get_db
from app.models import StoreStatus, BusinessHour, StoreTimezone
import csv

# Ingest store status CSV data into MongoDB
def ingest_store_status(file_path):
    db = get_db()
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        store_statuses = [
            {
                "store_id": int(row["store_id"]),
                "timestamp_utc": row["timestamp_utc"],
                "status": row["status"]
            } for row in reader
        ]
    db.store_status.insert_many(store_statuses)

# Ingest business hours CSV data into MongoDB
def ingest_business_hours(file_path):
    db = get_db()
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        business_hours = [
            {
                "store_id": int(row["store_id"]),
                "dayOfWeek": int(row["dayOfWeek"]),
                "start_time_local": row["start_time_local"],
                "end_time_local": row["end_time_local"]
            } for row in reader
        ]
    db.business_hours.insert_many(business_hours)

# Ingest store timezones CSV data into MongoDB
def ingest_timezone(file_path):
    db = get_db()
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        timezones = [
            {
                "store_id": int(row["store_id"]),
                "timezone_str": row["timezone_str"]
            } for row in reader
        ]
    db.timezones.insert_many(timezones)

if __name__ == "__main__":
    ingest_store_status('data/store_status.csv')
    ingest_business_hours('data/business_hours.csv')
    ingest_timezone('data/store_timezones.csv')
