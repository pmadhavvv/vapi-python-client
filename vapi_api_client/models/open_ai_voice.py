from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.open_ai_voice_provider import OpenAIVoiceProvider
from ..models.open_ai_voice_voice_id import OpenAIVoiceVoiceId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chunk_plan import ChunkPlan
    from ..models.fallback_plan import FallbackPlan


T = TypeVar("T", bound="OpenAIVoice")


@_attrs_define
class OpenAIVoice:
    """
    Attributes:
        provider (OpenAIVoiceProvider): This is the voice provider that will be used.
        voice_id (OpenAIVoiceVoiceId): This is the provider-specific ID that will be used.
            Please note that ash, ballad, coral, sage, and verse may only be used with realtime models.
        speed (Union[Unset, float]): This is the speed multiplier that will be used.
        chunk_plan (Union[Unset, ChunkPlan]):
        fallback_plan (Union[Unset, FallbackPlan]):
    """

    provider: OpenAIVoiceProvider
    voice_id: OpenAIVoiceVoiceId
    speed: Union[Unset, float] = UNSET
    chunk_plan: Union[Unset, "ChunkPlan"] = UNSET
    fallback_plan: Union[Unset, "FallbackPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        voice_id = self.voice_id.value

        speed = self.speed

        chunk_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.chunk_plan, Unset):
            chunk_plan = self.chunk_plan.to_dict()

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
        if speed is not UNSET:
            field_dict["speed"] = speed
        if chunk_plan is not UNSET:
            field_dict["chunkPlan"] = chunk_plan
        if fallback_plan is not UNSET:
            field_dict["fallbackPlan"] = fallback_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chunk_plan import ChunkPlan
        from ..models.fallback_plan import FallbackPlan

        d = dict(src_dict)
        provider = OpenAIVoiceProvider(d.pop("provider"))

        voice_id = OpenAIVoiceVoiceId(d.pop("voiceId"))

        speed = d.pop("speed", UNSET)

        _chunk_plan = d.pop("chunkPlan", UNSET)
        chunk_plan: Union[Unset, ChunkPlan]
        if isinstance(_chunk_plan, Unset):
            chunk_plan = UNSET
        else:
            chunk_plan = ChunkPlan.from_dict(_chunk_plan)

        _fallback_plan = d.pop("fallbackPlan", UNSET)
        fallback_plan: Union[Unset, FallbackPlan]
        if isinstance(_fallback_plan, Unset):
            fallback_plan = UNSET
        else:
            fallback_plan = FallbackPlan.from_dict(_fallback_plan)

        open_ai_voice = cls(
            provider=provider,
            voice_id=voice_id,
            speed=speed,
            chunk_plan=chunk_plan,
            fallback_plan=fallback_plan,
        )

        open_ai_voice.additional_properties = d
        return open_ai_voice

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
