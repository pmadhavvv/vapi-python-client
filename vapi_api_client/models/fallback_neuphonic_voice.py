from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fallback_neuphonic_voice_model import FallbackNeuphonicVoiceModel
from ..models.fallback_neuphonic_voice_provider import FallbackNeuphonicVoiceProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chunk_plan import ChunkPlan
    from ..models.fallback_neuphonic_voice_language import FallbackNeuphonicVoiceLanguage


T = TypeVar("T", bound="FallbackNeuphonicVoice")


@_attrs_define
class FallbackNeuphonicVoice:
    """
    Attributes:
        provider (FallbackNeuphonicVoiceProvider): This is the voice provider that will be used.
        voice_id (str): This is the provider-specific ID that will be used.
        language (FallbackNeuphonicVoiceLanguage): This is the language (ISO 639-1) that is enforced for the model.
            Example: en.
        model (Union[Unset, FallbackNeuphonicVoiceModel]): This is the model that will be used. Defaults to 'neu_fast'
            if not specified. Example: neu_fast.
        speed (Union[Unset, float]): This is the speed multiplier that will be used.
        chunk_plan (Union[Unset, ChunkPlan]):
    """

    provider: FallbackNeuphonicVoiceProvider
    voice_id: str
    language: "FallbackNeuphonicVoiceLanguage"
    model: Union[Unset, FallbackNeuphonicVoiceModel] = UNSET
    speed: Union[Unset, float] = UNSET
    chunk_plan: Union[Unset, "ChunkPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        voice_id = self.voice_id

        language = self.language.to_dict()

        model: Union[Unset, str] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.value

        speed = self.speed

        chunk_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.chunk_plan, Unset):
            chunk_plan = self.chunk_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "voiceId": voice_id,
                "language": language,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if speed is not UNSET:
            field_dict["speed"] = speed
        if chunk_plan is not UNSET:
            field_dict["chunkPlan"] = chunk_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.chunk_plan import ChunkPlan
        from ..models.fallback_neuphonic_voice_language import FallbackNeuphonicVoiceLanguage

        d = src_dict.copy()
        provider = FallbackNeuphonicVoiceProvider(d.pop("provider"))

        voice_id = d.pop("voiceId")

        language = FallbackNeuphonicVoiceLanguage.from_dict(d.pop("language"))

        _model = d.pop("model", UNSET)
        model: Union[Unset, FallbackNeuphonicVoiceModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = FallbackNeuphonicVoiceModel(_model)

        speed = d.pop("speed", UNSET)

        _chunk_plan = d.pop("chunkPlan", UNSET)
        chunk_plan: Union[Unset, ChunkPlan]
        if isinstance(_chunk_plan, Unset):
            chunk_plan = UNSET
        else:
            chunk_plan = ChunkPlan.from_dict(_chunk_plan)

        fallback_neuphonic_voice = cls(
            provider=provider,
            voice_id=voice_id,
            language=language,
            model=model,
            speed=speed,
            chunk_plan=chunk_plan,
        )

        fallback_neuphonic_voice.additional_properties = d
        return fallback_neuphonic_voice

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
