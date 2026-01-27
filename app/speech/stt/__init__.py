from app.config import settings
from app.speech.stt.base import BaseSTT


def get_stt(provider: str | None = None) -> BaseSTT:
    """Factory function to get STT provider instance."""
    provider = provider or settings.stt_provider

    if provider == "openai":
        from app.speech.stt.openai import OpenAISTT

        return OpenAISTT()
    else:
        raise ValueError(f"Unknown STT provider: {provider}")
