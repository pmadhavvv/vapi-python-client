from enum import Enum


class ServerMessageHangType(str, Enum):
    HANG = "hang"

    def __str__(self) -> str:
        return str(self.value)
