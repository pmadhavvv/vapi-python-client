from enum import Enum


class ClientInboundMessageControlControl(str, Enum):
    MUTE_ASSISTANT = "mute-assistant"
    SAY_FIRST_MESSAGE = "say-first-message"
    UNMUTE_ASSISTANT = "unmute-assistant"

    def __str__(self) -> str:
        return str(self.value)
