from enum import Enum


class TrieveKnowledgeBaseCreateType(str, Enum):
    CREATE = "create"

    def __str__(self) -> str:
        return str(self.value)
