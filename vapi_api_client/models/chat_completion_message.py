from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completion_message_metadata import ChatCompletionMessageMetadata
    from ..models.chat_completion_message_role import ChatCompletionMessageRole


T = TypeVar("T", bound="ChatCompletionMessage")


@_attrs_define
class ChatCompletionMessage:
    """
    Attributes:
        role (ChatCompletionMessageRole):
        content (Union[None, str]):
        metadata (Union[Unset, ChatCompletionMessageMetadata]):
    """

    role: "ChatCompletionMessageRole"
    content: Union[None, str]
    metadata: Union[Unset, "ChatCompletionMessageMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role.to_dict()

        content: Union[None, str]
        content = self.content

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "content": content,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.chat_completion_message_metadata import ChatCompletionMessageMetadata
        from ..models.chat_completion_message_role import ChatCompletionMessageRole

        d = src_dict.copy()
        role = ChatCompletionMessageRole.from_dict(d.pop("role"))

        def _parse_content(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        content = _parse_content(d.pop("content"))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ChatCompletionMessageMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ChatCompletionMessageMetadata.from_dict(_metadata)

        chat_completion_message = cls(
            role=role,
            content=content,
            metadata=metadata,
        )

        chat_completion_message.additional_properties = d
        return chat_completion_message

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
