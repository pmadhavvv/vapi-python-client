from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keypad_input_plan_delimiters import KeypadInputPlanDelimiters
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeypadInputPlan")


@_attrs_define
class KeypadInputPlan:
    """
    Attributes:
        enabled (Union[Unset, bool]): This keeps track of whether the user has enabled keypad input.
            By default, it is off.

            @default false
        timeout_seconds (Union[Unset, float]): This is the time in seconds to wait before processing the input.
            If the input is not received within this time, the input will be ignored.
            If set to "off", the input will be processed when the user enters a delimiter or immediately if no delimiter is
            used.

            @default 2
        delimiters (Union[Unset, KeypadInputPlanDelimiters]): This is the delimiter(s) that will be used to process the
            input.
            Can be '#', '*', or an empty array.
    """

    enabled: Union[Unset, bool] = UNSET
    timeout_seconds: Union[Unset, float] = UNSET
    delimiters: Union[Unset, KeypadInputPlanDelimiters] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        timeout_seconds = self.timeout_seconds

        delimiters: Union[Unset, str] = UNSET
        if not isinstance(self.delimiters, Unset):
            delimiters = self.delimiters.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds
        if delimiters is not UNSET:
            field_dict["delimiters"] = delimiters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        _delimiters = d.pop("delimiters", UNSET)
        delimiters: Union[Unset, KeypadInputPlanDelimiters]
        if isinstance(_delimiters, Unset):
            delimiters = UNSET
        else:
            delimiters = KeypadInputPlanDelimiters(_delimiters)

        keypad_input_plan = cls(
            enabled=enabled,
            timeout_seconds=timeout_seconds,
            delimiters=delimiters,
        )

        keypad_input_plan.additional_properties = d
        return keypad_input_plan

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
