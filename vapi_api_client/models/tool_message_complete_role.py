from enum import Enum


class ToolMessageCompleteRole(str, Enum):
    ASSISTANT = "assistant"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
