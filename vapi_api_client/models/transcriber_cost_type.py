from enum import Enum


class TranscriberCostType(str, Enum):
    TRANSCRIBER = "transcriber"

    def __str__(self) -> str:
        return str(self.value)
