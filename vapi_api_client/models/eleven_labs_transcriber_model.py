from enum import Enum


class ElevenLabsTranscriberModel(str, Enum):
    SCRIBE_V1 = "scribe_v1"

    def __str__(self) -> str:
        return str(self.value)
