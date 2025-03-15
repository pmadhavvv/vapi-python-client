from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vapi_cost_sub_type import VapiCostSubType
from ..models.vapi_cost_type import VapiCostType

T = TypeVar("T", bound="VapiCost")


@_attrs_define
class VapiCost:
    """
    Attributes:
        type_ (VapiCostType): This is the type of cost, always 'vapi' for this class.
        sub_type (VapiCostSubType): This is the sub type of the cost.
        minutes (float): This is the minutes of Vapi usage. This should match `call.endedAt` - `call.startedAt`.
        cost (float): This is the cost of the component in USD.
    """

    type_: VapiCostType
    sub_type: VapiCostSubType
    minutes: float
    cost: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        sub_type = self.sub_type.value

        minutes = self.minutes

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "subType": sub_type,
                "minutes": minutes,
                "cost": cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = VapiCostType(d.pop("type"))

        sub_type = VapiCostSubType(d.pop("subType"))

        minutes = d.pop("minutes")

        cost = d.pop("cost")

        vapi_cost = cls(
            type_=type_,
            sub_type=sub_type,
            minutes=minutes,
            cost=cost,
        )

        vapi_cost.additional_properties = d
        return vapi_cost

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
