from enum import Enum


class NeetsVoiceProvider(str, Enum):
    NEETS = "neets"

    def __str__(self) -> str:
        return str(self.value)
