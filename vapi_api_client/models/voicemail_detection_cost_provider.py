from enum import Enum


class VoicemailDetectionCostProvider(str, Enum):
    GOOGLE = "google"
    OPENAI = "openai"
    TWILIO = "twilio"

    def __str__(self) -> str:
        return str(self.value)
