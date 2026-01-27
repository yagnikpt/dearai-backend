from openai import AsyncOpenAI

from app.config import settings
from app.llm.base import BaseLLM, LLMMessage


class OpenAILLM(BaseLLM):
    def __init__(self, model: str = "gpt-4o"):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
        self.model = model

    async def chat(self, messages: list[LLMMessage], system_prompt: str | None = None) -> str:
        msgs = []
        if system_prompt:
            msgs.append({"role": "system", "content": system_prompt})
        msgs.extend([m.to_dict() for m in messages])

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=msgs,
        )
        return response.choices[0].message.content or ""

    async def chat_stream(self, messages: list[LLMMessage], system_prompt: str | None = None):
        msgs = []
        if system_prompt:
            msgs.append({"role": "system", "content": system_prompt})
        msgs.extend([m.to_dict() for m in messages])

        stream = await self.client.chat.completions.create(
            model=self.model,
            messages=msgs,
            stream=True,
        )
        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
