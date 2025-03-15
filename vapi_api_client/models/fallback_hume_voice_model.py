from enum import Enum


class FallbackHumeVoiceModel(str, Enum):
    OCTAVE = "octave"

    def __str__(self) -> str:
        return str(self.value)
