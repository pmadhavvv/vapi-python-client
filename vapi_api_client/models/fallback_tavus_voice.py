from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fallback_tavus_voice_preset_voice_options import FallbackTavusVoicePresetVoiceOptions
from ..models.fallback_tavus_voice_provider import FallbackTavusVoiceProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chunk_plan import ChunkPlan
    from ..models.tavus_conversation_properties import TavusConversationProperties


T = TypeVar("T", bound="FallbackTavusVoice")


@_attrs_define
class FallbackTavusVoice:
    """
    Attributes:
        provider (FallbackTavusVoiceProvider): This is the voice provider that will be used.
        voice_id (Union[FallbackTavusVoicePresetVoiceOptions, str]): This is the provider-specific ID that will be used.
        persona_id (Union[Unset, str]): This is the unique identifier for the persona that the replica will use in the
            conversation.
        callback_url (Union[Unset, str]): This is the url that will receive webhooks with updates regarding the
            conversation state.
        conversation_name (Union[Unset, str]): This is the name for the conversation.
        conversational_context (Union[Unset, str]): This is the context that will be appended to any context provided in
            the persona, if one is provided.
        custom_greeting (Union[Unset, str]): This is the custom greeting that the replica will give once a participant
            joines the conversation.
        properties (Union[Unset, TavusConversationProperties]):
        chunk_plan (Union[Unset, ChunkPlan]):
    """

    provider: FallbackTavusVoiceProvider
    voice_id: Union[FallbackTavusVoicePresetVoiceOptions, str]
    persona_id: Union[Unset, str] = UNSET
    callback_url: Union[Unset, str] = UNSET
    conversation_name: Union[Unset, str] = UNSET
    conversational_context: Union[Unset, str] = UNSET
    custom_greeting: Union[Unset, str] = UNSET
    properties: Union[Unset, "TavusConversationProperties"] = UNSET
    chunk_plan: Union[Unset, "ChunkPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        voice_id: str
        if isinstance(self.voice_id, FallbackTavusVoicePresetVoiceOptions):
            voice_id = self.voice_id.value
        else:
            voice_id = self.voice_id

        persona_id = self.persona_id

        callback_url = self.callback_url

        conversation_name = self.conversation_name

        conversational_context = self.conversational_context

        custom_greeting = self.custom_greeting

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        chunk_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.chunk_plan, Unset):
            chunk_plan = self.chunk_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "voiceId": voice_id,
            }
        )
        if persona_id is not UNSET:
            field_dict["personaId"] = persona_id
        if callback_url is not UNSET:
            field_dict["callbackUrl"] = callback_url
        if conversation_name is not UNSET:
            field_dict["conversationName"] = conversation_name
        if conversational_context is not UNSET:
            field_dict["conversationalContext"] = conversational_context
        if custom_greeting is not UNSET:
            field_dict["customGreeting"] = custom_greeting
        if properties is not UNSET:
            field_dict["properties"] = properties
        if chunk_plan is not UNSET:
            field_dict["chunkPlan"] = chunk_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chunk_plan import ChunkPlan
        from ..models.tavus_conversation_properties import TavusConversationProperties

        d = dict(src_dict)
        provider = FallbackTavusVoiceProvider(d.pop("provider"))

        def _parse_voice_id(data: object) -> Union[FallbackTavusVoicePresetVoiceOptions, str]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                voice_id_type_0 = FallbackTavusVoicePresetVoiceOptions(data)

                return voice_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[FallbackTavusVoicePresetVoiceOptions, str], data)

        voice_id = _parse_voice_id(d.pop("voiceId"))

        persona_id = d.pop("personaId", UNSET)

        callback_url = d.pop("callbackUrl", UNSET)

        conversation_name = d.pop("conversationName", UNSET)

        conversational_context = d.pop("conversationalContext", UNSET)

        custom_greeting = d.pop("customGreeting", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, TavusConversationProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = TavusConversationProperties.from_dict(_properties)

        _chunk_plan = d.pop("chunkPlan", UNSET)
        chunk_plan: Union[Unset, ChunkPlan]
        if isinstance(_chunk_plan, Unset):
            chunk_plan = UNSET
        else:
            chunk_plan = ChunkPlan.from_dict(_chunk_plan)

        fallback_tavus_voice = cls(
            provider=provider,
            voice_id=voice_id,
            persona_id=persona_id,
            callback_url=callback_url,
            conversation_name=conversation_name,
            conversational_context=conversational_context,
            custom_greeting=custom_greeting,
            properties=properties,
            chunk_plan=chunk_plan,
        )

        fallback_tavus_voice.additional_properties = d
        return fallback_tavus_voice

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
