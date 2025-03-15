from enum import Enum


class FallbackNeuphonicVoiceModel(str, Enum):
    NEU_FAST = "neu_fast"
    NEU_HQ = "neu_hq"

    def __str__(self) -> str:
        return str(self.value)
