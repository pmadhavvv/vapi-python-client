from enum import Enum


class TavusVoiceProvider(str, Enum):
    TAVUS = "tavus"

    def __str__(self) -> str:
        return str(self.value)
