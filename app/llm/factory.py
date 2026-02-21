from app.llm.base import BaseLLM


def get_llm() -> BaseLLM:
    """Factory function to get LLM provider instance."""
    from app.llm.gemini import GeminiLLM

    return GeminiLLM()
