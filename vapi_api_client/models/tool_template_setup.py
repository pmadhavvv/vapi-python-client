from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolTemplateSetup")


@_attrs_define
class ToolTemplateSetup:
    """
    Attributes:
        title (str):
        description (Union[Unset, str]):
        video_url (Union[Unset, str]):
        docs_url (Union[Unset, str]):
    """

    title: str
    description: Union[Unset, str] = UNSET
    video_url: Union[Unset, str] = UNSET
    docs_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        video_url = self.video_url

        docs_url = self.docs_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if video_url is not UNSET:
            field_dict["videoUrl"] = video_url
        if docs_url is not UNSET:
            field_dict["docsUrl"] = docs_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        description = d.pop("description", UNSET)

        video_url = d.pop("videoUrl", UNSET)

        docs_url = d.pop("docsUrl", UNSET)

        tool_template_setup = cls(
            title=title,
            description=description,
            video_url=video_url,
            docs_url=docs_url,
        )

        tool_template_setup.additional_properties = d
        return tool_template_setup

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
