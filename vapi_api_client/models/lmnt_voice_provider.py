from enum import Enum


class LMNTVoiceProvider(str, Enum):
    LMNT = "lmnt"

    def __str__(self) -> str:
        return str(self.value)
