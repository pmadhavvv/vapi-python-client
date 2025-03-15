from enum import Enum


class ServerMessageConversationUpdateType(str, Enum):
    CONVERSATION_UPDATE = "conversation-update"

    def __str__(self) -> str:
        return str(self.value)
