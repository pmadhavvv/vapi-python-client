from enum import Enum


class ClientMessageSpeechUpdateRole(str, Enum):
    ASSISTANT = "assistant"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
