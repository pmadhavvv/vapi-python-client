from enum import Enum


class ServerMessagePhoneCallControlType(str, Enum):
    PHONE_CALL_CONTROL = "phone-call-control"

    def __str__(self) -> str:
        return str(self.value)
