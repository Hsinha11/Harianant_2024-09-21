from app.database import store_status_collection, business_hours_collection, timezone_collection
from datetime import datetime, timedelta
import pytz

def calculate_uptime_downtime(store_id, start_date, end_date):
    # Convert strings to datetime objects
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d')

    # Fetch the store's timezone
    timezone = timezone_collection.find_one({"store_id": store_id})
    if timezone:
        local_tz = pytz.timezone(timezone["timezone_str"])
    else:
        local_tz = pytz.UTC  # Default to UTC if not found

    # Fetch business hours for the store
    business_hours = business_hours_collection.find({"store_id": store_id})

    uptime = timedelta(0)
    downtime = timedelta(0)

    for hours in business_hours:
        # Get the store's business hours
        start_time = datetime.strptime(hours["start_time_local"], '%H:%M:%S').time()
        end_time = datetime.strptime(hours["end_time_local"], '%H:%M:%S').time()

        # Query the store status collection for statuses between start_date and end_date
        status_records = store_status_collection.find({
            "store_id": store_id,
            "timestamp_utc": {
                "$gte": start_datetime.isoformat() + "Z",
                "$lte": end_datetime.isoformat() + "Z"
            }
        })

        # Calculate uptime/downtime based on store statuses
        for record in status_records:
            timestamp = datetime.strptime(record["timestamp_utc"], '%Y-%m-%dT%H:%M:%S.%fZ')
            status = record["status"]

            if status == "active":
                uptime += timedelta(minutes=15)  # Add 15 minutes uptime
            else:
                downtime += timedelta(minutes=15)  # Add 15 minutes downtime

    return {
        "uptime": uptime.total_seconds() / 3600,  # Return uptime in hours
        "downtime": downtime.total_seconds() / 3600  # Return downtime in hours
    }
