import httpx
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from app.services.spotify_service import (
    build_spotify_login_url,
    exchange_code_for_token,
    get_current_user,
    get_current_user_playlists,
    get_playlist_tracks,
)


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.get("/login")
def login_with_spotify():
    login_url = build_spotify_login_url()

    return RedirectResponse(login_url)


@router.get("/callback")
async def spotify_callback(
    code: str | None = None,
    error: str | None = None,
):
    if error:
        raise HTTPException(
            status_code=400,
            detail=error,
        )

    if code is None:
        raise HTTPException(
            status_code=400,
            detail="Authorization code is missing.",
        )

    token_data = await exchange_code_for_token(code)

    return {
        "status": "success",
        "token_data": token_data,
    }


@router.get("/me")
async def current_user(access_token: str):
    try:
        return await get_current_user(access_token)
    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=exc.response.status_code,
            detail="Invalid or expired Spotify access token.",
        ) from exc


@router.get("/playlists")
async def current_user_playlists(access_token: str):
    try:
        return await get_current_user_playlists(access_token)
    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=exc.response.status_code,
            detail="Invalid or expired Spotify access token.",
        ) from exc


@router.get("/playlists/{playlist_id}/tracks")
async def playlist_tracks(playlist_id: str, access_token: str):
    try:
        return await get_playlist_tracks(
            access_token=access_token,
            playlist_id=playlist_id,
        )
    except httpx.HTTPStatusError as exc:
        return {
            "status_code": exc.response.status_code,
            "spotify_error": exc.response.json(),
        }


