from abc import ABC, abstractmethod


class BaseTTS(ABC):
    """Abstract base class for Text-to-Speech providers."""

    @abstractmethod
    async def synthesize(self, text: str, lang: str = "en-IN", voice: str = "shubh") -> bytes:
        """Convert text to speech audio."""
        pass
