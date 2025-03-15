from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MakeToolMetadata")


@_attrs_define
class MakeToolMetadata:
    """
    Attributes:
        scenario_id (Union[Unset, float]):
        trigger_hook_id (Union[Unset, float]):
    """

    scenario_id: Union[Unset, float] = UNSET
    trigger_hook_id: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scenario_id = self.scenario_id

        trigger_hook_id = self.trigger_hook_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scenario_id is not UNSET:
            field_dict["scenarioId"] = scenario_id
        if trigger_hook_id is not UNSET:
            field_dict["triggerHookId"] = trigger_hook_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        scenario_id = d.pop("scenarioId", UNSET)

        trigger_hook_id = d.pop("triggerHookId", UNSET)

        make_tool_metadata = cls(
            scenario_id=scenario_id,
            trigger_hook_id=trigger_hook_id,
        )

        make_tool_metadata.additional_properties = d
        return make_tool_metadata

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
