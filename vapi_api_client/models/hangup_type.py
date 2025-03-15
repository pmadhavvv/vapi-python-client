from enum import Enum


class HangupType(str, Enum):
    HANGUP = "hangup"

    def __str__(self) -> str:
        return str(self.value)
