from enum import Enum


class ClientMessageConversationUpdateType(str, Enum):
    CONVERSATION_UPDATE = "conversation-update"

    def __str__(self) -> str:
        return str(self.value)
