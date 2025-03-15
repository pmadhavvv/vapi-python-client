from enum import Enum


class TransferAssistantHookActionType(str, Enum):
    TRANSFER = "transfer"

    def __str__(self) -> str:
        return str(self.value)
