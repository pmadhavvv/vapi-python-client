from enum import Enum


class VoiceCostType(str, Enum):
    VOICE = "voice"

    def __str__(self) -> str:
        return str(self.value)
