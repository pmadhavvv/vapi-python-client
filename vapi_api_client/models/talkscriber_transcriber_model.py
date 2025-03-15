from enum import Enum


class TalkscriberTranscriberModel(str, Enum):
    WHISPER = "whisper"

    def __str__(self) -> str:
        return str(self.value)
