from enum import Enum


class CreateAzureOpenAICredentialDTOProvider(str, Enum):
    AZURE_OPENAI = "azure-openai"

    def __str__(self) -> str:
        return str(self.value)
