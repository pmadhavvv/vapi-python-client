from enum import Enum


class InflectionAICredentialProvider(str, Enum):
    INFLECTION_AI = "inflection-ai"

    def __str__(self) -> str:
        return str(self.value)
