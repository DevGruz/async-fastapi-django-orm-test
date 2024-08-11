from fastapi import APIRouter

from schemas import FilterSchema, ResultSchema
from services import get_filtered_data

router = APIRouter()


@router.post("/filter")
async def filter_data(filter_schema: FilterSchema) -> ResultSchema:
    data = await get_filtered_data(filter_schema)
    return data
