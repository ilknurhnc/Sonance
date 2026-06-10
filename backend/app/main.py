from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.health import router as health_router
from app.api.playlists import router as playlists_router
from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
)


app.include_router(health_router)
app.include_router(playlists_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name}",
        "docs": "/docs",
        "health": "/health",
    }