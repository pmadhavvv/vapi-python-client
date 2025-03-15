from enum import Enum


class CreateMakeToolDTOType(str, Enum):
    MAKE = "make"

    def __str__(self) -> str:
        return str(self.value)
