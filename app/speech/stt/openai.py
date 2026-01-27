import io

from openai import AsyncOpenAI

from app.config import settings
from app.speech.stt.base import BaseSTT


class OpenAISTT(BaseSTT):
    def __init__(self, model: str = "whisper-1"):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
        self.model = model

    async def transcribe(self, audio_data: bytes, language: str = "en") -> str:
        audio_file = io.BytesIO(audio_data)
        audio_file.name = "audio.webm"

        response = await self.client.audio.transcriptions.create(
            model=self.model,
            file=audio_file,
            language=language,
        )
        return response.text
