from enum import Enum


class FallbackLMNTVoiceProvider(str, Enum):
    LMNT = "lmnt"

    def __str__(self) -> str:
        return str(self.value)
