from pydantic import BaseModel


class PlaylistResponse(BaseModel):
    id: str
    name: str
    track_count: int
    description: str


class PlaylistListResponse(BaseModel):
    items: list[PlaylistResponse]
    total: int

class PlaylistCreateRequest(BaseModel):
    playlist_id: str

class PlaylistAnalyzeResponse(BaseModel):
    message: str
    playlist_id: str