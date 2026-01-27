from app.config import settings
from app.llm.base import BaseLLM


def get_llm(provider: str | None = None) -> BaseLLM:
    """Factory function to get LLM provider instance."""
    provider = provider or settings.llm_provider

    if provider == "openai":
        from app.llm.openai import OpenAILLM

        return OpenAILLM()
    elif provider == "anthropic":
        from app.llm.anthropic import AnthropicLLM

        return AnthropicLLM()
    else:
        raise ValueError(f"Unknown LLM provider: {provider}")
