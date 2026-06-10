from app.core.characters import CHARACTERS


def calculate_character_match_score(mood_profile: dict):
    nostalgic = mood_profile["nostalgic"]
    dreamy = mood_profile["dreamy"]
    melancholic = mood_profile["melancholic"]
    energetic = mood_profile["energetic"]

    emotional_depth = (nostalgic + dreamy + melancholic) / 3
    energy_balance = 100 - abs(energetic - 50)

    score = int((emotional_depth * 0.7) + (energy_balance * 0.3))

    return min(score, 100)


def determine_character_match(archetype: dict, mood_profile: dict):
    archetype_id = archetype["id"]

    for character in CHARACTERS:
        if archetype_id in character["associated_archetypes"]:
            return {
                "id": character["id"],
                "name": character["name"],
                "universe": character["universe"],
                "description": character["description"],
                "match_score": calculate_character_match_score(mood_profile),
                "reason": (
                    f"This playlist matches {character['name']} because both share the emotional language "
                    f"of {archetype['name']}: {archetype['tone']}."
                ),
            }

    fallback = CHARACTERS[0]

    return {
        "id": fallback["id"],
        "name": fallback["name"],
        "universe": fallback["universe"],
        "description": fallback["description"],
        "match_score": 70,
        "reason": "This character is the closest available match for the playlist profile.",
    }