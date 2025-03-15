from enum import Enum


class TalkscriberTranscriberProvider(str, Enum):
    TALKSCRIBER = "talkscriber"

    def __str__(self) -> str:
        return str(self.value)
