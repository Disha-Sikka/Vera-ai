from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Vera AI Challenge"
)

app.include_router(router)