def get_user_playlists():
    return [
        {
            "id": "playlist_1",
            "name": "Late Night Drive",
            "track_count": 42,
            "description": "Songs for quiet roads and city lights.",
        },
        {
            "id": "playlist_2",
            "name": "Soft Chaos",
            "track_count": 28,
            "description": "Emotional, messy, and strangely comforting.",
        },
    ]


def analyze_playlist_by_id(playlist_id: str):
    return {
        "message": "Playlist received",
        "playlist_id": playlist_id,
    }