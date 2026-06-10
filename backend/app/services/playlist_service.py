MOCK_PLAYLISTS = [
    {
        "id": "playlist_1",
        "name": "Late Night Drive",
        "track_count": 42,
        "description": "Songs for quiet roads and city lights.",
        "analysis_status": "pending",
    },
    {
        "id": "playlist_2",
        "name": "Soft Chaos",
        "track_count": 28,
        "description": "Emotional, messy, and strangely comforting.",
        "analysis_status": "pending",
    },
]


def get_user_playlists():
    return MOCK_PLAYLISTS


def get_playlist_by_id(playlist_id: str):
    for playlist in MOCK_PLAYLISTS:
        if playlist["id"] == playlist_id:
            return playlist

    return None