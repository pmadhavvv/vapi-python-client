from enum import Enum


class DeepgramCredentialProvider(str, Enum):
    DEEPGRAM = "deepgram"

    def __str__(self) -> str:
        return str(self.value)
