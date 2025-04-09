from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transport_provider import TransportProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="Transport")


@_attrs_define
class Transport:
    """
    Attributes:
        provider (Union[Unset, TransportProvider]): This is the provider used for the call.
        assistant_video_enabled (Union[Unset, bool]): This is determines whether the assistant will have video enabled.

            Only relevant for `webCall` type.
    """

    provider: Union[Unset, TransportProvider] = UNSET
    assistant_video_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        assistant_video_enabled = self.assistant_video_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider
        if assistant_video_enabled is not UNSET:
            field_dict["assistantVideoEnabled"] = assistant_video_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, TransportProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = TransportProvider(_provider)

        assistant_video_enabled = d.pop("assistantVideoEnabled", UNSET)

        transport = cls(
            provider=provider,
            assistant_video_enabled=assistant_video_enabled,
        )

        transport.additional_properties = d
        return transport

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
