from enum import Enum


class CerebrasModelProvider(str, Enum):
    CEREBRAS = "cerebras"

    def __str__(self) -> str:
        return str(self.value)
