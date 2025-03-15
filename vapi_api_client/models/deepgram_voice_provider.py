from enum import Enum


class DeepgramVoiceProvider(str, Enum):
    DEEPGRAM = "deepgram"

    def __str__(self) -> str:
        return str(self.value)
