from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_assistant_dto_background_sound import CreateAssistantDTOBackgroundSound
from ..models.create_assistant_dto_client_messages_item import CreateAssistantDTOClientMessagesItem
from ..models.create_assistant_dto_first_message_mode import CreateAssistantDTOFirstMessageMode
from ..models.create_assistant_dto_server_messages_item import CreateAssistantDTOServerMessagesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analysis_plan import AnalysisPlan
    from ..models.anthropic_model import AnthropicModel
    from ..models.anyscale_model import AnyscaleModel
    from ..models.artifact_plan import ArtifactPlan
    from ..models.assembly_ai_transcriber import AssemblyAITranscriber
    from ..models.assistant_hooks import AssistantHooks
    from ..models.azure_speech_transcriber import AzureSpeechTranscriber
    from ..models.azure_voice import AzureVoice
    from ..models.cartesia_voice import CartesiaVoice
    from ..models.cerebras_model import CerebrasModel
    from ..models.compliance_plan import CompliancePlan
    from ..models.create_anthropic_credential_dto import CreateAnthropicCredentialDTO
    from ..models.create_anyscale_credential_dto import CreateAnyscaleCredentialDTO
    from ..models.create_assembly_ai_credential_dto import CreateAssemblyAICredentialDTO
    from ..models.create_assistant_dto_metadata import CreateAssistantDTOMetadata
    from ..models.create_azure_credential_dto import CreateAzureCredentialDTO
    from ..models.create_azure_open_ai_credential_dto import CreateAzureOpenAICredentialDTO
    from ..models.create_byo_sip_trunk_credential_dto import CreateByoSipTrunkCredentialDTO
    from ..models.create_cartesia_credential_dto import CreateCartesiaCredentialDTO
    from ..models.create_cerebras_credential_dto import CreateCerebrasCredentialDTO
    from ..models.create_cloudflare_credential_dto import CreateCloudflareCredentialDTO
    from ..models.create_custom_llm_credential_dto import CreateCustomLLMCredentialDTO
    from ..models.create_deep_infra_credential_dto import CreateDeepInfraCredentialDTO
    from ..models.create_deep_seek_credential_dto import CreateDeepSeekCredentialDTO
    from ..models.create_deepgram_credential_dto import CreateDeepgramCredentialDTO
    from ..models.create_eleven_labs_credential_dto import CreateElevenLabsCredentialDTO
    from ..models.create_gcp_credential_dto import CreateGcpCredentialDTO
    from ..models.create_gladia_credential_dto import CreateGladiaCredentialDTO
    from ..models.create_go_high_level_credential_dto import CreateGoHighLevelCredentialDTO
    from ..models.create_google_credential_dto import CreateGoogleCredentialDTO
    from ..models.create_groq_credential_dto import CreateGroqCredentialDTO
    from ..models.create_hume_credential_dto import CreateHumeCredentialDTO
    from ..models.create_inflection_ai_credential_dto import CreateInflectionAICredentialDTO
    from ..models.create_langfuse_credential_dto import CreateLangfuseCredentialDTO
    from ..models.create_lmnt_credential_dto import CreateLmntCredentialDTO
    from ..models.create_make_credential_dto import CreateMakeCredentialDTO
    from ..models.create_mistral_credential_dto import CreateMistralCredentialDTO
    from ..models.create_neuphonic_credential_dto import CreateNeuphonicCredentialDTO
    from ..models.create_open_ai_credential_dto import CreateOpenAICredentialDTO
    from ..models.create_open_router_credential_dto import CreateOpenRouterCredentialDTO
    from ..models.create_perplexity_ai_credential_dto import CreatePerplexityAICredentialDTO
    from ..models.create_play_ht_credential_dto import CreatePlayHTCredentialDTO
    from ..models.create_rime_ai_credential_dto import CreateRimeAICredentialDTO
    from ..models.create_runpod_credential_dto import CreateRunpodCredentialDTO
    from ..models.create_s3_credential_dto import CreateS3CredentialDTO
    from ..models.create_smallest_ai_credential_dto import CreateSmallestAICredentialDTO
    from ..models.create_speechmatics_credential_dto import CreateSpeechmaticsCredentialDTO
    from ..models.create_supabase_credential_dto import CreateSupabaseCredentialDTO
    from ..models.create_tavus_credential_dto import CreateTavusCredentialDTO
    from ..models.create_together_ai_credential_dto import CreateTogetherAICredentialDTO
    from ..models.create_trieve_credential_dto import CreateTrieveCredentialDTO
    from ..models.create_twilio_credential_dto import CreateTwilioCredentialDTO
    from ..models.create_vonage_credential_dto import CreateVonageCredentialDTO
    from ..models.create_webhook_credential_dto import CreateWebhookCredentialDTO
    from ..models.create_x_ai_credential_dto import CreateXAiCredentialDTO
    from ..models.custom_llm_model import CustomLLMModel
    from ..models.custom_transcriber import CustomTranscriber
    from ..models.custom_voice import CustomVoice
    from ..models.deep_infra_model import DeepInfraModel
    from ..models.deep_seek_model import DeepSeekModel
    from ..models.deepgram_transcriber import DeepgramTranscriber
    from ..models.deepgram_voice import DeepgramVoice
    from ..models.eleven_labs_transcriber import ElevenLabsTranscriber
    from ..models.eleven_labs_voice import ElevenLabsVoice
    from ..models.gladia_transcriber import GladiaTranscriber
    from ..models.google_model import GoogleModel
    from ..models.google_voicemail_detection_plan import GoogleVoicemailDetectionPlan
    from ..models.groq_model import GroqModel
    from ..models.hume_voice import HumeVoice
    from ..models.inflection_ai_model import InflectionAIModel
    from ..models.keypad_input_plan import KeypadInputPlan
    from ..models.langfuse_observability_plan import LangfuseObservabilityPlan
    from ..models.lmnt_voice import LMNTVoice
    from ..models.message_plan import MessagePlan
    from ..models.monitor_plan import MonitorPlan
    from ..models.neets_voice import NeetsVoice
    from ..models.neuphonic_voice import NeuphonicVoice
    from ..models.open_ai_model import OpenAIModel
    from ..models.open_ai_voice import OpenAIVoice
    from ..models.open_ai_voicemail_detection_plan import OpenAIVoicemailDetectionPlan
    from ..models.open_router_model import OpenRouterModel
    from ..models.perplexity_ai_model import PerplexityAIModel
    from ..models.play_ht_voice import PlayHTVoice
    from ..models.rime_ai_voice import RimeAIVoice
    from ..models.server import Server
    from ..models.smallest_ai_voice import SmallestAIVoice
    from ..models.speechmatics_transcriber import SpeechmaticsTranscriber
    from ..models.start_speaking_plan import StartSpeakingPlan
    from ..models.stop_speaking_plan import StopSpeakingPlan
    from ..models.talkscriber_transcriber import TalkscriberTranscriber
    from ..models.tavus_voice import TavusVoice
    from ..models.together_ai_model import TogetherAIModel
    from ..models.transport_configuration_twilio import TransportConfigurationTwilio
    from ..models.twilio_voicemail_detection_plan import TwilioVoicemailDetectionPlan
    from ..models.vapi_model import VapiModel
    from ..models.vapi_voice import VapiVoice
    from ..models.xai_model import XaiModel


T = TypeVar("T", bound="CreateAssistantDTO")


