from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Monitor")


@_attrs_define
class Monitor:
    """
    Attributes:
        listen_url (Union[Unset, str]): This is the URL where the assistant's calls can be listened to in real-time. To
            enable, set `assistant.monitorPlan.listenEnabled` to `true`.
        control_url (Union[Unset, str]): This is the URL where the assistant's calls can be controlled in real-time. To
            enable, set `assistant.monitorPlan.controlEnabled` to `true`.
    """

    listen_url: Union[Unset, str] = UNSET
    control_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        listen_url = self.listen_url

        control_url = self.control_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if listen_url is not UNSET:
            field_dict["listenUrl"] = listen_url
        if control_url is not UNSET:
            field_dict["controlUrl"] = control_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listen_url = d.pop("listenUrl", UNSET)

        control_url = d.pop("controlUrl", UNSET)

        monitor = cls(
            listen_url=listen_url,
            control_url=control_url,
        )

        monitor.additional_properties = d
        return monitor

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
