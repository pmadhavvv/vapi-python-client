from enum import Enum


class InflectionAIModelProvider(str, Enum):
    INFLECTION_AI = "inflection-ai"

    def __str__(self) -> str:
        return str(self.value)
