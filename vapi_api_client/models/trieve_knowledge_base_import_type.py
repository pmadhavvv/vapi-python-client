from enum import Enum


class TrieveKnowledgeBaseImportType(str, Enum):
    IMPORT = "import"

    def __str__(self) -> str:
        return str(self.value)
