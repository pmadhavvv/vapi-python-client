from enum import Enum


class ClientMessageTranscriptTranscriptType(str, Enum):
    FINAL = "final"
    PARTIAL = "partial"

    def __str__(self) -> str:
        return str(self.value)
