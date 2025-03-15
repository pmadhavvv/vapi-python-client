from enum import Enum


class ServerMessageKnowledgeBaseRequestType(str, Enum):
    KNOWLEDGE_BASE_REQUEST = "knowledge-base-request"

    def __str__(self) -> str:
        return str(self.value)
