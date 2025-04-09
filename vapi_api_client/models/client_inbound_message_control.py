from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_inbound_message_control_control import ClientInboundMessageControlControl
from ..models.client_inbound_message_control_type import ClientInboundMessageControlType

T = TypeVar("T", bound="ClientInboundMessageControl")


@_attrs_define
class ClientInboundMessageControl:
    """
    Attributes:
        type_ (ClientInboundMessageControlType): This is the type of the message. Send "control" message to control the
            assistant. `control` options are:
            - "mute-assistant" - mute the assistant
            - "unmute-assistant" - unmute the assistant
            - "say-first-message" - say the first message (this is used when video recording is enabled and the conversation
            is only started once the client side kicks off the recording)
        control (ClientInboundMessageControlControl): This is the control action
    """

    type_: ClientInboundMessageControlType
    control: ClientInboundMessageControlControl
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        control = self.control.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "control": control,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ClientInboundMessageControlType(d.pop("type"))

        control = ClientInboundMessageControlControl(d.pop("control"))

        client_inbound_message_control = cls(
            type_=type_,
            control=control,
        )

        client_inbound_message_control.additional_properties = d
        return client_inbound_message_control

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
