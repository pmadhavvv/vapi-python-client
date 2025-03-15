from enum import Enum


class InflectionAIModelModel(str, Enum):
    INFLECTION_3_PI = "inflection_3_pi"

    def __str__(self) -> str:
        return str(self.value)
