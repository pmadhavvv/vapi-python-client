from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_inbound_message_end_call_type import ClientInboundMessageEndCallType

T = TypeVar("T", bound="ClientInboundMessageEndCall")


@_attrs_define
class ClientInboundMessageEndCall:
    """
    Attributes:
        type_ (ClientInboundMessageEndCallType): This is the type of the message. Send "end-call" message to end the
            call.
    """

    type_: ClientInboundMessageEndCallType
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
        type_ = ClientInboundMessageEndCallType(d.pop("type"))

        client_inbound_message_end_call = cls(
            type_=type_,
        )

        client_inbound_message_end_call.additional_properties = d
        return client_inbound_message_end_call

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
