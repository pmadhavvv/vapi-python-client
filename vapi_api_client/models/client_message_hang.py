from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_message_hang_type import ClientMessageHangType

T = TypeVar("T", bound="ClientMessageHang")


@_attrs_define
class ClientMessageHang:
    """
    Attributes:
        type_ (ClientMessageHangType): This is the type of the message. "hang" is sent when the assistant is hanging due
            to a delay. The delay can be caused by many factors, such as:
            - the model is too slow to respond
            - the voice is too slow to respond
            - the tool call is still waiting for a response from your server
            - etc.
    """

    type_: ClientMessageHangType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ClientMessageHangType(d.pop("type"))

        client_message_hang = cls(
            type_=type_,
        )

        client_message_hang.additional_properties = d
        return client_message_hang

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
