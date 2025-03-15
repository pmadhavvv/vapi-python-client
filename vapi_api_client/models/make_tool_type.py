from enum import Enum


class MakeToolType(str, Enum):
    MAKE = "make"

    def __str__(self) -> str:
        return str(self.value)
