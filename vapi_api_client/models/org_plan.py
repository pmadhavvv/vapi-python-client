from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_plan_included_providers_item import OrgPlanIncludedProvidersItem


T = TypeVar("T", bound="OrgPlan")


@_attrs_define
class OrgPlan:
    """
    Attributes:
        included_providers (Union[Unset, list['OrgPlanIncludedProvidersItem']]):
        included_minutes (Union[Unset, float]):
        cost_per_overage_minute (Union[Unset, float]):
    """

    included_providers: Union[Unset, list["OrgPlanIncludedProvidersItem"]] = UNSET
    included_minutes: Union[Unset, float] = UNSET
    cost_per_overage_minute: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        included_providers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.included_providers, Unset):
            included_providers = []
            for included_providers_item_data in self.included_providers:
                included_providers_item = included_providers_item_data.to_dict()
                included_providers.append(included_providers_item)

        included_minutes = self.included_minutes

        cost_per_overage_minute = self.cost_per_overage_minute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if included_providers is not UNSET:
            field_dict["includedProviders"] = included_providers
        if included_minutes is not UNSET:
            field_dict["includedMinutes"] = included_minutes
        if cost_per_overage_minute is not UNSET:
            field_dict["costPerOverageMinute"] = cost_per_overage_minute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_plan_included_providers_item import OrgPlanIncludedProvidersItem

        d = dict(src_dict)
        included_providers = []
        _included_providers = d.pop("includedProviders", UNSET)
        for included_providers_item_data in _included_providers or []:
            included_providers_item = OrgPlanIncludedProvidersItem.from_dict(included_providers_item_data)

            included_providers.append(included_providers_item)

        included_minutes = d.pop("includedMinutes", UNSET)

        cost_per_overage_minute = d.pop("costPerOverageMinute", UNSET)

        org_plan = cls(
            included_providers=included_providers,
            included_minutes=included_minutes,
            cost_per_overage_minute=cost_per_overage_minute,
        )

        org_plan.additional_properties = d
        return org_plan

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
