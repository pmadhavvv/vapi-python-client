from enum import Enum


class CreateOutputToolDTOType(str, Enum):
    OUTPUT = "output"

    def __str__(self) -> str:
        return str(self.value)
