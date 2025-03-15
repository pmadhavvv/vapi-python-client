from enum import Enum


class ServerMessageStatusUpdateType(str, Enum):
    STATUS_UPDATE = "status-update"

    def __str__(self) -> str:
        return str(self.value)
