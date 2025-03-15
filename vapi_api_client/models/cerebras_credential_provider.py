from enum import Enum


class CerebrasCredentialProvider(str, Enum):
    CEREBRAS = "cerebras"

    def __str__(self) -> str:
        return str(self.value)
