from enum import Enum


class FallbackNeetsVoiceProvider(str, Enum):
    NEETS = "neets"

    def __str__(self) -> str:
        return str(self.value)
