from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolTemplateMetadata")


@_attrs_define
class ToolTemplateMetadata:
    """
    Attributes:
        collection_type (Union[Unset, str]):
        collection_id (Union[Unset, str]):
        collection_name (Union[Unset, str]):
    """

    collection_type: Union[Unset, str] = UNSET
    collection_id: Union[Unset, str] = UNSET
    collection_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_type = self.collection_type

        collection_id = self.collection_id

        collection_name = self.collection_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collection_type is not UNSET:
            field_dict["collectionType"] = collection_type
        if collection_id is not UNSET:
            field_dict["collectionId"] = collection_id
        if collection_name is not UNSET:
            field_dict["collectionName"] = collection_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        collection_type = d.pop("collectionType", UNSET)

        collection_id = d.pop("collectionId", UNSET)

        collection_name = d.pop("collectionName", UNSET)

        tool_template_metadata = cls(
            collection_type=collection_type,
            collection_id=collection_id,
            collection_name=collection_name,
        )

        tool_template_metadata.additional_properties = d
        return tool_template_metadata

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
