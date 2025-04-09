from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.client_inbound_message_add_message import ClientInboundMessageAddMessage
    from ..models.client_inbound_message_control import ClientInboundMessageControl
    from ..models.client_inbound_message_end_call import ClientInboundMessageEndCall
    from ..models.client_inbound_message_say import ClientInboundMessageSay
    from ..models.client_inbound_message_transfer import ClientInboundMessageTransfer


T = TypeVar("T", bound="ClientInboundMessage")


@_attrs_define
class ClientInboundMessage:
    """
    Attributes:
        message (Union['ClientInboundMessageAddMessage', 'ClientInboundMessageControl', 'ClientInboundMessageEndCall',
            'ClientInboundMessageSay', 'ClientInboundMessageTransfer']): These are the messages that can be sent from
            client-side SDKs to control the call.
    """

    message: Union[
        "ClientInboundMessageAddMessage",
        "ClientInboundMessageControl",
        "ClientInboundMessageEndCall",
        "ClientInboundMessageSay",
        "ClientInboundMessageTransfer",
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.client_inbound_message_add_message import ClientInboundMessageAddMessage
        from ..models.client_inbound_message_control import ClientInboundMessageControl
        from ..models.client_inbound_message_end_call import ClientInboundMessageEndCall
        from ..models.client_inbound_message_say import ClientInboundMessageSay

        message: dict[str, Any]
        if isinstance(self.message, ClientInboundMessageAddMessage):
            message = self.message.to_dict()
        elif isinstance(self.message, ClientInboundMessageControl):
            message = self.message.to_dict()
        elif isinstance(self.message, ClientInboundMessageSay):
            message = self.message.to_dict()
        elif isinstance(self.message, ClientInboundMessageEndCall):
            message = self.message.to_dict()
        else:
            message = self.message.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.client_inbound_message_add_message import ClientInboundMessageAddMessage
        from ..models.client_inbound_message_control import ClientInboundMessageControl
        from ..models.client_inbound_message_end_call import ClientInboundMessageEndCall
        from ..models.client_inbound_message_say import ClientInboundMessageSay
        from ..models.client_inbound_message_transfer import ClientInboundMessageTransfer

        d = dict(src_dict)

        def _parse_message(
            data: object,
        ) -> Union[
            "ClientInboundMessageAddMessage",
            "ClientInboundMessageControl",
            "ClientInboundMessageEndCall",
            "ClientInboundMessageSay",
            "ClientInboundMessageTransfer",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_0 = ClientInboundMessageAddMessage.from_dict(data)

                return message_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_1 = ClientInboundMessageControl.from_dict(data)

                return message_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_2 = ClientInboundMessageSay.from_dict(data)

                return message_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_3 = ClientInboundMessageEndCall.from_dict(data)

                return message_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            message_type_4 = ClientInboundMessageTransfer.from_dict(data)

            return message_type_4

        message = _parse_message(d.pop("message"))

        client_inbound_message = cls(
            message=message,
        )

        client_inbound_message.additional_properties = d
        return client_inbound_message

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
