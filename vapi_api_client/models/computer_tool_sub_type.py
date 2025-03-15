from enum import Enum


class ComputerToolSubType(str, Enum):
    COMPUTER_20241022 = "computer_20241022"

    def __str__(self) -> str:
        return str(self.value)
