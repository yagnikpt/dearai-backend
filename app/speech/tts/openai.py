from openai import AsyncOpenAI

from app.config import settings
from app.speech.tts.base import BaseTTS


class OpenAITTS(BaseTTS):
    def __init__(self, model: str = "tts-1"):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
        self.model = model

    async def synthesize(self, text: str, voice: str = "alloy") -> bytes:
        response = await self.client.audio.speech.create(
            model=self.model,
            voice=voice,
            input=text,
        )
        return response.content
