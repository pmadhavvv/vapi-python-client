from enum import Enum


class CreateTransferCallToolDTOType(str, Enum):
    TRANSFERCALL = "transferCall"

    def __str__(self) -> str:
        return str(self.value)
