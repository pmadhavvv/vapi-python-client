from enum import Enum


class AzureOpenAICredentialProvider(str, Enum):
    AZURE_OPENAI = "azure-openai"

    def __str__(self) -> str:
        return str(self.value)
