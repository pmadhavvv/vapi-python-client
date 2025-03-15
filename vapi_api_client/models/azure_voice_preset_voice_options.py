from enum import Enum


class AzureVoicePresetVoiceOptions(str, Enum):
    ANDREW = "andrew"
    BRIAN = "brian"
    EMMA = "emma"

    def __str__(self) -> str:
        return str(self.value)
