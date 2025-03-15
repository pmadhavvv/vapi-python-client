from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fallback_custom_voice_provider import FallbackCustomVoiceProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chunk_plan import ChunkPlan
    from ..models.server import Server


T = TypeVar("T", bound="FallbackCustomVoice")


@_attrs_define
class FallbackCustomVoice:
    """
    Attributes:
        provider (FallbackCustomVoiceProvider): This is the voice provider that will be used. Use `custom-voice` for
            providers that are not natively supported.
        server (Server):
        chunk_plan (Union[Unset, ChunkPlan]):
    """

    provider: FallbackCustomVoiceProvider
    server: "Server"
    chunk_plan: Union[Unset, "ChunkPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        server = self.server.to_dict()

        chunk_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.chunk_plan, Unset):
            chunk_plan = self.chunk_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "server": server,
            }
        )
        if chunk_plan is not UNSET:
            field_dict["chunkPlan"] = chunk_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.chunk_plan import ChunkPlan
        from ..models.server import Server

        d = src_dict.copy()
        provider = FallbackCustomVoiceProvider(d.pop("provider"))

        server = Server.from_dict(d.pop("server"))

        _chunk_plan = d.pop("chunkPlan", UNSET)
        chunk_plan: Union[Unset, ChunkPlan]
        if isinstance(_chunk_plan, Unset):
            chunk_plan = UNSET
        else:
            chunk_plan = ChunkPlan.from_dict(_chunk_plan)

        fallback_custom_voice = cls(
            provider=provider,
            server=server,
            chunk_plan=chunk_plan,
        )

        fallback_custom_voice.additional_properties = d
        return fallback_custom_voice

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
