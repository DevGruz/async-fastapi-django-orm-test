import datetime
from pydantic import BaseModel


class FilterSchema(BaseModel):
    input_start: datetime.datetime


class ResultSchema(BaseModel):
    filtered_count: int
    client_info: str | None
    state_id: str | None
