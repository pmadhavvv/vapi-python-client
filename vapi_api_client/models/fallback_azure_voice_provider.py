from enum import Enum


class FallbackAzureVoiceProvider(str, Enum):
    AZURE = "azure"

    def __str__(self) -> str:
        return str(self.value)
