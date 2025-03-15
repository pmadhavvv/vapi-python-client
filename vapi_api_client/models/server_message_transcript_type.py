from enum import Enum


class ServerMessageTranscriptType(str, Enum):
    TRANSCRIPT = "transcript"
    TRANSCRIPTTRANSCRIPTTYPEFINAL = 'transcript[transcriptType="final"]'

    def __str__(self) -> str:
        return str(self.value)
