from enum import Enum


class CreateAssemblyAICredentialDTOProvider(str, Enum):
    ASSEMBLY_AI = "assembly-ai"

    def __str__(self) -> str:
        return str(self.value)
