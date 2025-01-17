"""
Sets up the API (FastAPI)
    * Routes
    * Middlewares + CORS
    * Events
"""

import logging
from timeit import default_timer as timer
from typing import Any

from app.api.endpoints import group, punishment, user
from app.config import settings
from app.db import Database
from app.http import HTTPClient
from app.state import State
from app.sync import OWSync
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from . import APIRoute, FastAPI, Request

logging.basicConfig(level=logging.DEBUG if settings.debug else logging.INFO)


def init_middlewares(app: FastAPI) -> None:
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next: Any) -> Any:
        start_time = timer()
        response = await call_next(request)
        end_time = timer()
        process_time = end_time - start_time
        response.headers["Process-Time-Ms"] = str(round(process_time * 1000, 2))
        return response

    origins = [
        "http://localhost",
        "http://127.0.0.1",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:4173",
        "http://127.0.0.1:4173",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Compress large responses
    app.add_middleware(GZipMiddleware)


def init_routes(app: FastAPI) -> None:
    app.include_router(user.router)
    app.include_router(group.router)
    app.include_router(punishment.router)


def init_events(app: FastAPI, **db_settings: str) -> None:
    @app.on_event("startup")
    async def start_handler() -> None:
        database = Database()
        app.set_db(database)

        http = HTTPClient()
        app.set_http(http)

        app.set_app_state(State())
        app.set_ow_sync(OWSync(app))

        await database.async_init(**db_settings)
        await http.async_init()

    @app.on_event("shutdown")
    async def shutdown_handler() -> None:
        database = app.db
        if database is not None:
            await database.close()

        if app.http is not None:
            await app.http.close()


def init_api(**db_settings: str) -> FastAPI:
    app = FastAPI()
    app.router.route_class = APIRoute
    init_middlewares(app)
    init_routes(app)
    init_events(app, **db_settings)
    return app


asgi_app = init_api()
