from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GhlToolMetadata")


@_attrs_define
class GhlToolMetadata:
    """
    Attributes:
        workflow_id (Union[Unset, str]):
        location_id (Union[Unset, str]):
    """

    workflow_id: Union[Unset, str] = UNSET
    location_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_id = self.workflow_id

        location_id = self.location_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if location_id is not UNSET:
            field_dict["locationId"] = location_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workflow_id = d.pop("workflowId", UNSET)

        location_id = d.pop("locationId", UNSET)

        ghl_tool_metadata = cls(
            workflow_id=workflow_id,
            location_id=location_id,
        )

        ghl_tool_metadata.additional_properties = d
        return ghl_tool_metadata

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
