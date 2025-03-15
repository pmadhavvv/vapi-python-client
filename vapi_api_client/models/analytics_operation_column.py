from enum import Enum


class AnalyticsOperationColumn(str, Enum):
    CONCURRENCY = "concurrency"
    COST = "cost"
    COSTBREAKDOWN_LLM = "costBreakdown.llm"
    COSTBREAKDOWN_LLMCOMPLETIONTOKENS = "costBreakdown.llmCompletionTokens"
    COSTBREAKDOWN_LLMPROMPTTOKENS = "costBreakdown.llmPromptTokens"
    COSTBREAKDOWN_STT = "costBreakdown.stt"
    COSTBREAKDOWN_TTS = "costBreakdown.tts"
    COSTBREAKDOWN_TTSCHARACTERS = "costBreakdown.ttsCharacters"
    COSTBREAKDOWN_VAPI = "costBreakdown.vapi"
    DURATION = "duration"
    ID = "id"
    MINUTESUSED = "minutesUsed"

    def __str__(self) -> str:
        return str(self.value)
