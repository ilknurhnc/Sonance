from pydantic import BaseModel


class PlaylistCreateRequest(BaseModel):
    playlist_id: str


class PlaylistResponse(BaseModel):
    id: str
    name: str
    track_count: int
    description: str


class PlaylistDetailResponse(BaseModel):
    id: str
    name: str
    track_count: int
    description: str
    analysis_status: str


class PlaylistListResponse(BaseModel):
    items: list[PlaylistResponse]
    total: int


class MoodProfile(BaseModel):
    nostalgic: int
    dreamy: int
    melancholic: int
    energetic: int


class ArchetypeResponse(BaseModel):
    id: str
    name: str
    description: str
    tone: str


class PlaylistAnalysisResponse(BaseModel):
    playlist_id: str
    archetype: ArchetypeResponse
    mood_profile: MoodProfile
    story: str