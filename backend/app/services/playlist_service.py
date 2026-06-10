from app.core.archetypes import ARCHETYPES


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


def get_archetype_by_id(archetype_id: str):
    for archetype in ARCHETYPES:
        if archetype["id"] == archetype_id:
            return archetype

    return ARCHETYPES[0]


def determine_archetype(mood_profile: dict):
    nostalgic = mood_profile["nostalgic"]
    dreamy = mood_profile["dreamy"]
    melancholic = mood_profile["melancholic"]
    energetic = mood_profile["energetic"]

    if nostalgic >= 80 and dreamy >= 70:
        return get_archetype_by_id("midnight_archivist")

    if melancholic >= 75 and nostalgic >= 60:
        return get_archetype_by_id("velvet_ruin")

    if energetic >= 80:
        return get_archetype_by_id("electric_pilgrim")

    if melancholic >= 65 and energetic >= 50:
        return get_archetype_by_id("soft_catastrophe")

    if dreamy >= 80:
        return get_archetype_by_id("fever_dreamer")

    return get_archetype_by_id("quiet_rebellion")


def analyze_playlist_by_id(playlist_id: str):
    mood_profile = {
        "nostalgic": 88,
        "dreamy": 76,
        "melancholic": 69,
        "energetic": 42,
    }

    archetype = determine_archetype(mood_profile)

    return {
        "playlist_id": playlist_id,
        "archetype": archetype,
        "mood_profile": mood_profile,
        "story": (
            "This playlist feels like a quiet drive through city lights, "
            "carrying old memories while slowly moving toward something new."
        ),
    }