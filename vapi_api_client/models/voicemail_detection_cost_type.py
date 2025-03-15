from enum import Enum


class VoicemailDetectionCostType(str, Enum):
    VOICEMAIL_DETECTION = "voicemail-detection"

    def __str__(self) -> str:
        return str(self.value)
