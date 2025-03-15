from enum import Enum


class CustomLLMCredentialProvider(str, Enum):
    CUSTOM_LLM = "custom-llm"

    def __str__(self) -> str:
        return str(self.value)
