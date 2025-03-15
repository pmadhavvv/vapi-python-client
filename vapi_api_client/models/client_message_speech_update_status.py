from enum import Enum


class ClientMessageSpeechUpdateStatus(str, Enum):
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
