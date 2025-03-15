from enum import Enum


class ServerMessageVoiceRequestType(str, Enum):
    VOICE_REQUEST = "voice-request"

    def __str__(self) -> str:
        return str(self.value)
