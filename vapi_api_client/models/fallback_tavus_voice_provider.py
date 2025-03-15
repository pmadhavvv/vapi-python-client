from enum import Enum


class FallbackTavusVoiceProvider(str, Enum):
    TAVUS = "tavus"

    def __str__(self) -> str:
        return str(self.value)
