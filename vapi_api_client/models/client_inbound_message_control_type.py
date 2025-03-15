from enum import Enum


class ClientInboundMessageControlType(str, Enum):
    CONTROL = "control"

    def __str__(self) -> str:
        return str(self.value)
