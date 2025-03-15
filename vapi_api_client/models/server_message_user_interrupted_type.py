from enum import Enum


class ServerMessageUserInterruptedType(str, Enum):
    USER_INTERRUPTED = "user-interrupted"

    def __str__(self) -> str:
        return str(self.value)
