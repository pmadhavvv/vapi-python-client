from enum import Enum


class AssistantOverridesFirstMessageMode(str, Enum):
    ASSISTANT_SPEAKS_FIRST = "assistant-speaks-first"
    ASSISTANT_SPEAKS_FIRST_WITH_MODEL_GENERATED_MESSAGE = "assistant-speaks-first-with-model-generated-message"
    ASSISTANT_WAITS_FOR_USER = "assistant-waits-for-user"

    def __str__(self) -> str:
        return str(self.value)
