from enum import Enum


class ClientMessageTranscriptType(str, Enum):
    TRANSCRIPT = "transcript"
    TRANSCRIPTTRANSCRIPTTYPEFINAL = 'transcript[transcriptType="final"]'

    def __str__(self) -> str:
        return str(self.value)
