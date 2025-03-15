from enum import Enum


class SpeechmaticsTranscriberModel(str, Enum):
    DEFAULT = "default"

    def __str__(self) -> str:
        return str(self.value)
