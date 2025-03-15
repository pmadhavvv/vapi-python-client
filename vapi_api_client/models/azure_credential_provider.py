from enum import Enum


class AzureCredentialProvider(str, Enum):
    AZURE = "azure"

    def __str__(self) -> str:
        return str(self.value)
