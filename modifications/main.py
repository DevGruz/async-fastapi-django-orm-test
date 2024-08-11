import uvicorn
import asyncio
from fastapi import FastAPI

from core import settings
from api import api_router

app = FastAPI()
app.include_router(api_router)


async def main():
    config = uvicorn.Config(
        app,
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        log_level=settings.LOG_LEVEL,
    )

    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
