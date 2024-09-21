from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URL and database name from environment variables
MONGO_DB_URL = os.getenv("MONGO_DB_URL", "mongodb://localhost:27017/")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "restaurant_monitoring")

# Create MongoDB client
client = MongoClient(MONGO_DB_URL)

# Access the database
db = client[MONGO_DB_NAME]

# Collections
store_status_collection = db["store_status"]
business_hours_collection = db["business_hours"]
timezone_collection = db["timezones"]

# Function to return the database client
def get_db():
    return db
