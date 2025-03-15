from enum import Enum


class FallbackAzureVoicePresetVoiceOptions(str, Enum):
    ANDREW = "andrew"
    BRIAN = "brian"
    EMMA = "emma"

    def __str__(self) -> str:
        return str(self.value)
