from enum import Enum


class ClientMessageUserInterruptedType(str, Enum):
    USER_INTERRUPTED = "user-interrupted"

    def __str__(self) -> str:
        return str(self.value)
