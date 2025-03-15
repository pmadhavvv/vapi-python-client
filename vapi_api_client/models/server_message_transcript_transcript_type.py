from enum import Enum


class ServerMessageTranscriptTranscriptType(str, Enum):
    FINAL = "final"
    PARTIAL = "partial"

    def __str__(self) -> str:
        return str(self.value)
