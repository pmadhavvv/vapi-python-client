from enum import Enum


class CreateCerebrasCredentialDTOProvider(str, Enum):
    CEREBRAS = "cerebras"

    def __str__(self) -> str:
        return str(self.value)
