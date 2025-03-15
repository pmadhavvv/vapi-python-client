from enum import Enum


class AssistantCustomEndpointingRuleType(str, Enum):
    ASSISTANT = "assistant"

    def __str__(self) -> str:
        return str(self.value)
