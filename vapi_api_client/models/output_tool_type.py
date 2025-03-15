from enum import Enum


class OutputToolType(str, Enum):
    OUTPUT = "output"

    def __str__(self) -> str:
        return str(self.value)
