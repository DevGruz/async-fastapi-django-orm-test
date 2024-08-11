from fastapi import APIRouter

from api.routes import filters

api_router = APIRouter()
api_router.include_router(filters.router, tags=["filters"])
