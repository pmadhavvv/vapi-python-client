from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_message_user_interrupted_type import ClientMessageUserInterruptedType

T = TypeVar("T", bound="ClientMessageUserInterrupted")


@_attrs_define
class ClientMessageUserInterrupted:
    """
    Attributes:
        type_ (ClientMessageUserInterruptedType): This is the type of the message. "user-interrupted" is sent when the
            user interrupts the assistant.
    """

    type_: ClientMessageUserInterruptedType
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
        type_ = ClientMessageUserInterruptedType(d.pop("type"))

        client_message_user_interrupted = cls(
            type_=type_,
        )

        client_message_user_interrupted.additional_properties = d
        return client_message_user_interrupted

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
