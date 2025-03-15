from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AutoReloadPlan")


@_attrs_define
class AutoReloadPlan:
    """
    Attributes:
        credits_ (float): This the amount of credits to reload.
        threshold (float): This is the limit at which the reload is triggered.
    """

    credits_: float
    threshold: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_ = self.credits_

        threshold = self.threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credits": credits_,
                "threshold": threshold,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        credits_ = d.pop("credits")

        threshold = d.pop("threshold")

        auto_reload_plan = cls(
            credits_=credits_,
            threshold=threshold,
        )

        auto_reload_plan.additional_properties = d
        return auto_reload_plan

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
