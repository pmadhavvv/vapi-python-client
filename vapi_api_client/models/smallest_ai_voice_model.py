from enum import Enum


class SmallestAIVoiceModel(str, Enum):
    LIGHTNING = "lightning"

    def __str__(self) -> str:
        return str(self.value)
