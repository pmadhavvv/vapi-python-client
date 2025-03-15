from enum import Enum


class ClientMessageSpeechUpdateType(str, Enum):
    SPEECH_UPDATE = "speech-update"

    def __str__(self) -> str:
        return str(self.value)
