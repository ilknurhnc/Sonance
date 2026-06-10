from urllib.parse import urlencode

from app.core.config import settings


SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"


def build_spotify_login_url():
    query_params = {
        "client_id": settings.spotify_client_id,
        "response_type": "code",
        "redirect_uri": settings.spotify_redirect_uri,
        "scope": "playlist-read-private playlist-read-collaborative",
    }

    return f"{SPOTIFY_AUTH_URL}?{urlencode(query_params)}"