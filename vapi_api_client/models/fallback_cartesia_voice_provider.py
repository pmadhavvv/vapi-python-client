from enum import Enum


class FallbackCartesiaVoiceProvider(str, Enum):
    CARTESIA = "cartesia"

    def __str__(self) -> str:
        return str(self.value)
