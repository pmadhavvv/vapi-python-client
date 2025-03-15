from enum import Enum


class ApiRequestMode(str, Enum):
    BACKGROUND = "background"
    BLOCKING = "blocking"

    def __str__(self) -> str:
        return str(self.value)
