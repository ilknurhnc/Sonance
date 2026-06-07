from fastapi import FastAPI

app = FastAPI(
    title="Sonance",
    description="A music intelligence platform that analyzes playlists, generates stories, matches characters, and recommends songs.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Sonance",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "sonance-api",
    }