from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.open_ai_message_role import OpenAIMessageRole

T = TypeVar("T", bound="OpenAIMessage")


@_attrs_define
class OpenAIMessage:
    """
    Attributes:
        content (Union[None, str]):
        role (OpenAIMessageRole):
    """

    content: Union[None, str]
    role: OpenAIMessageRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: Union[None, str]
        content = self.content

        role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_content(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        content = _parse_content(d.pop("content"))

        role = OpenAIMessageRole(d.pop("role"))

        open_ai_message = cls(
            content=content,
            role=role,
        )

        open_ai_message.additional_properties = d
        return open_ai_message

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
