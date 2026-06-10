from fastapi import APIRouter, HTTPException

from app.schemas.playlist import (
    PlaylistAnalysisResponse,
    PlaylistCreateRequest,
    PlaylistDetailResponse,
    PlaylistListResponse,
)
from app.services.analysis_service import analyze_playlist
from app.services.playlist_service import (
    get_playlist_by_id,
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


@router.get(
    "/{playlist_id}",
    response_model=PlaylistDetailResponse,
)
def get_playlist(playlist_id: str):
    playlist = get_playlist_by_id(playlist_id)

    if playlist is None:
        raise HTTPException(
            status_code=404,
            detail="Playlist not found",
        )

    return playlist


@router.post(
    "/analyze",
    response_model=PlaylistAnalysisResponse,
)
def analyze_playlist_endpoint(payload: PlaylistCreateRequest):
    playlist = get_playlist_by_id(payload.playlist_id)

    if playlist is None:
        raise HTTPException(
            status_code=404,
            detail="Playlist not found",
        )

    return analyze_playlist(payload.playlist_id)