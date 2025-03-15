from enum import Enum


class SayType(str, Enum):
    SAY = "say"

    def __str__(self) -> str:
        return str(self.value)
