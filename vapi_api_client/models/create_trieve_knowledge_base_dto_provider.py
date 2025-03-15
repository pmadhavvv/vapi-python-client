from enum import Enum


class CreateTrieveKnowledgeBaseDTOProvider(str, Enum):
    TRIEVE = "trieve"

    def __str__(self) -> str:
        return str(self.value)
