from app.core.mock_profiles import DEFAULT_MOOD_PROFILE, MOOD_PROFILES
from app.services.archetype_service import determine_archetype
from app.services.character_service import determine_character_match


def get_mock_mood_profile(playlist_id: str):
    return MOOD_PROFILES.get(playlist_id, DEFAULT_MOOD_PROFILE)


def generate_story(archetype: dict):
    return (
        f"This playlist belongs to {archetype['name']}. "
        f"It carries a {archetype['tone']} atmosphere, shaped by its emotional profile. "
        "It feels like a private scene from a film that was never fully explained."
    )


def analyze_playlist(playlist_id: str):
    mood_profile = get_mock_mood_profile(playlist_id)
    archetype = determine_archetype(mood_profile)
    character_match = determine_character_match(archetype, mood_profile)

    return {
        "playlist_id": playlist_id,
        "archetype": archetype,
        "mood_profile": mood_profile,
        "character_match": character_match,
        "story": generate_story(archetype),
    }