from enum import Enum


class FallbackHumeVoiceProvider(str, Enum):
    HUME = "hume"

    def __str__(self) -> str:
        return str(self.value)
