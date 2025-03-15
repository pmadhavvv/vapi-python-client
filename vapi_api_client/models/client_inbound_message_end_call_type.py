from enum import Enum


class ClientInboundMessageEndCallType(str, Enum):
    END_CALL = "end-call"

    def __str__(self) -> str:
        return str(self.value)
