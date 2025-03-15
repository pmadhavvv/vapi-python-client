from enum import Enum


class AzureVoiceProvider(str, Enum):
    AZURE = "azure"

    def __str__(self) -> str:
        return str(self.value)
