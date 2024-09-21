from pydantic import BaseModel
from datetime import datetime

class ReportBase(BaseModel):
    store_id: int
    uptime_last_hour: int
    uptime_last_day: int
    uptime_last_week: int
    downtime_last_hour: int
    downtime_last_day: int
    downtime_last_week: int

class ReportCreate(ReportBase):
    pass

class Report(ReportBase):
    id: int
    class Config:
        orm_mode = True
