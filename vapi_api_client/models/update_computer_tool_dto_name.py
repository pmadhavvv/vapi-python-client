from enum import Enum


class UpdateComputerToolDTOName(str, Enum):
    COMPUTER = "computer"

    def __str__(self) -> str:
        return str(self.value)
