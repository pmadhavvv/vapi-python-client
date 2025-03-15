from enum import Enum


class CerebrasModelModel(str, Enum):
    LLAMA3_1_8B = "llama3.1-8b"
    LLAMA_3_3_70B = "llama-3.3-70b"

    def __str__(self) -> str:
        return str(self.value)
