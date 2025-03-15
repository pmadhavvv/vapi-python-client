from enum import Enum


class ExactReplacementType(str, Enum):
    EXACT = "exact"

    def __str__(self) -> str:
        return str(self.value)
