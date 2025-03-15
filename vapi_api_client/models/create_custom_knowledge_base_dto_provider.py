from enum import Enum


class CreateCustomKnowledgeBaseDTOProvider(str, Enum):
    CUSTOM_KNOWLEDGE_BASE = "custom-knowledge-base"

    def __str__(self) -> str:
        return str(self.value)
