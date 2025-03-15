from enum import Enum


class HumeVoiceModel(str, Enum):
    OCTAVE = "octave"

    def __str__(self) -> str:
        return str(self.value)
