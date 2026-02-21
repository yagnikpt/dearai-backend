from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # App
    app_name: str = "DearAI"
    debug: bool = False

    # Database
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"

    # JWT
    jwt_secret_key: str = "change-me-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 30

    # LLM
    gemini_api_key: str = ""

    # Google
    google_cloud_project: str = ""
    google_cloud_location: str = "us-central1"

    # Speech
    stt_provider: str = "openai"
    tts_provider: str = "openai"

    # Hume.ai
    hume_api_key: str = ""
    hume_secret_key: str = ""

    # SarvamAI
    sarvam_api_key: str = ""

    # Guardrails
    guardrails_enabled: bool = True


settings = Settings()
