from enum import Enum


class CustomMessageType(str, Enum):
    CUSTOM_MESSAGE = "custom-message"

    def __str__(self) -> str:
        return str(self.value)
