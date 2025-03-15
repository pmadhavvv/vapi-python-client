from enum import Enum


class GatherType(str, Enum):
    GATHER = "gather"

    def __str__(self) -> str:
        return str(self.value)
