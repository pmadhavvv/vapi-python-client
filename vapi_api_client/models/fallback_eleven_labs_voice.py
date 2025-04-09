from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fallback_eleven_labs_voice_model import FallbackElevenLabsVoiceModel
from ..models.fallback_eleven_labs_voice_preset_voice_options import FallbackElevenLabsVoicePresetVoiceOptions
from ..models.fallback_eleven_labs_voice_provider import FallbackElevenLabsVoiceProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chunk_plan import ChunkPlan


T = TypeVar("T", bound="FallbackElevenLabsVoice")


@_attrs_define
class FallbackElevenLabsVoice:
    """
    Attributes:
        provider (FallbackElevenLabsVoiceProvider): This is the voice provider that will be used.
        voice_id (Union[FallbackElevenLabsVoicePresetVoiceOptions, str]): This is the provider-specific ID that will be
            used. Ensure the Voice is present in your 11Labs Voice Library.
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
        model (Union[Unset, FallbackElevenLabsVoiceModel]): This is the model that will be used. Defaults to
            'eleven_turbo_v2' if not specified. Example: eleven_turbo_v2_5.
        language (Union[Unset, str]): This is the language (ISO 639-1) that is enforced for the model. Currently only
            Turbo v2.5 supports language enforcement. For other models, an error will be returned if language code is
            provided.
        chunk_plan (Union[Unset, ChunkPlan]):
    """

    provider: FallbackElevenLabsVoiceProvider
    voice_id: Union[FallbackElevenLabsVoicePresetVoiceOptions, str]
    stability: Union[Unset, float] = UNSET
    similarity_boost: Union[Unset, float] = UNSET
    style: Union[Unset, float] = UNSET
    use_speaker_boost: Union[Unset, bool] = UNSET
    speed: Union[Unset, float] = UNSET
    optimize_streaming_latency: Union[Unset, float] = UNSET
    enable_ssml_parsing: Union[Unset, bool] = UNSET
    model: Union[Unset, FallbackElevenLabsVoiceModel] = UNSET
    language: Union[Unset, str] = UNSET
    chunk_plan: Union[Unset, "ChunkPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        voice_id: str
        if isinstance(self.voice_id, FallbackElevenLabsVoicePresetVoiceOptions):
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

        language = self.language

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
        if language is not UNSET:
            field_dict["language"] = language
        if chunk_plan is not UNSET:
            field_dict["chunkPlan"] = chunk_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chunk_plan import ChunkPlan

        d = dict(src_dict)
        provider = FallbackElevenLabsVoiceProvider(d.pop("provider"))

        def _parse_voice_id(data: object) -> Union[FallbackElevenLabsVoicePresetVoiceOptions, str]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                voice_id_type_0 = FallbackElevenLabsVoicePresetVoiceOptions(data)

                return voice_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[FallbackElevenLabsVoicePresetVoiceOptions, str], data)

        voice_id = _parse_voice_id(d.pop("voiceId"))

        stability = d.pop("stability", UNSET)

        similarity_boost = d.pop("similarityBoost", UNSET)

        style = d.pop("style", UNSET)

        use_speaker_boost = d.pop("useSpeakerBoost", UNSET)

        speed = d.pop("speed", UNSET)

        optimize_streaming_latency = d.pop("optimizeStreamingLatency", UNSET)

        enable_ssml_parsing = d.pop("enableSsmlParsing", UNSET)

        _model = d.pop("model", UNSET)
        model: Union[Unset, FallbackElevenLabsVoiceModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = FallbackElevenLabsVoiceModel(_model)

        language = d.pop("language", UNSET)

        _chunk_plan = d.pop("chunkPlan", UNSET)
        chunk_plan: Union[Unset, ChunkPlan]
        if isinstance(_chunk_plan, Unset):
            chunk_plan = UNSET
        else:
            chunk_plan = ChunkPlan.from_dict(_chunk_plan)

        fallback_eleven_labs_voice = cls(
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
            language=language,
            chunk_plan=chunk_plan,
        )

        fallback_eleven_labs_voice.additional_properties = d
        return fallback_eleven_labs_voice

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
