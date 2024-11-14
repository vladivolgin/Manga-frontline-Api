from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MANGADEX_API_URL: str = "https://api.mangadex.org"
    AUTH_URL: str = "https://auth.mangadex.org/realms/mangadex/protocol/openid-connect/token"
    API_V1_STR: str = "/api/v1"
    MANGADEX_USERNAME: str
    MANGADEX_PASSWORD: str
    MANGADEX_CLIENT_ID: str
    MANGADEX_CLIENT_SECRET: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()