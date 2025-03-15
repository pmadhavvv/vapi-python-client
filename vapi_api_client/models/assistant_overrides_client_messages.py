from enum import Enum


class AssistantOverridesClientMessages(str, Enum):
    CONVERSATION_UPDATE = "conversation-update"
    FUNCTION_CALL = "function-call"
    FUNCTION_CALL_RESULT = "function-call-result"
    HANG = "hang"
    LANGUAGE_CHANGED = "language-changed"
    METADATA = "metadata"
    MODEL_OUTPUT = "model-output"
    SPEECH_UPDATE = "speech-update"
    STATUS_UPDATE = "status-update"
    TOOL_CALLS = "tool-calls"
    TOOL_CALLS_RESULT = "tool-calls-result"
    TRANSCRIPT = "transcript"
    TRANSFER_UPDATE = "transfer-update"
    USER_INTERRUPTED = "user-interrupted"
    VOICE_INPUT = "voice-input"

    def __str__(self) -> str:
        return str(self.value)
