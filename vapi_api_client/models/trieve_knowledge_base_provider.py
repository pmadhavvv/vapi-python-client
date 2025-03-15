from enum import Enum


class TrieveKnowledgeBaseProvider(str, Enum):
    TRIEVE = "trieve"

    def __str__(self) -> str:
        return str(self.value)
