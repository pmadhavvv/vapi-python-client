from enum import Enum


class GroqModelModel(str, Enum):
    DEEPSEEK_R1_DISTILL_LLAMA_70B = "deepseek-r1-distill-llama-70b"
    GEMMA2_9B_IT = "gemma2-9b-it"
    LLAMA3_70B_8192 = "llama3-70b-8192"
    LLAMA3_8B_8192 = "llama3-8b-8192"
    LLAMA_3_1_405B_REASONING = "llama-3.1-405b-reasoning"
    LLAMA_3_1_70B_VERSATILE = "llama-3.1-70b-versatile"
    LLAMA_3_1_8B_INSTANT = "llama-3.1-8b-instant"
    LLAMA_3_3_70B_VERSATILE = "llama-3.3-70b-versatile"
    MIXTRAL_8X7B_32768 = "mixtral-8x7b-32768"

    def __str__(self) -> str:
        return str(self.value)
