from enum import Enum


class FallbackPlayHTVoiceProvider(str, Enum):
    PLAYHT = "playht"

    def __str__(self) -> str:
        return str(self.value)
