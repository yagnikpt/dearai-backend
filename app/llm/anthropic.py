from anthropic import AsyncAnthropic

from app.config import settings
from app.llm.base import BaseLLM, LLMMessage


class AnthropicLLM(BaseLLM):
    def __init__(self, model: str = "claude-sonnet-4-20250514"):
        self.client = AsyncAnthropic(api_key=settings.anthropic_api_key)
        self.model = model

    async def chat(self, messages: list[LLMMessage], system_prompt: str | None = None) -> str:
        msgs = [m.to_dict() for m in messages]

        response = await self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=system_prompt or "",
            messages=msgs,
        )
        return response.content[0].text

    async def chat_stream(self, messages: list[LLMMessage], system_prompt: str | None = None):
        msgs = [m.to_dict() for m in messages]

        async with self.client.messages.stream(
            model=self.model,
            max_tokens=4096,
            system=system_prompt or "",
            messages=msgs,
        ) as stream:
            async for text in stream.text_stream:
                yield text
