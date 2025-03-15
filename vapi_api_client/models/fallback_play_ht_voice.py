from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fallback_play_ht_voice_emotion import FallbackPlayHTVoiceEmotion
from ..models.fallback_play_ht_voice_language import FallbackPlayHTVoiceLanguage
from ..models.fallback_play_ht_voice_model import FallbackPlayHTVoiceModel
from ..models.fallback_play_ht_voice_preset_voice_options import FallbackPlayHTVoicePresetVoiceOptions
from ..models.fallback_play_ht_voice_provider import FallbackPlayHTVoiceProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chunk_plan import ChunkPlan


T = TypeVar("T", bound="FallbackPlayHTVoice")


@_attrs_define
class FallbackPlayHTVoice:
    """
    Attributes:
        provider (FallbackPlayHTVoiceProvider): This is the voice provider that will be used.
        voice_id (Union[FallbackPlayHTVoicePresetVoiceOptions, str]): This is the provider-specific ID that will be
            used.
        speed (Union[Unset, float]): This is the speed multiplier that will be used.
        temperature (Union[Unset, float]): A floating point number between 0, exclusive, and 2, inclusive. If equal to
            null or not provided, the model's default temperature will be used. The temperature parameter controls variance.
            Lower temperatures result in more predictable results, higher temperatures allow each run to vary more, so the
            voice may sound less like the baseline voice.
        emotion (Union[Unset, FallbackPlayHTVoiceEmotion]): An emotion to be applied to the speech.
        voice_guidance (Union[Unset, float]): A number between 1 and 6. Use lower numbers to reduce how unique your
            chosen voice will be compared to other voices.
        style_guidance (Union[Unset, float]): A number between 1 and 30. Use lower numbers to to reduce how strong your
            chosen emotion will be. Higher numbers will create a very emotional performance.
        text_guidance (Union[Unset, float]): A number between 1 and 2. This number influences how closely the generated
            speech adheres to the input text. Use lower values to create more fluid speech, but with a higher chance of
            deviating from the input text. Higher numbers will make the generated speech more accurate to the input text,
            ensuring that the words spoken align closely with the provided text.
        model (Union[Unset, FallbackPlayHTVoiceModel]): Playht voice model/engine to use.
        language (Union[Unset, FallbackPlayHTVoiceLanguage]): The language to use for the speech.
        chunk_plan (Union[Unset, ChunkPlan]):
    """

    provider: FallbackPlayHTVoiceProvider
    voice_id: Union[FallbackPlayHTVoicePresetVoiceOptions, str]
    speed: Union[Unset, float] = UNSET
    temperature: Union[Unset, float] = UNSET
    emotion: Union[Unset, FallbackPlayHTVoiceEmotion] = UNSET
    voice_guidance: Union[Unset, float] = UNSET
    style_guidance: Union[Unset, float] = UNSET
    text_guidance: Union[Unset, float] = UNSET
    model: Union[Unset, FallbackPlayHTVoiceModel] = UNSET
    language: Union[Unset, FallbackPlayHTVoiceLanguage] = UNSET
    chunk_plan: Union[Unset, "ChunkPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        voice_id: str
        if isinstance(self.voice_id, FallbackPlayHTVoicePresetVoiceOptions):
            voice_id = self.voice_id.value
        else:
            voice_id = self.voice_id

        speed = self.speed

        temperature = self.temperature

        emotion: Union[Unset, str] = UNSET
        if not isinstance(self.emotion, Unset):
            emotion = self.emotion.value

        voice_guidance = self.voice_guidance

        style_guidance = self.style_guidance

        text_guidance = self.text_guidance

        model: Union[Unset, str] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.value

        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

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
        if speed is not UNSET:
            field_dict["speed"] = speed
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if emotion is not UNSET:
            field_dict["emotion"] = emotion
        if voice_guidance is not UNSET:
            field_dict["voiceGuidance"] = voice_guidance
        if style_guidance is not UNSET:
            field_dict["styleGuidance"] = style_guidance
        if text_guidance is not UNSET:
            field_dict["textGuidance"] = text_guidance
        if model is not UNSET:
            field_dict["model"] = model
        if language is not UNSET:
            field_dict["language"] = language
        if chunk_plan is not UNSET:
            field_dict["chunkPlan"] = chunk_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.chunk_plan import ChunkPlan

        d = src_dict.copy()
        provider = FallbackPlayHTVoiceProvider(d.pop("provider"))

        def _parse_voice_id(data: object) -> Union[FallbackPlayHTVoicePresetVoiceOptions, str]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                voice_id_type_0 = FallbackPlayHTVoicePresetVoiceOptions(data)

                return voice_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[FallbackPlayHTVoicePresetVoiceOptions, str], data)

        voice_id = _parse_voice_id(d.pop("voiceId"))

        speed = d.pop("speed", UNSET)

        temperature = d.pop("temperature", UNSET)

        _emotion = d.pop("emotion", UNSET)
        emotion: Union[Unset, FallbackPlayHTVoiceEmotion]
        if isinstance(_emotion, Unset):
            emotion = UNSET
        else:
            emotion = FallbackPlayHTVoiceEmotion(_emotion)

        voice_guidance = d.pop("voiceGuidance", UNSET)

        style_guidance = d.pop("styleGuidance", UNSET)

        text_guidance = d.pop("textGuidance", UNSET)

        _model = d.pop("model", UNSET)
        model: Union[Unset, FallbackPlayHTVoiceModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = FallbackPlayHTVoiceModel(_model)

        _language = d.pop("language", UNSET)
        language: Union[Unset, FallbackPlayHTVoiceLanguage]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = FallbackPlayHTVoiceLanguage(_language)

        _chunk_plan = d.pop("chunkPlan", UNSET)
        chunk_plan: Union[Unset, ChunkPlan]
        if isinstance(_chunk_plan, Unset):
            chunk_plan = UNSET
        else:
            chunk_plan = ChunkPlan.from_dict(_chunk_plan)

        fallback_play_ht_voice = cls(
            provider=provider,
            voice_id=voice_id,
            speed=speed,
            temperature=temperature,
            emotion=emotion,
            voice_guidance=voice_guidance,
            style_guidance=style_guidance,
            text_guidance=text_guidance,
            model=model,
            language=language,
            chunk_plan=chunk_plan,
        )

        fallback_play_ht_voice.additional_properties = d
        return fallback_play_ht_voice

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
