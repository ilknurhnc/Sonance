from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.services.spotify_service import build_spotify_login_url


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.get("/login")
def login_with_spotify():
    login_url = build_spotify_login_url()

    return RedirectResponse(login_url)


@router.get("/callback")
def spotify_callback(code: str | None = None, error: str | None = None):
    if error:
        return {
            "status": "error",
            "message": error,
        }

    return {
        "status": "success",
        "code": code,
    }