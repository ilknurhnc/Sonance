from urllib.parse import urlencode

import httpx

from app.core.config import settings


SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"


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