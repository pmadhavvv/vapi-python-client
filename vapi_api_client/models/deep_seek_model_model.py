from enum import Enum


class DeepSeekModelModel(str, Enum):
    DEEPSEEK_CHAT = "deepseek-chat"
    DEEPSEEK_REASONER = "deepseek-reasoner"

    def __str__(self) -> str:
        return str(self.value)
