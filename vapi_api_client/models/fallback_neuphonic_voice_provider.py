from enum import Enum


class FallbackNeuphonicVoiceProvider(str, Enum):
    NEUPHONIC = "neuphonic"

    def __str__(self) -> str:
        return str(self.value)