@_attrs_define
class CreateAssistantDTO:
    """
    Attributes:
        transcriber (Union['AssemblyAITranscriber', 'AzureSpeechTranscriber', 'CustomTranscriber',
            'DeepgramTranscriber', 'ElevenLabsTranscriber', 'GladiaTranscriber', 'SpeechmaticsTranscriber',
            'TalkscriberTranscriber', Unset]): These are the options for the assistant's transcriber.
        model (Union['AnthropicModel', 'AnyscaleModel', 'CerebrasModel', 'CustomLLMModel', 'DeepInfraModel',
            'DeepSeekModel', 'GoogleModel', 'GroqModel', 'InflectionAIModel', 'OpenAIModel', 'OpenRouterModel',
            'PerplexityAIModel', 'TogetherAIModel', 'VapiModel', 'XaiModel', Unset]): These are the options for the
            assistant's LLM.
        voice (Union['AzureVoice', 'CartesiaVoice', 'CustomVoice', 'DeepgramVoice', 'ElevenLabsVoice', 'HumeVoice',
            'LMNTVoice', 'NeetsVoice', 'NeuphonicVoice', 'OpenAIVoice', 'PlayHTVoice', 'RimeAIVoice', 'SmallestAIVoice',
            'TavusVoice', 'VapiVoice', Unset]): These are the options for the assistant's voice.
        first_message (Union[Unset, str]): This is the first message that the assistant will say. This can also be a URL
            to a containerized audio file (mp3, wav, etc.).

            If unspecified, assistant will wait for user to speak and use the model to respond once they speak. Example:
            Hello! How can I help you today?.
        first_message_mode (Union[Unset, CreateAssistantDTOFirstMessageMode]): This is the mode for the first message.
            Default is 'assistant-speaks-first'.

            Use:
            - 'assistant-speaks-first' to have the assistant speak first.
            - 'assistant-waits-for-user' to have the assistant wait for the user to speak first.
            - 'assistant-speaks-first-with-model-generated-message' to have the assistant speak first with a message
            generated by the model based on the conversation state. (`assistant.model.messages` at call start,
            `call.messages` at squad transfer points).

            @default 'assistant-speaks-first' Example: assistant-speaks-first.
        voicemail_detection (Union['GoogleVoicemailDetectionPlan', 'OpenAIVoicemailDetectionPlan',
            'TwilioVoicemailDetectionPlan', Unset]): These are the settings to configure or disable voicemail detection.
            Alternatively, voicemail detection can be configured using the model.tools=[VoicemailTool].
            This uses Twilio's built-in detection while the VoicemailTool relies on the model to detect if a voicemail was
            reached.
            You can use neither of them, one of them, or both of them. By default, Twilio built-in detection is enabled
            while VoicemailTool is not.
        client_messages (Union[Unset, list[CreateAssistantDTOClientMessagesItem]]): These are the messages that will be
            sent to your Client SDKs. Default is conversation-update,function-call,hang,model-output,speech-update,status-
            update,transfer-update,transcript,tool-calls,user-interrupted,voice-input. You can check the shape of the
            messages in ClientMessage schema. Example: ['conversation-update', 'function-call', 'hang', 'model-output',
            'speech-update', 'status-update', 'transfer-update', 'transcript', 'tool-calls', 'user-interrupted', 'voice-
            input'].
        server_messages (Union[Unset, list[CreateAssistantDTOServerMessagesItem]]): These are the messages that will be
            sent to your Server URL. Default is conversation-update,end-of-call-report,function-call,hang,speech-
            update,status-update,tool-calls,transfer-destination-request,user-interrupted. You can check the shape of the
            messages in ServerMessage schema. Example: ['conversation-update', 'end-of-call-report', 'function-call',
            'hang', 'speech-update', 'status-update', 'tool-calls', 'transfer-destination-request', 'user-interrupted'].
        silence_timeout_seconds (Union[Unset, float]): How many seconds of silence to wait before ending the call.
            Defaults to 30.

            @default 30 Example: 30.
        max_duration_seconds (Union[Unset, float]): This is the maximum number of seconds that the call will last. When
            the call reaches this duration, it will be ended.

            @default 600 (10 minutes) Example: 600.
        background_sound (Union[Unset, CreateAssistantDTOBackgroundSound]): This is the background sound in the call.
            Default for phone calls is 'office' and default for web calls is 'off'. Example: office.
        background_denoising_enabled (Union[Unset, bool]): This enables filtering of noise and background speech while
            the user is talking.

            Default `false` while in beta.

            @default false
        model_output_in_messages_enabled (Union[Unset, bool]): This determines whether the model's output is used in
            conversation history rather than the transcription of assistant's speech.

            Default `false` while in beta.

            @default false
        transport_configurations (Union[Unset, list['TransportConfigurationTwilio']]): These are the configurations to
            be passed to the transport providers of assistant's calls, like Twilio. You can store multiple configurations
            for different transport providers. For a call, only the configuration matching the call transport provider is
            used.
        observability_plan (Union['LangfuseObservabilityPlan', Unset]): This is the plan for observability configuration
            of assistant's calls.
            Currently supports Langfuse for tracing and monitoring.
        credentials (Union[Unset, list[Union['CreateAnthropicCredentialDTO', 'CreateAnyscaleCredentialDTO',
            'CreateAssemblyAICredentialDTO', 'CreateAzureCredentialDTO', 'CreateAzureOpenAICredentialDTO',
            'CreateByoSipTrunkCredentialDTO', 'CreateCartesiaCredentialDTO', 'CreateCerebrasCredentialDTO',
            'CreateCloudflareCredentialDTO', 'CreateCustomLLMCredentialDTO', 'CreateDeepInfraCredentialDTO',
            'CreateDeepSeekCredentialDTO', 'CreateDeepgramCredentialDTO', 'CreateElevenLabsCredentialDTO',
            'CreateGcpCredentialDTO', 'CreateGladiaCredentialDTO', 'CreateGoHighLevelCredentialDTO',
            'CreateGoogleCredentialDTO', 'CreateGroqCredentialDTO', 'CreateHumeCredentialDTO',
            'CreateInflectionAICredentialDTO', 'CreateLangfuseCredentialDTO', 'CreateLmntCredentialDTO',
            'CreateMakeCredentialDTO', 'CreateMistralCredentialDTO', 'CreateNeuphonicCredentialDTO',
            'CreateOpenAICredentialDTO', 'CreateOpenRouterCredentialDTO', 'CreatePerplexityAICredentialDTO',
            'CreatePlayHTCredentialDTO', 'CreateRimeAICredentialDTO', 'CreateRunpodCredentialDTO', 'CreateS3CredentialDTO',
            'CreateSmallestAICredentialDTO', 'CreateSpeechmaticsCredentialDTO', 'CreateSupabaseCredentialDTO',
            'CreateTavusCredentialDTO', 'CreateTogetherAICredentialDTO', 'CreateTrieveCredentialDTO',
            'CreateTwilioCredentialDTO', 'CreateVonageCredentialDTO', 'CreateWebhookCredentialDTO',
            'CreateXAiCredentialDTO']]]): These are dynamic credentials that will be used for the assistant calls. By
            default, all the credentials are available for use in the call but you can supplement an additional credentials
            using this. Dynamic credentials override existing credentials.
        name (Union[Unset, str]): This is the name of the assistant.

            This is required when you want to transfer between assistants in a call.
        voicemail_message (Union[Unset, str]): This is the message that the assistant will say if the call is forwarded
            to voicemail.

            If unspecified, it will hang up.
        end_call_message (Union[Unset, str]): This is the message that the assistant will say if it ends the call.

            If unspecified, it will hang up without saying anything.
        end_call_phrases (Union[Unset, list[str]]): This list contains phrases that, if spoken by the assistant, will
            trigger the call to be hung up. Case insensitive.
        compliance_plan (Union[Unset, CompliancePlan]):
        metadata (Union[Unset, CreateAssistantDTOMetadata]): This is for metadata you want to store on the assistant.
        analysis_plan (Union[Unset, AnalysisPlan]):
        artifact_plan (Union[Unset, ArtifactPlan]):
        message_plan (Union[Unset, MessagePlan]):
        start_speaking_plan (Union[Unset, StartSpeakingPlan]):
        stop_speaking_plan (Union[Unset, StopSpeakingPlan]):
        monitor_plan (Union[Unset, MonitorPlan]):
        credential_ids (Union[Unset, list[str]]): These are the credentials that will be used for the assistant calls.
            By default, all the credentials are available for use in the call but you can provide a subset using this.
        server (Union[Unset, Server]):
        hooks (Union[Unset, list['AssistantHooks']]): This is a set of actions that will be performed on certain events.
        keypad_input_plan (Union[Unset, KeypadInputPlan]):
    """

    transcriber: Union[
        "AssemblyAITranscriber",
        "AzureSpeechTranscriber",
        "CustomTranscriber",
        "DeepgramTranscriber",
        "ElevenLabsTranscriber",
        "GladiaTranscriber",
        "SpeechmaticsTranscriber",
        "TalkscriberTranscriber",
        Unset,
    ] = UNSET
    model: Union[
        "AnthropicModel",
        "AnyscaleModel",
        "CerebrasModel",
        "CustomLLMModel",
        "DeepInfraModel",
        "DeepSeekModel",
        "GoogleModel",
        "GroqModel",
        "InflectionAIModel",
        "OpenAIModel",
        "OpenRouterModel",
        "PerplexityAIModel",
        "TogetherAIModel",
        "VapiModel",
        "XaiModel",
        Unset,
    ] = UNSET
    voice: Union[
        "AzureVoice",
        "CartesiaVoice",
        "CustomVoice",
        "DeepgramVoice",
        "ElevenLabsVoice",
        "HumeVoice",
        "LMNTVoice",
        "NeetsVoice",
        "NeuphonicVoice",
        "OpenAIVoice",
        "PlayHTVoice",
        "RimeAIVoice",
        "SmallestAIVoice",
        "TavusVoice",
        "VapiVoice",
        Unset,
    ] = UNSET
    first_message: Union[Unset, str] = UNSET
    first_message_mode: Union[Unset, CreateAssistantDTOFirstMessageMode] = UNSET
    voicemail_detection: Union[
        "GoogleVoicemailDetectionPlan", "OpenAIVoicemailDetectionPlan", "TwilioVoicemailDetectionPlan", Unset
    ] = UNSET
    client_messages: Union[Unset, list[CreateAssistantDTOClientMessagesItem]] = UNSET
    server_messages: Union[Unset, list[CreateAssistantDTOServerMessagesItem]] = UNSET
    silence_timeout_seconds: Union[Unset, float] = UNSET
    max_duration_seconds: Union[Unset, float] = UNSET
    background_sound: Union[Unset, CreateAssistantDTOBackgroundSound] = UNSET
    background_denoising_enabled: Union[Unset, bool] = UNSET
    model_output_in_messages_enabled: Union[Unset, bool] = UNSET
    transport_configurations: Union[Unset, list["TransportConfigurationTwilio"]] = UNSET
    observability_plan: Union["LangfuseObservabilityPlan", Unset] = UNSET
    credentials: Union[
        Unset,
        list[
            Union[
                "CreateAnthropicCredentialDTO",
                "CreateAnyscaleCredentialDTO",
                "CreateAssemblyAICredentialDTO",
                "CreateAzureCredentialDTO",
                "CreateAzureOpenAICredentialDTO",
                "CreateByoSipTrunkCredentialDTO",
                "CreateCartesiaCredentialDTO",
                "CreateCerebrasCredentialDTO",
                "CreateCloudflareCredentialDTO",
                "CreateCustomLLMCredentialDTO",
                "CreateDeepInfraCredentialDTO",
                "CreateDeepSeekCredentialDTO",
                "CreateDeepgramCredentialDTO",
                "CreateElevenLabsCredentialDTO",
                "CreateGcpCredentialDTO",
                "CreateGladiaCredentialDTO",
                "CreateGoHighLevelCredentialDTO",
                "CreateGoogleCredentialDTO",
                "CreateGroqCredentialDTO",
                "CreateHumeCredentialDTO",
                "CreateInflectionAICredentialDTO",
                "CreateLangfuseCredentialDTO",
                "CreateLmntCredentialDTO",
                "CreateMakeCredentialDTO",
                "CreateMistralCredentialDTO",
                "CreateNeuphonicCredentialDTO",
                "CreateOpenAICredentialDTO",
                "CreateOpenRouterCredentialDTO",
                "CreatePerplexityAICredentialDTO",
                "CreatePlayHTCredentialDTO",
                "CreateRimeAICredentialDTO",
                "CreateRunpodCredentialDTO",
                "CreateS3CredentialDTO",
                "CreateSmallestAICredentialDTO",
                "CreateSpeechmaticsCredentialDTO",
                "CreateSupabaseCredentialDTO",
                "CreateTavusCredentialDTO",
                "CreateTogetherAICredentialDTO",
                "CreateTrieveCredentialDTO",
                "CreateTwilioCredentialDTO",
                "CreateVonageCredentialDTO",
                "CreateWebhookCredentialDTO",
                "CreateXAiCredentialDTO",
            ]
        ],
    ] = UNSET
    name: Union[Unset, str] = UNSET
    voicemail_message: Union[Unset, str] = UNSET
    end_call_message: Union[Unset, str] = UNSET
    end_call_phrases: Union[Unset, list[str]] = UNSET
    compliance_plan: Union[Unset, "CompliancePlan"] = UNSET
    metadata: Union[Unset, "CreateAssistantDTOMetadata"] = UNSET
    analysis_plan: Union[Unset, "AnalysisPlan"] = UNSET
    artifact_plan: Union[Unset, "ArtifactPlan"] = UNSET
    message_plan: Union[Unset, "MessagePlan"] = UNSET
    start_speaking_plan: Union[Unset, "StartSpeakingPlan"] = UNSET
    stop_speaking_plan: Union[Unset, "StopSpeakingPlan"] = UNSET
    monitor_plan: Union[Unset, "MonitorPlan"] = UNSET
    credential_ids: Union[Unset, list[str]] = UNSET
    server: Union[Unset, "Server"] = UNSET
    hooks: Union[Unset, list["AssistantHooks"]] = UNSET
    keypad_input_plan: Union[Unset, "KeypadInputPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.anthropic_model import AnthropicModel
        from ..models.anyscale_model import AnyscaleModel
        from ..models.assembly_ai_transcriber import AssemblyAITranscriber
        from ..models.azure_speech_transcriber import AzureSpeechTranscriber
        from ..models.azure_voice import AzureVoice
        from ..models.cartesia_voice import CartesiaVoice
        from ..models.cerebras_model import CerebrasModel
        from ..models.create_anthropic_credential_dto import CreateAnthropicCredentialDTO
        from ..models.create_anyscale_credential_dto import CreateAnyscaleCredentialDTO
        from ..models.create_assembly_ai_credential_dto import CreateAssemblyAICredentialDTO
        from ..models.create_azure_credential_dto import CreateAzureCredentialDTO
        from ..models.create_azure_open_ai_credential_dto import CreateAzureOpenAICredentialDTO
        from ..models.create_byo_sip_trunk_credential_dto import CreateByoSipTrunkCredentialDTO
        from ..models.create_cartesia_credential_dto import CreateCartesiaCredentialDTO
        from ..models.create_cerebras_credential_dto import CreateCerebrasCredentialDTO
        from ..models.create_cloudflare_credential_dto import CreateCloudflareCredentialDTO
        from ..models.create_custom_llm_credential_dto import CreateCustomLLMCredentialDTO
        from ..models.create_deep_infra_credential_dto import CreateDeepInfraCredentialDTO
        from ..models.create_deep_seek_credential_dto import CreateDeepSeekCredentialDTO
        from ..models.create_deepgram_credential_dto import CreateDeepgramCredentialDTO
        from ..models.create_eleven_labs_credential_dto import CreateElevenLabsCredentialDTO
        from ..models.create_gcp_credential_dto import CreateGcpCredentialDTO
        from ..models.create_gladia_credential_dto import CreateGladiaCredentialDTO
        from ..models.create_go_high_level_credential_dto import CreateGoHighLevelCredentialDTO
        from ..models.create_google_credential_dto import CreateGoogleCredentialDTO
        from ..models.create_groq_credential_dto import CreateGroqCredentialDTO
        from ..models.create_hume_credential_dto import CreateHumeCredentialDTO
        from ..models.create_inflection_ai_credential_dto import CreateInflectionAICredentialDTO
        from ..models.create_langfuse_credential_dto import CreateLangfuseCredentialDTO
        from ..models.create_lmnt_credential_dto import CreateLmntCredentialDTO
        from ..models.create_make_credential_dto import CreateMakeCredentialDTO
        from ..models.create_mistral_credential_dto import CreateMistralCredentialDTO
        from ..models.create_neuphonic_credential_dto import CreateNeuphonicCredentialDTO
        from ..models.create_open_ai_credential_dto import CreateOpenAICredentialDTO
        from ..models.create_open_router_credential_dto import CreateOpenRouterCredentialDTO
        from ..models.create_perplexity_ai_credential_dto import CreatePerplexityAICredentialDTO
        from ..models.create_play_ht_credential_dto import CreatePlayHTCredentialDTO
        from ..models.create_rime_ai_credential_dto import CreateRimeAICredentialDTO
        from ..models.create_runpod_credential_dto import CreateRunpodCredentialDTO
        from ..models.create_s3_credential_dto import CreateS3CredentialDTO
        from ..models.create_smallest_ai_credential_dto import CreateSmallestAICredentialDTO
        from ..models.create_speechmatics_credential_dto import CreateSpeechmaticsCredentialDTO
        from ..models.create_supabase_credential_dto import CreateSupabaseCredentialDTO
        from ..models.create_tavus_credential_dto import CreateTavusCredentialDTO
        from ..models.create_together_ai_credential_dto import CreateTogetherAICredentialDTO
        from ..models.create_trieve_credential_dto import CreateTrieveCredentialDTO
        from ..models.create_twilio_credential_dto import CreateTwilioCredentialDTO
        from ..models.create_vonage_credential_dto import CreateVonageCredentialDTO
        from ..models.create_webhook_credential_dto import CreateWebhookCredentialDTO
        from ..models.custom_llm_model import CustomLLMModel
        from ..models.custom_transcriber import CustomTranscriber
        from ..models.custom_voice import CustomVoice
        from ..models.deep_infra_model import DeepInfraModel
        from ..models.deep_seek_model import DeepSeekModel
        from ..models.deepgram_transcriber import DeepgramTranscriber
        from ..models.deepgram_voice import DeepgramVoice
        from ..models.eleven_labs_transcriber import ElevenLabsTranscriber
        from ..models.eleven_labs_voice import ElevenLabsVoice
        from ..models.gladia_transcriber import GladiaTranscriber
        from ..models.google_model import GoogleModel
        from ..models.google_voicemail_detection_plan import GoogleVoicemailDetectionPlan
        from ..models.groq_model import GroqModel
        from ..models.hume_voice import HumeVoice
        from ..models.inflection_ai_model import InflectionAIModel
        from ..models.lmnt_voice import LMNTVoice
        from ..models.neets_voice import NeetsVoice
        from ..models.neuphonic_voice import NeuphonicVoice
        from ..models.open_ai_model import OpenAIModel
        from ..models.open_ai_voice import OpenAIVoice
        from ..models.open_ai_voicemail_detection_plan import OpenAIVoicemailDetectionPlan
        from ..models.open_router_model import OpenRouterModel
        from ..models.perplexity_ai_model import PerplexityAIModel
        from ..models.play_ht_voice import PlayHTVoice
        from ..models.rime_ai_voice import RimeAIVoice
        from ..models.smallest_ai_voice import SmallestAIVoice
        from ..models.speechmatics_transcriber import SpeechmaticsTranscriber
        from ..models.tavus_voice import TavusVoice
        from ..models.together_ai_model import TogetherAIModel
        from ..models.vapi_model import VapiModel

        transcriber: Union[Unset, dict[str, Any]]
        if isinstance(self.transcriber, Unset):
            transcriber = UNSET
        elif isinstance(self.transcriber, AssemblyAITranscriber):
            transcriber = self.transcriber.to_dict()
        elif isinstance(self.transcriber, AzureSpeechTranscriber):
            transcriber = self.transcriber.to_dict()
        elif isinstance(self.transcriber, CustomTranscriber):
            transcriber = self.transcriber.to_dict()
        elif isinstance(self.transcriber, DeepgramTranscriber):
            transcriber = self.transcriber.to_dict()
        elif isinstance(self.transcriber, ElevenLabsTranscriber):
            transcriber = self.transcriber.to_dict()
        elif isinstance(self.transcriber, GladiaTranscriber):
            transcriber = self.transcriber.to_dict()
        elif isinstance(self.transcriber, SpeechmaticsTranscriber):
            transcriber = self.transcriber.to_dict()
        else:
            transcriber = self.transcriber.to_dict()

        model: Union[Unset, dict[str, Any]]
        if isinstance(self.model, Unset):
            model = UNSET
        elif isinstance(self.model, AnyscaleModel):
            model = self.model.to_dict()
        elif isinstance(self.model, AnthropicModel):
            model = self.model.to_dict()
        elif isinstance(self.model, CerebrasModel):
            model = self.model.to_dict()
        elif isinstance(self.model, CustomLLMModel):
            model = self.model.to_dict()
        elif isinstance(self.model, DeepInfraModel):
            model = self.model.to_dict()
        elif isinstance(self.model, DeepSeekModel):
            model = self.model.to_dict()
        elif isinstance(self.model, GoogleModel):
            model = self.model.to_dict()
        elif isinstance(self.model, GroqModel):
            model = self.model.to_dict()
        elif isinstance(self.model, InflectionAIModel):
            model = self.model.to_dict()
        elif isinstance(self.model, OpenAIModel):
            model = self.model.to_dict()
        elif isinstance(self.model, OpenRouterModel):
            model = self.model.to_dict()
        elif isinstance(self.model, PerplexityAIModel):
            model = self.model.to_dict()
        elif isinstance(self.model, TogetherAIModel):
            model = self.model.to_dict()
        elif isinstance(self.model, VapiModel):
            model = self.model.to_dict()
        else:
            model = self.model.to_dict()

        voice: Union[Unset, dict[str, Any]]
        if isinstance(self.voice, Unset):
            voice = UNSET
        elif isinstance(self.voice, AzureVoice):
            voice = self.voice.to_dict()
        elif isinstance(self.voice, CartesiaVoice):
            voice = self.voice.to_dict()
        elif isinstance(self.voice, CustomVoice):
            voice = self.voice.to_dict()
        elif isinstance(self.voice, DeepgramVoice):
            voice = self.voice.to_dict()
        elif isinstance(self.voice, ElevenLabsVoice):
            voice = self.voice.to_dict()
        elif isinstance(self.voice, HumeVoice):
            voice = self.voice.to_dict()
        elif isinstance(self.voice, LMNTVoice):
            voice = self.voice.to_dict()
        elif isinstance(self.voice, NeetsVoice):
            voice = self.voice.to_dict()
        elif isinstance(self.voice, NeuphonicVoice):
            voice = self.voice.to_dict()
        elif isinstance(self.voice, OpenAIVoice):
            voice = self.voice.to_dict()
        elif isinstance(self.voice, PlayHTVoice):
            voice = self.voice.to_dict()
        elif isinstance(self.voice, RimeAIVoice):
            voice = self.voice.to_dict()
        elif isinstance(self.voice, SmallestAIVoice):
            voice = self.voice.to_dict()
        elif isinstance(self.voice, TavusVoice):
            voice = self.voice.to_dict()
        else:
            voice = self.voice.to_dict()

        first_message = self.first_message

        first_message_mode: Union[Unset, str] = UNSET
        if not isinstance(self.first_message_mode, Unset):
            first_message_mode = self.first_message_mode.value

        voicemail_detection: Union[Unset, dict[str, Any]]
        if isinstance(self.voicemail_detection, Unset):
            voicemail_detection = UNSET
        elif isinstance(self.voicemail_detection, GoogleVoicemailDetectionPlan):
            voicemail_detection = self.voicemail_detection.to_dict()
        elif isinstance(self.voicemail_detection, OpenAIVoicemailDetectionPlan):
            voicemail_detection = self.voicemail_detection.to_dict()
        else:
            voicemail_detection = self.voicemail_detection.to_dict()

        client_messages: Union[Unset, list[str]] = UNSET
        if not isinstance(self.client_messages, Unset):
            client_messages = []
            for client_messages_item_data in self.client_messages:
                client_messages_item = client_messages_item_data.value
                client_messages.append(client_messages_item)

        server_messages: Union[Unset, list[str]] = UNSET
        if not isinstance(self.server_messages, Unset):
            server_messages = []
            for server_messages_item_data in self.server_messages:
                server_messages_item = server_messages_item_data.value
                server_messages.append(server_messages_item)

        silence_timeout_seconds = self.silence_timeout_seconds

        max_duration_seconds = self.max_duration_seconds

        background_sound: Union[Unset, str] = UNSET
        if not isinstance(self.background_sound, Unset):
            background_sound = self.background_sound.value

        background_denoising_enabled = self.background_denoising_enabled

        model_output_in_messages_enabled = self.model_output_in_messages_enabled

        transport_configurations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.transport_configurations, Unset):
            transport_configurations = []
            for transport_configurations_item_data in self.transport_configurations:
                transport_configurations_item = transport_configurations_item_data.to_dict()
                transport_configurations.append(transport_configurations_item)

        observability_plan: Union[Unset, dict[str, Any]]
        if isinstance(self.observability_plan, Unset):
            observability_plan = UNSET
        else:
            observability_plan = self.observability_plan.to_dict()

        credentials: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = []
            for credentials_item_data in self.credentials:
                credentials_item: dict[str, Any]
                if isinstance(credentials_item_data, CreateAnthropicCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateAnyscaleCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateAssemblyAICredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateAzureCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateAzureOpenAICredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateByoSipTrunkCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateCartesiaCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateCerebrasCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateCloudflareCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateCustomLLMCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateDeepgramCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateDeepInfraCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateDeepSeekCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateElevenLabsCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateGcpCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateGladiaCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateGoHighLevelCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateGoogleCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateGroqCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateHumeCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateInflectionAICredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateLangfuseCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateLmntCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateMakeCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateMistralCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateNeuphonicCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateOpenAICredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateOpenRouterCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreatePerplexityAICredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreatePlayHTCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateRimeAICredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateRunpodCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateS3CredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateSmallestAICredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateSpeechmaticsCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateSupabaseCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateTavusCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateTogetherAICredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateTrieveCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateTwilioCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateVonageCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                elif isinstance(credentials_item_data, CreateWebhookCredentialDTO):
                    credentials_item = credentials_item_data.to_dict()
                else:
                    credentials_item = credentials_item_data.to_dict()

                credentials.append(credentials_item)

        name = self.name

        voicemail_message = self.voicemail_message

        end_call_message = self.end_call_message

        end_call_phrases: Union[Unset, list[str]] = UNSET
        if not isinstance(self.end_call_phrases, Unset):
            end_call_phrases = self.end_call_phrases

        compliance_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.compliance_plan, Unset):
            compliance_plan = self.compliance_plan.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        analysis_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.analysis_plan, Unset):
            analysis_plan = self.analysis_plan.to_dict()

        artifact_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artifact_plan, Unset):
            artifact_plan = self.artifact_plan.to_dict()

        message_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.message_plan, Unset):
            message_plan = self.message_plan.to_dict()

        start_speaking_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.start_speaking_plan, Unset):
            start_speaking_plan = self.start_speaking_plan.to_dict()

        stop_speaking_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stop_speaking_plan, Unset):
            stop_speaking_plan = self.stop_speaking_plan.to_dict()

        monitor_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monitor_plan, Unset):
            monitor_plan = self.monitor_plan.to_dict()

        credential_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.credential_ids, Unset):
            credential_ids = self.credential_ids

        server: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        hooks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.hooks, Unset):
            hooks = []
            for hooks_item_data in self.hooks:
                hooks_item = hooks_item_data.to_dict()
                hooks.append(hooks_item)

        keypad_input_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.keypad_input_plan, Unset):
            keypad_input_plan = self.keypad_input_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transcriber is not UNSET:
            field_dict["transcriber"] = transcriber
        if model is not UNSET:
            field_dict["model"] = model
        if voice is not UNSET:
            field_dict["voice"] = voice
        if first_message is not UNSET:
            field_dict["firstMessage"] = first_message
        if first_message_mode is not UNSET:
            field_dict["firstMessageMode"] = first_message_mode
        if voicemail_detection is not UNSET:
            field_dict["voicemailDetection"] = voicemail_detection
        if client_messages is not UNSET:
            field_dict["clientMessages"] = client_messages
        if server_messages is not UNSET:
            field_dict["serverMessages"] = server_messages
        if silence_timeout_seconds is not UNSET:
            field_dict["silenceTimeoutSeconds"] = silence_timeout_seconds
        if max_duration_seconds is not UNSET:
            field_dict["maxDurationSeconds"] = max_duration_seconds
        if background_sound is not UNSET:
            field_dict["backgroundSound"] = background_sound
        if background_denoising_enabled is not UNSET:
            field_dict["backgroundDenoisingEnabled"] = background_denoising_enabled
        if model_output_in_messages_enabled is not UNSET:
            field_dict["modelOutputInMessagesEnabled"] = model_output_in_messages_enabled
        if transport_configurations is not UNSET:
            field_dict["transportConfigurations"] = transport_configurations
        if observability_plan is not UNSET:
            field_dict["observabilityPlan"] = observability_plan
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if name is not UNSET:
            field_dict["name"] = name
        if voicemail_message is not UNSET:
            field_dict["voicemailMessage"] = voicemail_message
        if end_call_message is not UNSET:
            field_dict["endCallMessage"] = end_call_message
        if end_call_phrases is not UNSET:
            field_dict["endCallPhrases"] = end_call_phrases
        if compliance_plan is not UNSET:
            field_dict["compliancePlan"] = compliance_plan
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if analysis_plan is not UNSET:
            field_dict["analysisPlan"] = analysis_plan
        if artifact_plan is not UNSET:
            field_dict["artifactPlan"] = artifact_plan
        if message_plan is not UNSET:
            field_dict["messagePlan"] = message_plan
        if start_speaking_plan is not UNSET:
            field_dict["startSpeakingPlan"] = start_speaking_plan
        if stop_speaking_plan is not UNSET:
            field_dict["stopSpeakingPlan"] = stop_speaking_plan
        if monitor_plan is not UNSET:
            field_dict["monitorPlan"] = monitor_plan
        if credential_ids is not UNSET:
            field_dict["credentialIds"] = credential_ids
        if server is not UNSET:
            field_dict["server"] = server
        if hooks is not UNSET:
            field_dict["hooks"] = hooks
        if keypad_input_plan is not UNSET:
            field_dict["keypadInputPlan"] = keypad_input_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analysis_plan import AnalysisPlan
        from ..models.anthropic_model import AnthropicModel
        from ..models.anyscale_model import AnyscaleModel
        from ..models.artifact_plan import ArtifactPlan
        from ..models.assembly_ai_transcriber import AssemblyAITranscriber
        from ..models.assistant_hooks import AssistantHooks
        from ..models.azure_speech_transcriber import AzureSpeechTranscriber
        from ..models.azure_voice import AzureVoice
        from ..models.cartesia_voice import CartesiaVoice
        from ..models.cerebras_model import CerebrasModel
        from ..models.compliance_plan import CompliancePlan
        from ..models.create_anthropic_credential_dto import CreateAnthropicCredentialDTO
        from ..models.create_anyscale_credential_dto import CreateAnyscaleCredentialDTO
        from ..models.create_assembly_ai_credential_dto import CreateAssemblyAICredentialDTO
        from ..models.create_assistant_dto_metadata import CreateAssistantDTOMetadata
        from ..models.create_azure_credential_dto import CreateAzureCredentialDTO
        from ..models.create_azure_open_ai_credential_dto import CreateAzureOpenAICredentialDTO
        from ..models.create_byo_sip_trunk_credential_dto import CreateByoSipTrunkCredentialDTO
        from ..models.create_cartesia_credential_dto import CreateCartesiaCredentialDTO
        from ..models.create_cerebras_credential_dto import CreateCerebrasCredentialDTO
        from ..models.create_cloudflare_credential_dto import CreateCloudflareCredentialDTO
        from ..models.create_custom_llm_credential_dto import CreateCustomLLMCredentialDTO
        from ..models.create_deep_infra_credential_dto import CreateDeepInfraCredentialDTO
        from ..models.create_deep_seek_credential_dto import CreateDeepSeekCredentialDTO
        from ..models.create_deepgram_credential_dto import CreateDeepgramCredentialDTO
        from ..models.create_eleven_labs_credential_dto import CreateElevenLabsCredentialDTO
        from ..models.create_gcp_credential_dto import CreateGcpCredentialDTO
        from ..models.create_gladia_credential_dto import CreateGladiaCredentialDTO
        from ..models.create_go_high_level_credential_dto import CreateGoHighLevelCredentialDTO
        from ..models.create_google_credential_dto import CreateGoogleCredentialDTO
        from ..models.create_groq_credential_dto import CreateGroqCredentialDTO
        from ..models.create_hume_credential_dto import CreateHumeCredentialDTO
        from ..models.create_inflection_ai_credential_dto import CreateInflectionAICredentialDTO
        from ..models.create_langfuse_credential_dto import CreateLangfuseCredentialDTO
        from ..models.create_lmnt_credential_dto import CreateLmntCredentialDTO
        from ..models.create_make_credential_dto import CreateMakeCredentialDTO
        from ..models.create_mistral_credential_dto import CreateMistralCredentialDTO
        from ..models.create_neuphonic_credential_dto import CreateNeuphonicCredentialDTO
        from ..models.create_open_ai_credential_dto import CreateOpenAICredentialDTO
        from ..models.create_open_router_credential_dto import CreateOpenRouterCredentialDTO
        from ..models.create_perplexity_ai_credential_dto import CreatePerplexityAICredentialDTO
        from ..models.create_play_ht_credential_dto import CreatePlayHTCredentialDTO
        from ..models.create_rime_ai_credential_dto import CreateRimeAICredentialDTO
        from ..models.create_runpod_credential_dto import CreateRunpodCredentialDTO
        from ..models.create_s3_credential_dto import CreateS3CredentialDTO
        from ..models.create_smallest_ai_credential_dto import CreateSmallestAICredentialDTO
        from ..models.create_speechmatics_credential_dto import CreateSpeechmaticsCredentialDTO
        from ..models.create_supabase_credential_dto import CreateSupabaseCredentialDTO
        from ..models.create_tavus_credential_dto import CreateTavusCredentialDTO
        from ..models.create_together_ai_credential_dto import CreateTogetherAICredentialDTO
        from ..models.create_trieve_credential_dto import CreateTrieveCredentialDTO
        from ..models.create_twilio_credential_dto import CreateTwilioCredentialDTO
        from ..models.create_vonage_credential_dto import CreateVonageCredentialDTO
        from ..models.create_webhook_credential_dto import CreateWebhookCredentialDTO
        from ..models.create_x_ai_credential_dto import CreateXAiCredentialDTO
        from ..models.custom_llm_model import CustomLLMModel
        from ..models.custom_transcriber import CustomTranscriber
        from ..models.custom_voice import CustomVoice
        from ..models.deep_infra_model import DeepInfraModel
        from ..models.deep_seek_model import DeepSeekModel
        from ..models.deepgram_transcriber import DeepgramTranscriber
        from ..models.deepgram_voice import DeepgramVoice
        from ..models.eleven_labs_transcriber import ElevenLabsTranscriber
        from ..models.eleven_labs_voice import ElevenLabsVoice
        from ..models.gladia_transcriber import GladiaTranscriber
        from ..models.google_model import GoogleModel
        from ..models.google_voicemail_detection_plan import GoogleVoicemailDetectionPlan
        from ..models.groq_model import GroqModel
        from ..models.hume_voice import HumeVoice
        from ..models.inflection_ai_model import InflectionAIModel
        from ..models.keypad_input_plan import KeypadInputPlan
        from ..models.langfuse_observability_plan import LangfuseObservabilityPlan
        from ..models.lmnt_voice import LMNTVoice
        from ..models.message_plan import MessagePlan
        from ..models.monitor_plan import MonitorPlan
        from ..models.neets_voice import NeetsVoice
        from ..models.neuphonic_voice import NeuphonicVoice
        from ..models.open_ai_model import OpenAIModel
        from ..models.open_ai_voice import OpenAIVoice
        from ..models.open_ai_voicemail_detection_plan import OpenAIVoicemailDetectionPlan
        from ..models.open_router_model import OpenRouterModel
        from ..models.perplexity_ai_model import PerplexityAIModel
        from ..models.play_ht_voice import PlayHTVoice
        from ..models.rime_ai_voice import RimeAIVoice
        from ..models.server import Server
        from ..models.smallest_ai_voice import SmallestAIVoice
        from ..models.speechmatics_transcriber import SpeechmaticsTranscriber
        from ..models.start_speaking_plan import StartSpeakingPlan
        from ..models.stop_speaking_plan import StopSpeakingPlan
        from ..models.talkscriber_transcriber import TalkscriberTranscriber
        from ..models.tavus_voice import TavusVoice
        from ..models.together_ai_model import TogetherAIModel
        from ..models.transport_configuration_twilio import TransportConfigurationTwilio
        from ..models.twilio_voicemail_detection_plan import TwilioVoicemailDetectionPlan
        from ..models.vapi_model import VapiModel
        from ..models.vapi_voice import VapiVoice
        from ..models.xai_model import XaiModel

        d = dict(src_dict)

        def _parse_transcriber(
            data: object,
        ) -> Union[
            "AssemblyAITranscriber",
            "AzureSpeechTranscriber",
            "CustomTranscriber",
            "DeepgramTranscriber",
            "ElevenLabsTranscriber",
            "GladiaTranscriber",
            "SpeechmaticsTranscriber",
            "TalkscriberTranscriber",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transcriber_type_0 = AssemblyAITranscriber.from_dict(data)

                return transcriber_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transcriber_type_1 = AzureSpeechTranscriber.from_dict(data)

                return transcriber_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transcriber_type_2 = CustomTranscriber.from_dict(data)

                return transcriber_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transcriber_type_3 = DeepgramTranscriber.from_dict(data)

                return transcriber_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transcriber_type_4 = ElevenLabsTranscriber.from_dict(data)

                return transcriber_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transcriber_type_5 = GladiaTranscriber.from_dict(data)

                return transcriber_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transcriber_type_6 = SpeechmaticsTranscriber.from_dict(data)

                return transcriber_type_6
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            transcriber_type_7 = TalkscriberTranscriber.from_dict(data)

            return transcriber_type_7

        transcriber = _parse_transcriber(d.pop("transcriber", UNSET))

        def _parse_model(
            data: object,
        ) -> Union[
            "AnthropicModel",
            "AnyscaleModel",
            "CerebrasModel",
            "CustomLLMModel",
            "DeepInfraModel",
            "DeepSeekModel",
            "GoogleModel",
            "GroqModel",
            "InflectionAIModel",
            "OpenAIModel",
            "OpenRouterModel",
            "PerplexityAIModel",
            "TogetherAIModel",
            "VapiModel",
            "XaiModel",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_0 = AnyscaleModel.from_dict(data)

                return model_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_1 = AnthropicModel.from_dict(data)

                return model_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_2 = CerebrasModel.from_dict(data)

                return model_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_3 = CustomLLMModel.from_dict(data)

                return model_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_4 = DeepInfraModel.from_dict(data)

                return model_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_5 = DeepSeekModel.from_dict(data)

                return model_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_6 = GoogleModel.from_dict(data)

                return model_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_7 = GroqModel.from_dict(data)

                return model_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_8 = InflectionAIModel.from_dict(data)

                return model_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_9 = OpenAIModel.from_dict(data)

                return model_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_10 = OpenRouterModel.from_dict(data)

                return model_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_11 = PerplexityAIModel.from_dict(data)

                return model_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_12 = TogetherAIModel.from_dict(data)

                return model_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_13 = VapiModel.from_dict(data)

                return model_type_13
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            model_type_14 = XaiModel.from_dict(data)

            return model_type_14

        model = _parse_model(d.pop("model", UNSET))

        def _parse_voice(
            data: object,
        ) -> Union[
            "AzureVoice",
            "CartesiaVoice",
            "CustomVoice",
            "DeepgramVoice",
            "ElevenLabsVoice",
            "HumeVoice",
            "LMNTVoice",
            "NeetsVoice",
            "NeuphonicVoice",
            "OpenAIVoice",
            "PlayHTVoice",
            "RimeAIVoice",
            "SmallestAIVoice",
            "TavusVoice",
            "VapiVoice",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_0 = AzureVoice.from_dict(data)

                return voice_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_1 = CartesiaVoice.from_dict(data)

                return voice_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_2 = CustomVoice.from_dict(data)

                return voice_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_3 = DeepgramVoice.from_dict(data)

                return voice_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_4 = ElevenLabsVoice.from_dict(data)

                return voice_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_5 = HumeVoice.from_dict(data)

                return voice_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_6 = LMNTVoice.from_dict(data)

                return voice_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_7 = NeetsVoice.from_dict(data)

                return voice_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_8 = NeuphonicVoice.from_dict(data)

                return voice_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_9 = OpenAIVoice.from_dict(data)

                return voice_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_10 = PlayHTVoice.from_dict(data)

                return voice_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_11 = RimeAIVoice.from_dict(data)

                return voice_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_12 = SmallestAIVoice.from_dict(data)

                return voice_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_13 = TavusVoice.from_dict(data)

                return voice_type_13
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            voice_type_14 = VapiVoice.from_dict(data)

            return voice_type_14

        voice = _parse_voice(d.pop("voice", UNSET))

        first_message = d.pop("firstMessage", UNSET)

        _first_message_mode = d.pop("firstMessageMode", UNSET)
        first_message_mode: Union[Unset, CreateAssistantDTOFirstMessageMode]
        if isinstance(_first_message_mode, Unset):
            first_message_mode = UNSET
        else:
            first_message_mode = CreateAssistantDTOFirstMessageMode(_first_message_mode)

        def _parse_voicemail_detection(
            data: object,
        ) -> Union[
            "GoogleVoicemailDetectionPlan", "OpenAIVoicemailDetectionPlan", "TwilioVoicemailDetectionPlan", Unset
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voicemail_detection_type_0 = GoogleVoicemailDetectionPlan.from_dict(data)

                return voicemail_detection_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voicemail_detection_type_1 = OpenAIVoicemailDetectionPlan.from_dict(data)

                return voicemail_detection_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            voicemail_detection_type_2 = TwilioVoicemailDetectionPlan.from_dict(data)

            return voicemail_detection_type_2

        voicemail_detection = _parse_voicemail_detection(d.pop("voicemailDetection", UNSET))

        client_messages = []
        _client_messages = d.pop("clientMessages", UNSET)
        for client_messages_item_data in _client_messages or []:
            client_messages_item = CreateAssistantDTOClientMessagesItem(client_messages_item_data)

            client_messages.append(client_messages_item)

        server_messages = []
        _server_messages = d.pop("serverMessages", UNSET)
        for server_messages_item_data in _server_messages or []:
            server_messages_item = CreateAssistantDTOServerMessagesItem(server_messages_item_data)

            server_messages.append(server_messages_item)

        silence_timeout_seconds = d.pop("silenceTimeoutSeconds", UNSET)

        max_duration_seconds = d.pop("maxDurationSeconds", UNSET)

        _background_sound = d.pop("backgroundSound", UNSET)
        background_sound: Union[Unset, CreateAssistantDTOBackgroundSound]
        if isinstance(_background_sound, Unset):
            background_sound = UNSET
        else:
            background_sound = CreateAssistantDTOBackgroundSound(_background_sound)

        background_denoising_enabled = d.pop("backgroundDenoisingEnabled", UNSET)

        model_output_in_messages_enabled = d.pop("modelOutputInMessagesEnabled", UNSET)

        transport_configurations = []
        _transport_configurations = d.pop("transportConfigurations", UNSET)
        for transport_configurations_item_data in _transport_configurations or []:
            transport_configurations_item = TransportConfigurationTwilio.from_dict(transport_configurations_item_data)

            transport_configurations.append(transport_configurations_item)

        def _parse_observability_plan(data: object) -> Union["LangfuseObservabilityPlan", Unset]:
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            observability_plan_type_0 = LangfuseObservabilityPlan.from_dict(data)

            return observability_plan_type_0

        observability_plan = _parse_observability_plan(d.pop("observabilityPlan", UNSET))

        credentials = []
        _credentials = d.pop("credentials", UNSET)
        for credentials_item_data in _credentials or []:

            def _parse_credentials_item(
                data: object,
            ) -> Union[
                "CreateAnthropicCredentialDTO",
                "CreateAnyscaleCredentialDTO",
                "CreateAssemblyAICredentialDTO",
                "CreateAzureCredentialDTO",
                "CreateAzureOpenAICredentialDTO",
                "CreateByoSipTrunkCredentialDTO",
                "CreateCartesiaCredentialDTO",
                "CreateCerebrasCredentialDTO",
                "CreateCloudflareCredentialDTO",
                "CreateCustomLLMCredentialDTO",
                "CreateDeepInfraCredentialDTO",
                "CreateDeepSeekCredentialDTO",
                "CreateDeepgramCredentialDTO",
                "CreateElevenLabsCredentialDTO",
                "CreateGcpCredentialDTO",
                "CreateGladiaCredentialDTO",
                "CreateGoHighLevelCredentialDTO",
                "CreateGoogleCredentialDTO",
                "CreateGroqCredentialDTO",
                "CreateHumeCredentialDTO",
                "CreateInflectionAICredentialDTO",
                "CreateLangfuseCredentialDTO",
                "CreateLmntCredentialDTO",
                "CreateMakeCredentialDTO",
                "CreateMistralCredentialDTO",
                "CreateNeuphonicCredentialDTO",
                "CreateOpenAICredentialDTO",
                "CreateOpenRouterCredentialDTO",
                "CreatePerplexityAICredentialDTO",
                "CreatePlayHTCredentialDTO",
                "CreateRimeAICredentialDTO",
                "CreateRunpodCredentialDTO",
                "CreateS3CredentialDTO",
                "CreateSmallestAICredentialDTO",
                "CreateSpeechmaticsCredentialDTO",
                "CreateSupabaseCredentialDTO",
                "CreateTavusCredentialDTO",
                "CreateTogetherAICredentialDTO",
                "CreateTrieveCredentialDTO",
                "CreateTwilioCredentialDTO",
                "CreateVonageCredentialDTO",
                "CreateWebhookCredentialDTO",
                "CreateXAiCredentialDTO",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_0 = CreateAnthropicCredentialDTO.from_dict(data)

                    return credentials_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_1 = CreateAnyscaleCredentialDTO.from_dict(data)

                    return credentials_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_2 = CreateAssemblyAICredentialDTO.from_dict(data)

                    return credentials_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_3 = CreateAzureCredentialDTO.from_dict(data)

                    return credentials_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_4 = CreateAzureOpenAICredentialDTO.from_dict(data)

                    return credentials_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_5 = CreateByoSipTrunkCredentialDTO.from_dict(data)

                    return credentials_item_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_6 = CreateCartesiaCredentialDTO.from_dict(data)

                    return credentials_item_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_7 = CreateCerebrasCredentialDTO.from_dict(data)

                    return credentials_item_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_8 = CreateCloudflareCredentialDTO.from_dict(data)

                    return credentials_item_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_9 = CreateCustomLLMCredentialDTO.from_dict(data)

                    return credentials_item_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_10 = CreateDeepgramCredentialDTO.from_dict(data)

                    return credentials_item_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_11 = CreateDeepInfraCredentialDTO.from_dict(data)

                    return credentials_item_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_12 = CreateDeepSeekCredentialDTO.from_dict(data)

                    return credentials_item_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_13 = CreateElevenLabsCredentialDTO.from_dict(data)

                    return credentials_item_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_14 = CreateGcpCredentialDTO.from_dict(data)

                    return credentials_item_type_14
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_15 = CreateGladiaCredentialDTO.from_dict(data)

                    return credentials_item_type_15
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_16 = CreateGoHighLevelCredentialDTO.from_dict(data)

                    return credentials_item_type_16
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_17 = CreateGoogleCredentialDTO.from_dict(data)

                    return credentials_item_type_17
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_18 = CreateGroqCredentialDTO.from_dict(data)

                    return credentials_item_type_18
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_19 = CreateHumeCredentialDTO.from_dict(data)

                    return credentials_item_type_19
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_20 = CreateInflectionAICredentialDTO.from_dict(data)

                    return credentials_item_type_20
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_21 = CreateLangfuseCredentialDTO.from_dict(data)

                    return credentials_item_type_21
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_22 = CreateLmntCredentialDTO.from_dict(data)

                    return credentials_item_type_22
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_23 = CreateMakeCredentialDTO.from_dict(data)

                    return credentials_item_type_23
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_24 = CreateMistralCredentialDTO.from_dict(data)

                    return credentials_item_type_24
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_25 = CreateNeuphonicCredentialDTO.from_dict(data)

                    return credentials_item_type_25
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_26 = CreateOpenAICredentialDTO.from_dict(data)

                    return credentials_item_type_26
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_27 = CreateOpenRouterCredentialDTO.from_dict(data)

                    return credentials_item_type_27
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_28 = CreatePerplexityAICredentialDTO.from_dict(data)

                    return credentials_item_type_28
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_29 = CreatePlayHTCredentialDTO.from_dict(data)

                    return credentials_item_type_29
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_30 = CreateRimeAICredentialDTO.from_dict(data)

                    return credentials_item_type_30
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_31 = CreateRunpodCredentialDTO.from_dict(data)

                    return credentials_item_type_31
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_32 = CreateS3CredentialDTO.from_dict(data)

                    return credentials_item_type_32
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_33 = CreateSmallestAICredentialDTO.from_dict(data)

                    return credentials_item_type_33
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_34 = CreateSpeechmaticsCredentialDTO.from_dict(data)

                    return credentials_item_type_34
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_35 = CreateSupabaseCredentialDTO.from_dict(data)

                    return credentials_item_type_35
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_36 = CreateTavusCredentialDTO.from_dict(data)

                    return credentials_item_type_36
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_37 = CreateTogetherAICredentialDTO.from_dict(data)

                    return credentials_item_type_37
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_38 = CreateTrieveCredentialDTO.from_dict(data)

                    return credentials_item_type_38
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_39 = CreateTwilioCredentialDTO.from_dict(data)

                    return credentials_item_type_39
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_40 = CreateVonageCredentialDTO.from_dict(data)

                    return credentials_item_type_40
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credentials_item_type_41 = CreateWebhookCredentialDTO.from_dict(data)

                    return credentials_item_type_41
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_item_type_42 = CreateXAiCredentialDTO.from_dict(data)

                return credentials_item_type_42

            credentials_item = _parse_credentials_item(credentials_item_data)

            credentials.append(credentials_item)

        name = d.pop("name", UNSET)

        voicemail_message = d.pop("voicemailMessage", UNSET)

        end_call_message = d.pop("endCallMessage", UNSET)

        end_call_phrases = cast(list[str], d.pop("endCallPhrases", UNSET))

        _compliance_plan = d.pop("compliancePlan", UNSET)
        compliance_plan: Union[Unset, CompliancePlan]
        if isinstance(_compliance_plan, Unset):
            compliance_plan = UNSET
        else:
            compliance_plan = CompliancePlan.from_dict(_compliance_plan)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CreateAssistantDTOMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateAssistantDTOMetadata.from_dict(_metadata)

        _analysis_plan = d.pop("analysisPlan", UNSET)
        analysis_plan: Union[Unset, AnalysisPlan]
        if isinstance(_analysis_plan, Unset):
            analysis_plan = UNSET
        else:
            analysis_plan = AnalysisPlan.from_dict(_analysis_plan)

        _artifact_plan = d.pop("artifactPlan", UNSET)
        artifact_plan: Union[Unset, ArtifactPlan]
        if isinstance(_artifact_plan, Unset):
            artifact_plan = UNSET
        else:
            artifact_plan = ArtifactPlan.from_dict(_artifact_plan)

        _message_plan = d.pop("messagePlan", UNSET)
        message_plan: Union[Unset, MessagePlan]
        if isinstance(_message_plan, Unset):
            message_plan = UNSET
        else:
            message_plan = MessagePlan.from_dict(_message_plan)

        _start_speaking_plan = d.pop("startSpeakingPlan", UNSET)
        start_speaking_plan: Union[Unset, StartSpeakingPlan]
        if isinstance(_start_speaking_plan, Unset):
            start_speaking_plan = UNSET
        else:
            start_speaking_plan = StartSpeakingPlan.from_dict(_start_speaking_plan)

        _stop_speaking_plan = d.pop("stopSpeakingPlan", UNSET)
        stop_speaking_plan: Union[Unset, StopSpeakingPlan]
        if isinstance(_stop_speaking_plan, Unset):
            stop_speaking_plan = UNSET
        else:
            stop_speaking_plan = StopSpeakingPlan.from_dict(_stop_speaking_plan)

        _monitor_plan = d.pop("monitorPlan", UNSET)
        monitor_plan: Union[Unset, MonitorPlan]
        if isinstance(_monitor_plan, Unset):
            monitor_plan = UNSET
        else:
            monitor_plan = MonitorPlan.from_dict(_monitor_plan)

        credential_ids = cast(list[str], d.pop("credentialIds", UNSET))

        _server = d.pop("server", UNSET)
        server: Union[Unset, Server]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = Server.from_dict(_server)

        hooks = []
        _hooks = d.pop("hooks", UNSET)
        for hooks_item_data in _hooks or []:
            hooks_item = AssistantHooks.from_dict(hooks_item_data)

            hooks.append(hooks_item)

        _keypad_input_plan = d.pop("keypadInputPlan", UNSET)
        keypad_input_plan: Union[Unset, KeypadInputPlan]
        if isinstance(_keypad_input_plan, Unset):
            keypad_input_plan = UNSET
        else:
            keypad_input_plan = KeypadInputPlan.from_dict(_keypad_input_plan)

        create_assistant_dto = cls(
            transcriber=transcriber,
            model=model,
            voice=voice,
            first_message=first_message,
            first_message_mode=first_message_mode,
            voicemail_detection=voicemail_detection,
            client_messages=client_messages,
            server_messages=server_messages,
            silence_timeout_seconds=silence_timeout_seconds,
            max_duration_seconds=max_duration_seconds,
            background_sound=background_sound,
            background_denoising_enabled=background_denoising_enabled,
            model_output_in_messages_enabled=model_output_in_messages_enabled,
            transport_configurations=transport_configurations,
            observability_plan=observability_plan,
            credentials=credentials,
            name=name,
            voicemail_message=voicemail_message,
            end_call_message=end_call_message,
            end_call_phrases=end_call_phrases,
            compliance_plan=compliance_plan,
            metadata=metadata,
            analysis_plan=analysis_plan,
            artifact_plan=artifact_plan,
            message_plan=message_plan,
            start_speaking_plan=start_speaking_plan,
            stop_speaking_plan=stop_speaking_plan,
            monitor_plan=monitor_plan,
            credential_ids=credential_ids,
            server=server,
            hooks=hooks,
            keypad_input_plan=keypad_input_plan,
        )

        create_assistant_dto.additional_properties = d
        return create_assistant_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
