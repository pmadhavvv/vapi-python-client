from enum import Enum


class LogResource(str, Enum):
    ANALYTICS = "analytics"
    ASSISTANT = "assistant"
    BLOCK = "block"
    CALL = "call"
    CREDENTIAL = "credential"
    FILE = "file"
    LOG = "log"
    METRIC = "metric"
    ORG = "org"
    PHONE_NUMBER = "phone-number"
    PROVIDER = "provider"
    SQUAD = "squad"
    TEMPLATE = "template"
    TOKEN = "token"
    TOOL = "tool"
    VOICE_LIBRARY = "voice-library"

    def __str__(self) -> str:
        return str(self.value)
