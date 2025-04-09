from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fallback_vapi_voice_provider import FallbackVapiVoiceProvider
from ..models.fallback_vapi_voice_voice_id import FallbackVapiVoiceVoiceId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chunk_plan import ChunkPlan


T = TypeVar("T", bound="FallbackVapiVoice")


@_attrs_define
class FallbackVapiVoice:
    """
    Attributes:
        provider (FallbackVapiVoiceProvider): This is the voice provider that will be used.
        voice_id (FallbackVapiVoiceVoiceId): The voices provided by Vapi
        chunk_plan (Union[Unset, ChunkPlan]):
    """

    provider: FallbackVapiVoiceProvider
    voice_id: FallbackVapiVoiceVoiceId
    chunk_plan: Union[Unset, "ChunkPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        voice_id = self.voice_id.value

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
        if chunk_plan is not UNSET:
            field_dict["chunkPlan"] = chunk_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chunk_plan import ChunkPlan

        d = dict(src_dict)
        provider = FallbackVapiVoiceProvider(d.pop("provider"))

        voice_id = FallbackVapiVoiceVoiceId(d.pop("voiceId"))

        _chunk_plan = d.pop("chunkPlan", UNSET)
        chunk_plan: Union[Unset, ChunkPlan]
        if isinstance(_chunk_plan, Unset):
            chunk_plan = UNSET
        else:
            chunk_plan = ChunkPlan.from_dict(_chunk_plan)

        fallback_vapi_voice = cls(
            provider=provider,
            voice_id=voice_id,
            chunk_plan=chunk_plan,
        )

        fallback_vapi_voice.additional_properties = d
        return fallback_vapi_voice

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
