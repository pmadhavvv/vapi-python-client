from enum import Enum


class FallbackSmallestAIVoiceProvider(str, Enum):
    SMALLEST_AI = "smallest-ai"

    def __str__(self) -> str:
        return str(self.value)
