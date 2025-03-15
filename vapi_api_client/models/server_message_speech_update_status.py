from enum import Enum


class ServerMessageSpeechUpdateStatus(str, Enum):
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
