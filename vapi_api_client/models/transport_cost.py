from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transport_cost_provider import TransportCostProvider
from ..models.transport_cost_type import TransportCostType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransportCost")


@_attrs_define
class TransportCost:
    """
    Attributes:
        type_ (TransportCostType): This is the type of cost, always 'transport' for this class.
        minutes (float): This is the minutes of `transport` usage. This should match `call.endedAt` - `call.startedAt`.
        cost (float): This is the cost of the component in USD.
        provider (Union[Unset, TransportCostProvider]):
    """

    type_: TransportCostType
    minutes: float
    cost: float
    provider: Union[Unset, TransportCostProvider] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        minutes = self.minutes

        cost = self.cost

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "minutes": minutes,
                "cost": cost,
            }
        )
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = TransportCostType(d.pop("type"))

        minutes = d.pop("minutes")

        cost = d.pop("cost")

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, TransportCostProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = TransportCostProvider(_provider)

        transport_cost = cls(
            type_=type_,
            minutes=minutes,
            cost=cost,
            provider=provider,
        )

        transport_cost.additional_properties = d
        return transport_cost

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
