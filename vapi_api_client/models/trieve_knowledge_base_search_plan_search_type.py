from enum import Enum


class TrieveKnowledgeBaseSearchPlanSearchType(str, Enum):
    BM25 = "bm25"
    FULLTEXT = "fulltext"
    HYBRID = "hybrid"
    SEMANTIC = "semantic"

    def __str__(self) -> str:
        return str(self.value)
