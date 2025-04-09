from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backoff_plan_type import BackoffPlanType

T = TypeVar("T", bound="BackoffPlan")


@_attrs_define
class BackoffPlan:
    """
    Attributes:
        max_retries (float): This is the maximum number of retries to attempt if the request fails. Defaults to 0 (no
            retries).

            @default 0
        type_ (BackoffPlanType): This is the type of backoff plan to use. Defaults to fixed.

            @default fixed Example: fixed.
        base_delay_seconds (float): This is the base delay in seconds. For linear backoff, this is the delay between
            each retry. For exponential backoff, this is the initial delay. Example: 1.
    """

    max_retries: float
    type_: BackoffPlanType
    base_delay_seconds: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_retries = self.max_retries

        type_ = self.type_.value

        base_delay_seconds = self.base_delay_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maxRetries": max_retries,
                "type": type_,
                "baseDelaySeconds": base_delay_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_retries = d.pop("maxRetries")

        type_ = BackoffPlanType(d.pop("type"))

        base_delay_seconds = d.pop("baseDelaySeconds")

        backoff_plan = cls(
            max_retries=max_retries,
            type_=type_,
            base_delay_seconds=base_delay_seconds,
        )

        backoff_plan.additional_properties = d
        return backoff_plan

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
