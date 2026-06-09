from fastapi import APIRouter

from app.schemas.playlist import (
    PlaylistAnalyzeResponse,
    PlaylistCreateRequest,
    PlaylistListResponse,
)
from app.services.playlist_service import (
    analyze_playlist_by_id,
    get_user_playlists,
)


router = APIRouter(
    prefix="/playlists",
    tags=["Playlists"],
)


@router.get("", response_model=PlaylistListResponse)
def list_playlists():
    playlists = get_user_playlists()

    return {
        "items": playlists,
        "total": len(playlists),
    }


@router.post(
    "/analyze",
    response_model=PlaylistAnalyzeResponse,
)
def analyze_playlist(payload: PlaylistCreateRequest):
    return analyze_playlist_by_id(payload.playlist_id)