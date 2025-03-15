from enum import Enum


class GoogleModelModel(str, Enum):
    GEMINI_1_0_PRO = "gemini-1.0-pro"
    GEMINI_1_5_FLASH = "gemini-1.5-flash"
    GEMINI_1_5_FLASH_002 = "gemini-1.5-flash-002"
    GEMINI_1_5_PRO = "gemini-1.5-pro"
    GEMINI_1_5_PRO_002 = "gemini-1.5-pro-002"
    GEMINI_2_0_FLASH = "gemini-2.0-flash"
    GEMINI_2_0_FLASH_EXP = "gemini-2.0-flash-exp"
    GEMINI_2_0_FLASH_LITE = "gemini-2.0-flash-lite"
    GEMINI_2_0_FLASH_LITE_PREVIEW_02_05 = "gemini-2.0-flash-lite-preview-02-05"
    GEMINI_2_0_FLASH_REALTIME_EXP = "gemini-2.0-flash-realtime-exp"
    GEMINI_2_0_FLASH_THINKING_EXP = "gemini-2.0-flash-thinking-exp"
    GEMINI_2_0_PRO_EXP_02_05 = "gemini-2.0-pro-exp-02-05"

    def __str__(self) -> str:
        return str(self.value)
