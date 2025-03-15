from enum import Enum


class FallbackCartesiaVoiceModel(str, Enum):
    SONIC = "sonic"
    SONIC_2 = "sonic-2"
    SONIC_ENGLISH = "sonic-english"
    SONIC_MULTILINGUAL = "sonic-multilingual"
    SONIC_PREVIEW = "sonic-preview"

    def __str__(self) -> str:
        return str(self.value)
