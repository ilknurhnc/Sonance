from app.core.archetypes import ARCHETYPES


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