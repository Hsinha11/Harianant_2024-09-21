from pydantic import BaseModel, Field
from bson import ObjectId

# Pydantic model for Store Status
class StoreStatus(BaseModel):
    store_id: int
    timestamp_utc: str
    status: str

# Pydantic model for Business Hour
class BusinessHour(BaseModel):
    store_id: int
    dayOfWeek: int
    start_time_local: str
    end_time_local: str

# Pydantic model for Store Timezone
class StoreTimezone(BaseModel):
    store_id: int
    timezone_str: str

# For MongoDB ObjectId handling
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

# You can add any additional model logic or methods as needed
