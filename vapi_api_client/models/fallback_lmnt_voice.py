from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fallback_lmnt_voice_preset_voice_options import FallbackLMNTVoicePresetVoiceOptions
from ..models.fallback_lmnt_voice_provider import FallbackLMNTVoiceProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chunk_plan import ChunkPlan


T = TypeVar("T", bound="FallbackLMNTVoice")


@_attrs_define
class FallbackLMNTVoice:
    """
    Attributes:
        provider (FallbackLMNTVoiceProvider): This is the voice provider that will be used.
        voice_id (Union[FallbackLMNTVoicePresetVoiceOptions, str]): This is the provider-specific ID that will be used.
        speed (Union[Unset, float]): This is the speed multiplier that will be used.
        chunk_plan (Union[Unset, ChunkPlan]):
    """

    provider: FallbackLMNTVoiceProvider
    voice_id: Union[FallbackLMNTVoicePresetVoiceOptions, str]
    speed: Union[Unset, float] = UNSET
    chunk_plan: Union[Unset, "ChunkPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        voice_id: str
        if isinstance(self.voice_id, FallbackLMNTVoicePresetVoiceOptions):
            voice_id = self.voice_id.value
        else:
            voice_id = self.voice_id

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
            }
        )
        if speed is not UNSET:
            field_dict["speed"] = speed
        if chunk_plan is not UNSET:
            field_dict["chunkPlan"] = chunk_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.chunk_plan import ChunkPlan

        d = src_dict.copy()
        provider = FallbackLMNTVoiceProvider(d.pop("provider"))

        def _parse_voice_id(data: object) -> Union[FallbackLMNTVoicePresetVoiceOptions, str]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                voice_id_type_0 = FallbackLMNTVoicePresetVoiceOptions(data)

                return voice_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[FallbackLMNTVoicePresetVoiceOptions, str], data)

        voice_id = _parse_voice_id(d.pop("voiceId"))

        speed = d.pop("speed", UNSET)

        _chunk_plan = d.pop("chunkPlan", UNSET)
        chunk_plan: Union[Unset, ChunkPlan]
        if isinstance(_chunk_plan, Unset):
            chunk_plan = UNSET
        else:
            chunk_plan = ChunkPlan.from_dict(_chunk_plan)

        fallback_lmnt_voice = cls(
            provider=provider,
            voice_id=voice_id,
            speed=speed,
            chunk_plan=chunk_plan,
        )

        fallback_lmnt_voice.additional_properties = d
        return fallback_lmnt_voice

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
