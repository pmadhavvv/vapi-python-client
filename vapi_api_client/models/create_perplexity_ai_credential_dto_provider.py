from enum import Enum


class CreatePerplexityAICredentialDTOProvider(str, Enum):
    PERPLEXITY_AI = "perplexity-ai"

    def __str__(self) -> str:
        return str(self.value)
