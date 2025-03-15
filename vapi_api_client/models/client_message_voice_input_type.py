from enum import Enum


class ClientMessageVoiceInputType(str, Enum):
    VOICE_INPUT = "voice-input"

    def __str__(self) -> str:
        return str(self.value)
