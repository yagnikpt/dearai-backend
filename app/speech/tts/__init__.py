from app.config import settings
from app.speech.tts.base import BaseTTS


def get_tts(provider: str | None = None) -> BaseTTS:
    """Factory function to get TTS provider instance."""
    provider = provider or settings.tts_provider

    if provider == "openai":
        from app.speech.tts.openai import OpenAITTS

        return OpenAITTS()
    else:
        raise ValueError(f"Unknown TTS provider: {provider}")
