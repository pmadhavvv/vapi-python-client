from enum import Enum


class ServerMessageAssistantRequestType(str, Enum):
    ASSISTANT_REQUEST = "assistant-request"

    def __str__(self) -> str:
        return str(self.value)
