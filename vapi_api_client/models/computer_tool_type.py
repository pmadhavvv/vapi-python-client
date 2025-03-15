from enum import Enum


class ComputerToolType(str, Enum):
    COMPUTER = "computer"

    def __str__(self) -> str:
        return str(self.value)
