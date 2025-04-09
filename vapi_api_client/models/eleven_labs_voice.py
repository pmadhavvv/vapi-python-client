from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.eleven_labs_voice_model import ElevenLabsVoiceModel
from ..models.eleven_labs_voice_preset_voice_options import ElevenLabsVoicePresetVoiceOptions
from ..models.eleven_labs_voice_provider import ElevenLabsVoiceProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chunk_plan import ChunkPlan
    from ..models.fallback_plan import FallbackPlan


T = TypeVar("T", bound="ElevenLabsVoice")


@_attrs_define
class ElevenLabsVoice:
    """
    Attributes:
        provider (ElevenLabsVoiceProvider): This is the voice provider that will be used.
        voice_id (Union[ElevenLabsVoicePresetVoiceOptions, str]): This is the provider-specific ID that will be used.
            Ensure the Voice is present in your 11Labs Voice Library.
        stability (Union[Unset, float]): Defines the stability for voice settings. Example: 0.5.
        similarity_boost (Union[Unset, float]): Defines the similarity boost for voice settings. Example: 0.75.
        style (Union[Unset, float]): Defines the style for voice settings.
        use_speaker_boost (Union[Unset, bool]): Defines the use speaker boost for voice settings.
        speed (Union[Unset, float]): Defines the speed for voice settings. Example: 0.9.
        optimize_streaming_latency (Union[Unset, float]): Defines the optimize streaming latency for voice settings.
            Defaults to 3. Example: 3.
        enable_ssml_parsing (Union[Unset, bool]): This enables the use of https://elevenlabs.io/docs/speech-
            synthesis/prompting#pronunciation. Defaults to false to save latency.

            @default false
        model (Union[Unset, ElevenLabsVoiceModel]): This is the model that will be used. Defaults to 'eleven_turbo_v2'
            if not specified. Example: eleven_turbo_v2_5.
        chunk_plan (Union[Unset, ChunkPlan]):
        language (Union[Unset, str]): This is the language (ISO 639-1) that is enforced for the model. Currently only
            Turbo v2.5 supports language enforcement. For other models, an error will be returned if language code is
            provided.
        fallback_plan (Union[Unset, FallbackPlan]):
    """

    provider: ElevenLabsVoiceProvider
    voice_id: Union[ElevenLabsVoicePresetVoiceOptions, str]
    stability: Union[Unset, float] = UNSET
    similarity_boost: Union[Unset, float] = UNSET
    style: Union[Unset, float] = UNSET
    use_speaker_boost: Union[Unset, bool] = UNSET
    speed: Union[Unset, float] = UNSET
    optimize_streaming_latency: Union[Unset, float] = UNSET
    enable_ssml_parsing: Union[Unset, bool] = UNSET
    model: Union[Unset, ElevenLabsVoiceModel] = UNSET
    chunk_plan: Union[Unset, "ChunkPlan"] = UNSET
    language: Union[Unset, str] = UNSET
    fallback_plan: Union[Unset, "FallbackPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        voice_id: str
        if isinstance(self.voice_id, ElevenLabsVoicePresetVoiceOptions):
            voice_id = self.voice_id.value
        else:
            voice_id = self.voice_id

        stability = self.stability

        similarity_boost = self.similarity_boost

        style = self.style

        use_speaker_boost = self.use_speaker_boost

        speed = self.speed

        optimize_streaming_latency = self.optimize_streaming_latency

        enable_ssml_parsing = self.enable_ssml_parsing

        model: Union[Unset, str] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.value

        chunk_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.chunk_plan, Unset):
            chunk_plan = self.chunk_plan.to_dict()

        language = self.language

        fallback_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fallback_plan, Unset):
            fallback_plan = self.fallback_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "voiceId": voice_id,
            }
        )
        if stability is not UNSET:
            field_dict["stability"] = stability
        if similarity_boost is not UNSET:
            field_dict["similarityBoost"] = similarity_boost
        if style is not UNSET:
            field_dict["style"] = style
        if use_speaker_boost is not UNSET:
            field_dict["useSpeakerBoost"] = use_speaker_boost
        if speed is not UNSET:
            field_dict["speed"] = speed
        if optimize_streaming_latency is not UNSET:
            field_dict["optimizeStreamingLatency"] = optimize_streaming_latency
        if enable_ssml_parsing is not UNSET:
            field_dict["enableSsmlParsing"] = enable_ssml_parsing
        if model is not UNSET:
            field_dict["model"] = model
        if chunk_plan is not UNSET:
            field_dict["chunkPlan"] = chunk_plan
        if language is not UNSET:
            field_dict["language"] = language
        if fallback_plan is not UNSET:
            field_dict["fallbackPlan"] = fallback_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chunk_plan import ChunkPlan
        from ..models.fallback_plan import FallbackPlan

        d = dict(src_dict)
        provider = ElevenLabsVoiceProvider(d.pop("provider"))

        def _parse_voice_id(data: object) -> Union[ElevenLabsVoicePresetVoiceOptions, str]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                voice_id_type_0 = ElevenLabsVoicePresetVoiceOptions(data)

                return voice_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[ElevenLabsVoicePresetVoiceOptions, str], data)

        voice_id = _parse_voice_id(d.pop("voiceId"))

        stability = d.pop("stability", UNSET)

        similarity_boost = d.pop("similarityBoost", UNSET)

        style = d.pop("style", UNSET)

        use_speaker_boost = d.pop("useSpeakerBoost", UNSET)

        speed = d.pop("speed", UNSET)

        optimize_streaming_latency = d.pop("optimizeStreamingLatency", UNSET)

        enable_ssml_parsing = d.pop("enableSsmlParsing", UNSET)

        _model = d.pop("model", UNSET)
        model: Union[Unset, ElevenLabsVoiceModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = ElevenLabsVoiceModel(_model)

        _chunk_plan = d.pop("chunkPlan", UNSET)
        chunk_plan: Union[Unset, ChunkPlan]
        if isinstance(_chunk_plan, Unset):
            chunk_plan = UNSET
        else:
            chunk_plan = ChunkPlan.from_dict(_chunk_plan)

        language = d.pop("language", UNSET)

        _fallback_plan = d.pop("fallbackPlan", UNSET)
        fallback_plan: Union[Unset, FallbackPlan]
        if isinstance(_fallback_plan, Unset):
            fallback_plan = UNSET
        else:
            fallback_plan = FallbackPlan.from_dict(_fallback_plan)

        eleven_labs_voice = cls(
            provider=provider,
            voice_id=voice_id,
            stability=stability,
            similarity_boost=similarity_boost,
            style=style,
            use_speaker_boost=use_speaker_boost,
            speed=speed,
            optimize_streaming_latency=optimize_streaming_latency,
            enable_ssml_parsing=enable_ssml_parsing,
            model=model,
            chunk_plan=chunk_plan,
            language=language,
            fallback_plan=fallback_plan,
        )

        eleven_labs_voice.additional_properties = d
        return eleven_labs_voice

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
