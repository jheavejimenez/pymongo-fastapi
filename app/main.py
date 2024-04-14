from fastapi import FastAPI

from app.interfaces.routes import router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app
