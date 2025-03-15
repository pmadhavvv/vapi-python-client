from enum import Enum


class CustomLLMModelProvider(str, Enum):
    CUSTOM_LLM = "custom-llm"

    def __str__(self) -> str:
        return str(self.value)
