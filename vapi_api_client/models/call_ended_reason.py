from enum import Enum


class CallEndedReason(str, Enum):
    ASSISTANT_ENDED_CALL = "assistant-ended-call"
    ASSISTANT_ENDED_CALL_WITH_HANGUP_TASK = "assistant-ended-call-with-hangup-task"
    ASSISTANT_FORWARDED_CALL = "assistant-forwarded-call"
    ASSISTANT_JOIN_TIMED_OUT = "assistant-join-timed-out"
    ASSISTANT_NOT_FOUND = "assistant-not-found"
    ASSISTANT_NOT_PROVIDED = "assistant-not-provided"
    ASSISTANT_NOT_VALID = "assistant-not-valid"
    ASSISTANT_REQUEST_FAILED = "assistant-request-failed"
    ASSISTANT_REQUEST_RETURNED_ERROR = "assistant-request-returned-error"
    ASSISTANT_REQUEST_RETURNED_FORWARDING_PHONE_NUMBER = "assistant-request-returned-forwarding-phone-number"
    ASSISTANT_REQUEST_RETURNED_INVALID_ASSISTANT = "assistant-request-returned-invalid-assistant"
    ASSISTANT_REQUEST_RETURNED_NO_ASSISTANT = "assistant-request-returned-no-assistant"
    ASSISTANT_REQUEST_RETURNED_UNSPEAKABLE_ERROR = "assistant-request-returned-unspeakable-error"
    ASSISTANT_SAID_END_CALL_PHRASE = "assistant-said-end-call-phrase"
    ASSISTANT_SAID_MESSAGE_WITH_END_CALL_ENABLED = "assistant-said-message-with-end-call-enabled"
    CALL_START_ERROR_NEITHER_ASSISTANT_NOR_SERVER_SET = "call-start-error-neither-assistant-nor-server-set"
    CUSTOMER_BUSY = "customer-busy"
    CUSTOMER_DID_NOT_ANSWER = "customer-did-not-answer"
    CUSTOMER_DID_NOT_GIVE_MICROPHONE_PERMISSION = "customer-did-not-give-microphone-permission"
    CUSTOMER_ENDED_CALL = "customer-ended-call"
    DB_ERROR = "db-error"
    EXCEEDED_MAX_DURATION = "exceeded-max-duration"
    LICENSE_CHECK_FAILED = "license-check-failed"
    MANUALLY_CANCELED = "manually-canceled"
    PHONE_CALL_PROVIDER_BYPASS_ENABLED_BUT_NO_CALL_RECEIVED = "phone-call-provider-bypass-enabled-but-no-call-received"
    PHONE_CALL_PROVIDER_CLOSED_WEBSOCKET = "phone-call-provider-closed-websocket"
    PIPELINE_ERROR_11LABS_TRANSCRIBER_FAILED = "pipeline-error-11labs-transcriber-failed"
    PIPELINE_ERROR_ANTHROPIC_400_BAD_REQUEST_VALIDATION_FAILED = (
        "pipeline-error-anthropic-400-bad-request-validation-failed"
    )
    PIPELINE_ERROR_ANTHROPIC_401_UNAUTHORIZED = "pipeline-error-anthropic-401-unauthorized"
    PIPELINE_ERROR_ANTHROPIC_403_MODEL_ACCESS_DENIED = "pipeline-error-anthropic-403-model-access-denied"
    PIPELINE_ERROR_ANTHROPIC_429_EXCEEDED_QUOTA = "pipeline-error-anthropic-429-exceeded-quota"
    PIPELINE_ERROR_ANTHROPIC_500_SERVER_ERROR = "pipeline-error-anthropic-500-server-error"
    PIPELINE_ERROR_ANTHROPIC_LLM_FAILED = "pipeline-error-anthropic-llm-failed"
    PIPELINE_ERROR_ANYSCALE_400_BAD_REQUEST_VALIDATION_FAILED = (
        "pipeline-error-anyscale-400-bad-request-validation-failed"
    )
    PIPELINE_ERROR_ANYSCALE_401_UNAUTHORIZED = "pipeline-error-anyscale-401-unauthorized"
    PIPELINE_ERROR_ANYSCALE_403_MODEL_ACCESS_DENIED = "pipeline-error-anyscale-403-model-access-denied"
    PIPELINE_ERROR_ANYSCALE_429_EXCEEDED_QUOTA = "pipeline-error-anyscale-429-exceeded-quota"
    PIPELINE_ERROR_ANYSCALE_500_SERVER_ERROR = "pipeline-error-anyscale-500-server-error"
    PIPELINE_ERROR_ANYSCALE_LLM_FAILED = "pipeline-error-anyscale-llm-failed"
    PIPELINE_ERROR_ASSEMBLY_AI_TRANSCRIBER_FAILED = "pipeline-error-assembly-ai-transcriber-failed"
    PIPELINE_ERROR_AZURE_OPENAI_400_BAD_REQUEST_VALIDATION_FAILED = (
        "pipeline-error-azure-openai-400-bad-request-validation-failed"
    )
    PIPELINE_ERROR_AZURE_OPENAI_401_UNAUTHORIZED = "pipeline-error-azure-openai-401-unauthorized"
    PIPELINE_ERROR_AZURE_OPENAI_403_MODEL_ACCESS_DENIED = "pipeline-error-azure-openai-403-model-access-denied"
    PIPELINE_ERROR_AZURE_OPENAI_429_EXCEEDED_QUOTA = "pipeline-error-azure-openai-429-exceeded-quota"
    PIPELINE_ERROR_AZURE_OPENAI_500_SERVER_ERROR = "pipeline-error-azure-openai-500-server-error"
    PIPELINE_ERROR_AZURE_OPENAI_LLM_FAILED = "pipeline-error-azure-openai-llm-failed"
    PIPELINE_ERROR_AZURE_SPEECH_TRANSCRIBER_FAILED = "pipeline-error-azure-speech-transcriber-failed"
    PIPELINE_ERROR_AZURE_VOICE_FAILED = "pipeline-error-azure-voice-failed"
    PIPELINE_ERROR_CARTESIA_500_SERVER_ERROR = "pipeline-error-cartesia-500-server-error"
    PIPELINE_ERROR_CARTESIA_503_SERVER_ERROR = "pipeline-error-cartesia-503-server-error"
    PIPELINE_ERROR_CARTESIA_522_SERVER_ERROR = "pipeline-error-cartesia-522-server-error"
    PIPELINE_ERROR_CARTESIA_REQUESTED_PAYMENT = "pipeline-error-cartesia-requested-payment"
    PIPELINE_ERROR_CARTESIA_SOCKET_HANG_UP = "pipeline-error-cartesia-socket-hang-up"
    PIPELINE_ERROR_CARTESIA_VOICE_FAILED = "pipeline-error-cartesia-voice-failed"
    PIPELINE_ERROR_CEREBRAS_400_BAD_REQUEST_VALIDATION_FAILED = (
        "pipeline-error-cerebras-400-bad-request-validation-failed"
    )
    PIPELINE_ERROR_CEREBRAS_401_UNAUTHORIZED = "pipeline-error-cerebras-401-unauthorized"
    PIPELINE_ERROR_CEREBRAS_403_MODEL_ACCESS_DENIED = "pipeline-error-cerebras-403-model-access-denied"
    PIPELINE_ERROR_CEREBRAS_429_EXCEEDED_QUOTA = "pipeline-error-cerebras-429-exceeded-quota"
    PIPELINE_ERROR_CEREBRAS_500_SERVER_ERROR = "pipeline-error-cerebras-500-server-error"
    PIPELINE_ERROR_CEREBRAS_LLM_FAILED = "pipeline-error-cerebras-llm-failed"
    PIPELINE_ERROR_CUSTOM_LLM_400_BAD_REQUEST_VALIDATION_FAILED = (
        "pipeline-error-custom-llm-400-bad-request-validation-failed"
    )
    PIPELINE_ERROR_CUSTOM_LLM_401_UNAUTHORIZED = "pipeline-error-custom-llm-401-unauthorized"
    PIPELINE_ERROR_CUSTOM_LLM_403_MODEL_ACCESS_DENIED = "pipeline-error-custom-llm-403-model-access-denied"
    PIPELINE_ERROR_CUSTOM_LLM_429_EXCEEDED_QUOTA = "pipeline-error-custom-llm-429-exceeded-quota"
    PIPELINE_ERROR_CUSTOM_LLM_500_SERVER_ERROR = "pipeline-error-custom-llm-500-server-error"
    PIPELINE_ERROR_CUSTOM_LLM_LLM_FAILED = "pipeline-error-custom-llm-llm-failed"
    PIPELINE_ERROR_CUSTOM_TRANSCRIBER_FAILED = "pipeline-error-custom-transcriber-failed"
    PIPELINE_ERROR_CUSTOM_VOICE_FAILED = "pipeline-error-custom-voice-failed"
    PIPELINE_ERROR_DEEPGRAM_RETURNING_400_NO_SUCH_MODEL_LANGUAGE_TIER_COMBINATION = (
        "pipeline-error-deepgram-returning-400-no-such-model-language-tier-combination"
    )
    PIPELINE_ERROR_DEEPGRAM_RETURNING_401_INVALID_CREDENTIALS = (
        "pipeline-error-deepgram-returning-401-invalid-credentials"
    )
    PIPELINE_ERROR_DEEPGRAM_RETURNING_403_MODEL_ACCESS_DENIED = (
        "pipeline-error-deepgram-returning-403-model-access-denied"
    )
    PIPELINE_ERROR_DEEPGRAM_RETURNING_404_NOT_FOUND = "pipeline-error-deepgram-returning-404-not-found"
    PIPELINE_ERROR_DEEPGRAM_RETURNING_500_INVALID_JSON = "pipeline-error-deepgram-returning-500-invalid-json"
    PIPELINE_ERROR_DEEPGRAM_RETURNING_502_BAD_GATEWAY_EHOSTUNREACH = (
        "pipeline-error-deepgram-returning-502-bad-gateway-ehostunreach"
    )
    PIPELINE_ERROR_DEEPGRAM_RETURNING_502_NETWORK_ERROR = "pipeline-error-deepgram-returning-502-network-error"
    PIPELINE_ERROR_DEEPGRAM_TRANSCRIBER_FAILED = "pipeline-error-deepgram-transcriber-failed"
    PIPELINE_ERROR_DEEPGRAM_VOICE_FAILED = "pipeline-error-deepgram-voice-failed"
    PIPELINE_ERROR_DEEPINFRA_400_BAD_REQUEST_VALIDATION_FAILED = (
        "pipeline-error-deepinfra-400-bad-request-validation-failed"
    )
    PIPELINE_ERROR_DEEPINFRA_401_UNAUTHORIZED = "pipeline-error-deepinfra-401-unauthorized"
    PIPELINE_ERROR_DEEPINFRA_403_MODEL_ACCESS_DENIED = "pipeline-error-deepinfra-403-model-access-denied"
    PIPELINE_ERROR_DEEPINFRA_429_EXCEEDED_QUOTA = "pipeline-error-deepinfra-429-exceeded-quota"
    PIPELINE_ERROR_DEEPINFRA_500_SERVER_ERROR = "pipeline-error-deepinfra-500-server-error"
    PIPELINE_ERROR_DEEPINFRA_LLM_FAILED = "pipeline-error-deepinfra-llm-failed"
    PIPELINE_ERROR_DEEP_SEEK_400_BAD_REQUEST_VALIDATION_FAILED = (
        "pipeline-error-deep-seek-400-bad-request-validation-failed"
    )
    PIPELINE_ERROR_DEEP_SEEK_401_UNAUTHORIZED = "pipeline-error-deep-seek-401-unauthorized"
    PIPELINE_ERROR_DEEP_SEEK_403_MODEL_ACCESS_DENIED = "pipeline-error-deep-seek-403-model-access-denied"
    PIPELINE_ERROR_DEEP_SEEK_429_EXCEEDED_QUOTA = "pipeline-error-deep-seek-429-exceeded-quota"
    PIPELINE_ERROR_DEEP_SEEK_500_SERVER_ERROR = "pipeline-error-deep-seek-500-server-error"
    PIPELINE_ERROR_DEEP_SEEK_LLM_FAILED = "pipeline-error-deep-seek-llm-failed"
    PIPELINE_ERROR_ELEVEN_LABS_500_SERVER_ERROR = "pipeline-error-eleven-labs-500-server-error"
    PIPELINE_ERROR_ELEVEN_LABS_BLOCKED_ACCOUNT_IN_PROBATION = "pipeline-error-eleven-labs-blocked-account-in-probation"
    PIPELINE_ERROR_ELEVEN_LABS_BLOCKED_CONCURRENT_REQUESTS_AND_REQUESTED_UPGRADE = (
        "pipeline-error-eleven-labs-blocked-concurrent-requests-and-requested-upgrade"
    )
    PIPELINE_ERROR_ELEVEN_LABS_BLOCKED_CONTENT_AGAINST_THEIR_POLICY = (
        "pipeline-error-eleven-labs-blocked-content-against-their-policy"
    )
    PIPELINE_ERROR_ELEVEN_LABS_BLOCKED_FREE_PLAN_AND_REQUESTED_UPGRADE = (
        "pipeline-error-eleven-labs-blocked-free-plan-and-requested-upgrade"
    )
    PIPELINE_ERROR_ELEVEN_LABS_BLOCKED_USING_INSTANT_VOICE_CLONE_AND_REQUESTED_UPGRADE = (
        "pipeline-error-eleven-labs-blocked-using-instant-voice-clone-and-requested-upgrade"
    )
    PIPELINE_ERROR_ELEVEN_LABS_BLOCKED_VOICE_POTENTIALLY_AGAINST_TERMS_OF_SERVICE_AND_AWAITING_VERIFICATION = (
        "pipeline-error-eleven-labs-blocked-voice-potentially-against-terms-of-service-and-awaiting-verification"
    )
    PIPELINE_ERROR_ELEVEN_LABS_INVALID_API_KEY = "pipeline-error-eleven-labs-invalid-api-key"
    PIPELINE_ERROR_ELEVEN_LABS_INVALID_VOICE_SAMPLES = "pipeline-error-eleven-labs-invalid-voice-samples"
    PIPELINE_ERROR_ELEVEN_LABS_MAX_CHARACTER_LIMIT_EXCEEDED = "pipeline-error-eleven-labs-max-character-limit-exceeded"
    PIPELINE_ERROR_ELEVEN_LABS_MISSING_SAMPLES_FOR_VOICE_CLONE = (
        "pipeline-error-eleven-labs-missing-samples-for-voice-clone"
    )
    PIPELINE_ERROR_ELEVEN_LABS_PROFESSIONAL_VOICES_ONLY_FOR_CREATOR_PLUS = (
        "pipeline-error-eleven-labs-professional-voices-only-for-creator-plus"
    )
    PIPELINE_ERROR_ELEVEN_LABS_QUOTA_EXCEEDED = "pipeline-error-eleven-labs-quota-exceeded"
    PIPELINE_ERROR_ELEVEN_LABS_SYSTEM_BUSY_AND_REQUESTED_UPGRADE = (
        "pipeline-error-eleven-labs-system-busy-and-requested-upgrade"
    )
    PIPELINE_ERROR_ELEVEN_LABS_UNAUTHORIZED_ACCESS = "pipeline-error-eleven-labs-unauthorized-access"
    PIPELINE_ERROR_ELEVEN_LABS_UNAUTHORIZED_TO_ACCESS_MODEL = "pipeline-error-eleven-labs-unauthorized-to-access-model"
    PIPELINE_ERROR_ELEVEN_LABS_VOICE_DISABLED_BY_OWNER = "pipeline-error-eleven-labs-voice-disabled-by-owner"
    PIPELINE_ERROR_ELEVEN_LABS_VOICE_FAILED = "pipeline-error-eleven-labs-voice-failed"
    PIPELINE_ERROR_ELEVEN_LABS_VOICE_NOT_ALLOWED_FOR_FREE_USERS = (
        "pipeline-error-eleven-labs-voice-not-allowed-for-free-users"
    )
    PIPELINE_ERROR_ELEVEN_LABS_VOICE_NOT_FINE_TUNED = "pipeline-error-eleven-labs-voice-not-fine-tuned"
    PIPELINE_ERROR_ELEVEN_LABS_VOICE_NOT_FINE_TUNED_AND_CANNOT_BE_USED = (
        "pipeline-error-eleven-labs-voice-not-fine-tuned-and-cannot-be-used"
    )
    PIPELINE_ERROR_ELEVEN_LABS_VOICE_NOT_FOUND = "pipeline-error-eleven-labs-voice-not-found"
    PIPELINE_ERROR_GLADIA_TRANSCRIBER_FAILED = "pipeline-error-gladia-transcriber-failed"
    PIPELINE_ERROR_GOOGLE_400_BAD_REQUEST_VALIDATION_FAILED = "pipeline-error-google-400-bad-request-validation-failed"
    PIPELINE_ERROR_GOOGLE_401_UNAUTHORIZED = "pipeline-error-google-401-unauthorized"
    PIPELINE_ERROR_GOOGLE_403_MODEL_ACCESS_DENIED = "pipeline-error-google-403-model-access-denied"
    PIPELINE_ERROR_GOOGLE_429_EXCEEDED_QUOTA = "pipeline-error-google-429-exceeded-quota"
    PIPELINE_ERROR_GOOGLE_500_SERVER_ERROR = "pipeline-error-google-500-server-error"
    PIPELINE_ERROR_GOOGLE_LLM_FAILED = "pipeline-error-google-llm-failed"
    PIPELINE_ERROR_GOOGLE_TRANSCRIBER_FAILED = "pipeline-error-google-transcriber-failed"
    PIPELINE_ERROR_GROQ_400_BAD_REQUEST_VALIDATION_FAILED = "pipeline-error-groq-400-bad-request-validation-failed"
    PIPELINE_ERROR_GROQ_401_UNAUTHORIZED = "pipeline-error-groq-401-unauthorized"
    PIPELINE_ERROR_GROQ_403_MODEL_ACCESS_DENIED = "pipeline-error-groq-403-model-access-denied"
    PIPELINE_ERROR_GROQ_429_EXCEEDED_QUOTA = "pipeline-error-groq-429-exceeded-quota"
    PIPELINE_ERROR_GROQ_500_SERVER_ERROR = "pipeline-error-groq-500-server-error"
    PIPELINE_ERROR_GROQ_LLM_FAILED = "pipeline-error-groq-llm-failed"
    PIPELINE_ERROR_HUME_VOICE_FAILED = "pipeline-error-hume-voice-failed"
    PIPELINE_ERROR_INFLECTION_AI_400_BAD_REQUEST_VALIDATION_FAILED = (
        "pipeline-error-inflection-ai-400-bad-request-validation-failed"
    )
    PIPELINE_ERROR_INFLECTION_AI_401_UNAUTHORIZED = "pipeline-error-inflection-ai-401-unauthorized"
    PIPELINE_ERROR_INFLECTION_AI_403_MODEL_ACCESS_DENIED = "pipeline-error-inflection-ai-403-model-access-denied"
    PIPELINE_ERROR_INFLECTION_AI_429_EXCEEDED_QUOTA = "pipeline-error-inflection-ai-429-exceeded-quota"
    PIPELINE_ERROR_INFLECTION_AI_500_SERVER_ERROR = "pipeline-error-inflection-ai-500-server-error"
    PIPELINE_ERROR_INFLECTION_AI_LLM_FAILED = "pipeline-error-inflection-ai-llm-failed"
    PIPELINE_ERROR_LMNT_VOICE_FAILED = "pipeline-error-lmnt-voice-failed"
    PIPELINE_ERROR_MISTRAL_400_BAD_REQUEST_VALIDATION_FAILED = (
        "pipeline-error-mistral-400-bad-request-validation-failed"
    )
    PIPELINE_ERROR_MISTRAL_401_UNAUTHORIZED = "pipeline-error-mistral-401-unauthorized"
    PIPELINE_ERROR_MISTRAL_403_MODEL_ACCESS_DENIED = "pipeline-error-mistral-403-model-access-denied"
    PIPELINE_ERROR_MISTRAL_429_EXCEEDED_QUOTA = "pipeline-error-mistral-429-exceeded-quota"
    PIPELINE_ERROR_MISTRAL_500_SERVER_ERROR = "pipeline-error-mistral-500-server-error"
    PIPELINE_ERROR_MISTRAL_LLM_FAILED = "pipeline-error-mistral-llm-failed"
    PIPELINE_ERROR_NEETS_VOICE_FAILED = "pipeline-error-neets-voice-failed"
    PIPELINE_ERROR_NEUPHONIC_VOICE_FAILED = "pipeline-error-neuphonic-voice-failed"
    PIPELINE_ERROR_OPENAI_400_BAD_REQUEST_VALIDATION_FAILED = "pipeline-error-openai-400-bad-request-validation-failed"
    PIPELINE_ERROR_OPENAI_401_UNAUTHORIZED = "pipeline-error-openai-401-unauthorized"
    PIPELINE_ERROR_OPENAI_403_MODEL_ACCESS_DENIED = "pipeline-error-openai-403-model-access-denied"
    PIPELINE_ERROR_OPENAI_429_EXCEEDED_QUOTA = "pipeline-error-openai-429-exceeded-quota"
    PIPELINE_ERROR_OPENAI_500_SERVER_ERROR = "pipeline-error-openai-500-server-error"
    PIPELINE_ERROR_OPENAI_LLM_FAILED = "pipeline-error-openai-llm-failed"
    PIPELINE_ERROR_OPENAI_VOICE_FAILED = "pipeline-error-openai-voice-failed"
    PIPELINE_ERROR_OPENROUTER_400_BAD_REQUEST_VALIDATION_FAILED = (
        "pipeline-error-openrouter-400-bad-request-validation-failed"
    )
    PIPELINE_ERROR_OPENROUTER_401_UNAUTHORIZED = "pipeline-error-openrouter-401-unauthorized"
    PIPELINE_ERROR_OPENROUTER_403_MODEL_ACCESS_DENIED = "pipeline-error-openrouter-403-model-access-denied"
    PIPELINE_ERROR_OPENROUTER_429_EXCEEDED_QUOTA = "pipeline-error-openrouter-429-exceeded-quota"
    PIPELINE_ERROR_OPENROUTER_500_SERVER_ERROR = "pipeline-error-openrouter-500-server-error"
    PIPELINE_ERROR_OPENROUTER_LLM_FAILED = "pipeline-error-openrouter-llm-failed"
    PIPELINE_ERROR_PERPLEXITY_AI_400_BAD_REQUEST_VALIDATION_FAILED = (
        "pipeline-error-perplexity-ai-400-bad-request-validation-failed"
    )
    PIPELINE_ERROR_PERPLEXITY_AI_401_UNAUTHORIZED = "pipeline-error-perplexity-ai-401-unauthorized"
    PIPELINE_ERROR_PERPLEXITY_AI_403_MODEL_ACCESS_DENIED = "pipeline-error-perplexity-ai-403-model-access-denied"
    PIPELINE_ERROR_PERPLEXITY_AI_429_EXCEEDED_QUOTA = "pipeline-error-perplexity-ai-429-exceeded-quota"
    PIPELINE_ERROR_PERPLEXITY_AI_500_SERVER_ERROR = "pipeline-error-perplexity-ai-500-server-error"
    PIPELINE_ERROR_PERPLEXITY_AI_LLM_FAILED = "pipeline-error-perplexity-ai-llm-failed"
    PIPELINE_ERROR_PLAYHT_401_UNAUTHORIZED = "pipeline-error-playht-401-unauthorized"
    PIPELINE_ERROR_PLAYHT_403_FORBIDDEN_API_ACCESS_NOT_AVAILABLE = (
        "pipeline-error-playht-403-forbidden-api-access-not-available"
    )
    PIPELINE_ERROR_PLAYHT_403_FORBIDDEN_OUT_OF_CHARACTERS = "pipeline-error-playht-403-forbidden-out-of-characters"
    PIPELINE_ERROR_PLAYHT_429_EXCEEDED_QUOTA = "pipeline-error-playht-429-exceeded-quota"
    PIPELINE_ERROR_PLAYHT_502_GATEWAY_ERROR = "pipeline-error-playht-502-gateway-error"
    PIPELINE_ERROR_PLAYHT_504_GATEWAY_ERROR = "pipeline-error-playht-504-gateway-error"
    PIPELINE_ERROR_PLAYHT_INVALID_EMOTION = "pipeline-error-playht-invalid-emotion"
    PIPELINE_ERROR_PLAYHT_INVALID_VOICE = "pipeline-error-playht-invalid-voice"
    PIPELINE_ERROR_PLAYHT_OUT_OF_CREDITS = "pipeline-error-playht-out-of-credits"
    PIPELINE_ERROR_PLAYHT_REQUEST_TIMED_OUT = "pipeline-error-playht-request-timed-out"
    PIPELINE_ERROR_PLAYHT_UNEXPECTED_ERROR = "pipeline-error-playht-unexpected-error"
    PIPELINE_ERROR_PLAYHT_VOICE_FAILED = "pipeline-error-playht-voice-failed"
    PIPELINE_ERROR_PLAYHT_VOICE_MUST_BE_A_VALID_VOICE_MANIFEST_URI = (
        "pipeline-error-playht-voice-must-be-a-valid-voice-manifest-uri"
    )
    PIPELINE_ERROR_RIME_AI_VOICE_FAILED = "pipeline-error-rime-ai-voice-failed"
    PIPELINE_ERROR_RUNPOD_400_BAD_REQUEST_VALIDATION_FAILED = "pipeline-error-runpod-400-bad-request-validation-failed"
    PIPELINE_ERROR_RUNPOD_401_UNAUTHORIZED = "pipeline-error-runpod-401-unauthorized"
    PIPELINE_ERROR_RUNPOD_403_MODEL_ACCESS_DENIED = "pipeline-error-runpod-403-model-access-denied"
    PIPELINE_ERROR_RUNPOD_429_EXCEEDED_QUOTA = "pipeline-error-runpod-429-exceeded-quota"
    PIPELINE_ERROR_RUNPOD_500_SERVER_ERROR = "pipeline-error-runpod-500-server-error"
    PIPELINE_ERROR_RUNPOD_LLM_FAILED = "pipeline-error-runpod-llm-failed"
    PIPELINE_ERROR_SMALLEST_AI_VOICE_FAILED = "pipeline-error-smallest-ai-voice-failed"
    PIPELINE_ERROR_SPEECHMATICS_TRANSCRIBER_FAILED = "pipeline-error-speechmatics-transcriber-failed"
    PIPELINE_ERROR_TALKSCRIBER_TRANSCRIBER_FAILED = "pipeline-error-talkscriber-transcriber-failed"
    PIPELINE_ERROR_TAVUS_VIDEO_FAILED = "pipeline-error-tavus-video-failed"
    PIPELINE_ERROR_TOGETHER_AI_400_BAD_REQUEST_VALIDATION_FAILED = (
        "pipeline-error-together-ai-400-bad-request-validation-failed"
    )
    PIPELINE_ERROR_TOGETHER_AI_401_UNAUTHORIZED = "pipeline-error-together-ai-401-unauthorized"
    PIPELINE_ERROR_TOGETHER_AI_403_MODEL_ACCESS_DENIED = "pipeline-error-together-ai-403-model-access-denied"
    PIPELINE_ERROR_TOGETHER_AI_429_EXCEEDED_QUOTA = "pipeline-error-together-ai-429-exceeded-quota"
    PIPELINE_ERROR_TOGETHER_AI_500_SERVER_ERROR = "pipeline-error-together-ai-500-server-error"
    PIPELINE_ERROR_TOGETHER_AI_LLM_FAILED = "pipeline-error-together-ai-llm-failed"
    PIPELINE_ERROR_VAPI_400_BAD_REQUEST_VALIDATION_FAILED = "pipeline-error-vapi-400-bad-request-validation-failed"
    PIPELINE_ERROR_VAPI_401_UNAUTHORIZED = "pipeline-error-vapi-401-unauthorized"
    PIPELINE_ERROR_VAPI_403_MODEL_ACCESS_DENIED = "pipeline-error-vapi-403-model-access-denied"
    PIPELINE_ERROR_VAPI_429_EXCEEDED_QUOTA = "pipeline-error-vapi-429-exceeded-quota"
    PIPELINE_ERROR_VAPI_500_SERVER_ERROR = "pipeline-error-vapi-500-server-error"
    PIPELINE_ERROR_VAPI_LLM_FAILED = "pipeline-error-vapi-llm-failed"
    PIPELINE_ERROR_XAI_400_BAD_REQUEST_VALIDATION_FAILED = "pipeline-error-xai-400-bad-request-validation-failed"
    PIPELINE_ERROR_XAI_401_UNAUTHORIZED = "pipeline-error-xai-401-unauthorized"
    PIPELINE_ERROR_XAI_403_MODEL_ACCESS_DENIED = "pipeline-error-xai-403-model-access-denied"
    PIPELINE_ERROR_XAI_429_EXCEEDED_QUOTA = "pipeline-error-xai-429-exceeded-quota"
    PIPELINE_ERROR_XAI_500_SERVER_ERROR = "pipeline-error-xai-500-server-error"
    PIPELINE_ERROR_XAI_LLM_FAILED = "pipeline-error-xai-llm-failed"
    PIPELINE_NO_AVAILABLE_MODEL = "pipeline-no-available-model"
    SILENCE_TIMED_OUT = "silence-timed-out"
    SIP_GATEWAY_FAILED_TO_CONNECT_CALL = "sip-gateway-failed-to-connect-call"
    TWILIO_FAILED_TO_CONNECT_CALL = "twilio-failed-to-connect-call"
    TWILIO_REPORTED_CUSTOMER_MISDIALED = "twilio-reported-customer-misdialed"
    UNKNOWN_ERROR = "unknown-error"
    VAPIFAULT_CALL_STARTED_BUT_CONNECTION_TO_TRANSPORT_MISSING = (
        "vapifault-call-started-but-connection-to-transport-missing"
    )
    VAPIFAULT_PHONE_CALL_WORKER_COULD_NOT_FIND_CALL = "vapifault-phone-call-worker-could-not-find-call"
    VAPIFAULT_PHONE_CALL_WORKER_SETUP_SOCKET_ERROR = "vapifault-phone-call-worker-setup-socket-error"
    VAPIFAULT_PHONE_CALL_WORKER_WORKER_SETUP_SOCKET_TIMEOUT = "vapifault-phone-call-worker-worker-setup-socket-timeout"
    VAPIFAULT_TRANSPORT_CONNECTED_BUT_CALL_NOT_ACTIVE = "vapifault-transport-connected-but-call-not-active"
    VAPIFAULT_TRANSPORT_NEVER_CONNECTED = "vapifault-transport-never-connected"
    VAPIFAULT_WEB_CALL_WORKER_SETUP_FAILED = "vapifault-web-call-worker-setup-failed"
    VOICEMAIL = "voicemail"
    VONAGE_COMPLETED = "vonage-completed"
    VONAGE_DISCONNECTED = "vonage-disconnected"
    VONAGE_FAILED_TO_CONNECT_CALL = "vonage-failed-to-connect-call"
    VONAGE_REJECTED = "vonage-rejected"
    WORKER_SHUTDOWN = "worker-shutdown"

    def __str__(self) -> str:
        return str(self.value)
