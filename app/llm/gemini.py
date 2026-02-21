import asyncio
from collections.abc import AsyncGenerator

from google import genai
from google.genai import types

from app.config import settings
from app.llm.base import BaseLLM, LLMMessage


class GeminiLLM(BaseLLM):
    def __init__(self, model: str = "gemini-2.5-flash"):
        print(settings)
        self.client = genai.Client(
            vertexai=True,
            project=settings.google_cloud_project,
            location=settings.google_cloud_location,
        )
        self.model = model

    def _build_contents(self, messages: list[LLMMessage]) -> list[types.Content]:
        contents = []
        for msg in messages:
            role = "model" if msg.role == "assistant" else "user"
            contents.append(types.Content(role=role, parts=[types.Part(text=msg.content)]))
        return contents

    async def chat(self, messages: list[LLMMessage], system_prompt: str | None = None) -> str:
        config = types.GenerateContentConfig(
            system_instruction=system_prompt or "",
        )
        response = await self.client.aio.models.generate_content(
            model=self.model,
            contents=self._build_contents(messages),
            config=config,
        )
        return response.text or ""

    async def chat_stream(
        self, messages: list[LLMMessage], system_prompt: str | None = None
    ) -> AsyncGenerator[str, None]:
        config = types.GenerateContentConfig(
            system_instruction=system_prompt or "",
        )
        async for chunk in await self.client.aio.models.generate_content_stream(
            model=self.model,
            contents=self._build_contents(messages),
            config=config,
        ):
            if chunk.text:
                yield chunk.text


async def main():
    llm = GeminiLLM()
    messages = [LLMMessage(role="user", content="Hello, how are you?")]
    response = await llm.chat(messages)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
