from enum import Enum


class FallbackRimeAIVoiceModel(str, Enum):
    MIST = "mist"
    MISTV2 = "mistv2"
    V1 = "v1"

    def __str__(self) -> str:
        return str(self.value)
