from enum import Enum


class AzureOpenAICredentialModels(str, Enum):
    GPT_35_TURBO_0125 = "gpt-35-turbo-0125"
    GPT_35_TURBO_1106 = "gpt-35-turbo-1106"
    GPT_4O_2024_05_13 = "gpt-4o-2024-05-13"
    GPT_4O_2024_08_06 = "gpt-4o-2024-08-06"
    GPT_4O_MINI_2024_07_18 = "gpt-4o-mini-2024-07-18"
    GPT_4_0125_PREVIEW = "gpt-4-0125-preview"
    GPT_4_0613 = "gpt-4-0613"
    GPT_4_1106_PREVIEW = "gpt-4-1106-preview"
    GPT_4_TURBO_2024_04_09 = "gpt-4-turbo-2024-04-09"

    def __str__(self) -> str:
        return str(self.value)
