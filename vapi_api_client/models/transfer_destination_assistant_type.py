from enum import Enum


class TransferDestinationAssistantType(str, Enum):
    ASSISTANT = "assistant"

    def __str__(self) -> str:
        return str(self.value)
