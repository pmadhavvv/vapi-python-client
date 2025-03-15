from enum import Enum


class CallLogPrivilegedLevel(str, Enum):
    CHECKPOINT = "CHECKPOINT"
    ERROR = "ERROR"
    INFO = "INFO"
    LOG = "LOG"
    WARN = "WARN"

    def __str__(self) -> str:
        return str(self.value)
