from enum import Enum


class HumeVoiceProvider(str, Enum):
    HUME = "hume"

    def __str__(self) -> str:
        return str(self.value)
