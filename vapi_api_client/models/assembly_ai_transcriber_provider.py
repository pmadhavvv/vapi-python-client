from enum import Enum


class AssemblyAITranscriberProvider(str, Enum):
    ASSEMBLY_AI = "assembly-ai"

    def __str__(self) -> str:
        return str(self.value)
