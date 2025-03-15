from enum import Enum


class XaiModelModel(str, Enum):
    GROK_2 = "grok-2"
    GROK_3 = "grok-3"
    GROK_BETA = "grok-beta"

    def __str__(self) -> str:
        return str(self.value)
