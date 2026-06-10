from urllib.parse import urlencode

import httpx

from app.core.config import settings


SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_CURRENT_USER_URL = "https://api.spotify.com/v1/me"
SPOTIFY_PLAYLISTS_URL = "https://api.spotify.com/v1/me/playlists"


def build_spotify_login_url():
    query_params = {
        "client_id": settings.spotify_client_id,
        "response_type": "code",
        "redirect_uri": settings.spotify_redirect_uri,
        "scope": "playlist-read-private playlist-read-collaborative",
    }

    return f"{SPOTIFY_AUTH_URL}?{urlencode(query_params)}"


async def exchange_code_for_token(code: str):
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": settings.spotify_redirect_uri,
        "client_id": settings.spotify_client_id,
        "client_secret": settings.spotify_client_secret,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            SPOTIFY_TOKEN_URL,
            data=payload,
        )

    response.raise_for_status()

    return response.json()


async def get_current_user(access_token: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            SPOTIFY_CURRENT_USER_URL,
            headers={
                "Authorization": f"Bearer {access_token}",
            },
        )

    response.raise_for_status()

    return response.json()


async def get_current_user_playlists(access_token: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            SPOTIFY_PLAYLISTS_URL,
            headers={
                "Authorization": f"Bearer {access_token}",
            },
        )

    response.raise_for_status()

    return response.json()


async def get_playlist_tracks(access_token: str, playlist_id: str):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            headers={
                "Authorization": f"Bearer {access_token}",
            },
        )

    response.raise_for_status()

    return response.json()