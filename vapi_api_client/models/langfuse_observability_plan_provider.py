from enum import Enum


class LangfuseObservabilityPlanProvider(str, Enum):
    LANGFUSE = "langfuse"

    def __str__(self) -> str:
        return str(self.value)
