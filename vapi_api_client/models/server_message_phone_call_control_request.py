from enum import Enum


class ServerMessagePhoneCallControlRequest(str, Enum):
    FORWARD = "forward"
    HANG_UP = "hang-up"

    def __str__(self) -> str:
        return str(self.value)
