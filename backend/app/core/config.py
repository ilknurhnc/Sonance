from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Sonance"
    app_version: str = "0.1.0"
    app_description: str = "A music intelligence platform."
    environment: str = "development"

    spotify_client_id: str
    spotify_client_secret: str
    spotify_redirect_uri: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()