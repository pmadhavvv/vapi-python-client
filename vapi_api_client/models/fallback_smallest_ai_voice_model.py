from enum import Enum


class FallbackSmallestAIVoiceModel(str, Enum):
    LIGHTNING = "lightning"

    def __str__(self) -> str:
        return str(self.value)
