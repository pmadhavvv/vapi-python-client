from enum import Enum


class CreateAssistantDTOServerMessages(str, Enum):
    CONVERSATION_UPDATE = "conversation-update"
    END_OF_CALL_REPORT = "end-of-call-report"
    FUNCTION_CALL = "function-call"
    HANG = "hang"
    LANGUAGE_CHANGED = "language-changed"
    LANGUAGE_CHANGE_DETECTED = "language-change-detected"
    MODEL_OUTPUT = "model-output"
    PHONE_CALL_CONTROL = "phone-call-control"
    SPEECH_UPDATE = "speech-update"
    STATUS_UPDATE = "status-update"
    TOOL_CALLS = "tool-calls"
    TRANSCRIPT = "transcript"
    TRANSCRIPTTRANSCRIPTTYPEFINAL = 'transcript[transcriptType="final"]'
    TRANSFER_DESTINATION_REQUEST = "transfer-destination-request"
    TRANSFER_UPDATE = "transfer-update"
    USER_INTERRUPTED = "user-interrupted"
    VOICE_INPUT = "voice-input"

    def __str__(self) -> str:
        return str(self.value)
