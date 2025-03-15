from enum import Enum


class FallbackDeepgramVoiceProvider(str, Enum):
    DEEPGRAM = "deepgram"

    def __str__(self) -> str:
        return str(self.value)
