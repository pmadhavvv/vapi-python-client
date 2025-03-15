from enum import Enum


class SayHookType(str, Enum):
    SAY = "say"

    def __str__(self) -> str:
        return str(self.value)
