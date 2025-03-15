from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorPlan")


@_attrs_define
class MonitorPlan:
    """
    Attributes:
        listen_enabled (Union[Unset, bool]): This determines whether the assistant's calls allow live listening.
            Defaults to true.

            Fetch `call.monitor.listenUrl` to get the live listening URL.

            @default true
        control_enabled (Union[Unset, bool]): This determines whether the assistant's calls allow live control. Defaults
            to true.

            Fetch `call.monitor.controlUrl` to get the live control URL.

            To use, send any control message via a POST request to `call.monitor.controlUrl`. Here are the types of controls
            supported: https://docs.vapi.ai/api-reference/messages/client-inbound-message

            @default true
    """

    listen_enabled: Union[Unset, bool] = UNSET
    control_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        listen_enabled = self.listen_enabled

        control_enabled = self.control_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if listen_enabled is not UNSET:
            field_dict["listenEnabled"] = listen_enabled
        if control_enabled is not UNSET:
            field_dict["controlEnabled"] = control_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        listen_enabled = d.pop("listenEnabled", UNSET)

        control_enabled = d.pop("controlEnabled", UNSET)

        monitor_plan = cls(
            listen_enabled=listen_enabled,
            control_enabled=control_enabled,
        )

        monitor_plan.additional_properties = d
        return monitor_plan

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
