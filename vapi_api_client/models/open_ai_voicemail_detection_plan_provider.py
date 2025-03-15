from enum import Enum


class OpenAIVoicemailDetectionPlanProvider(str, Enum):
    OPENAI = "openai"

    def __str__(self) -> str:
        return str(self.value)
