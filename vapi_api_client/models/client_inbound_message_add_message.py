from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_inbound_message_add_message_type import ClientInboundMessageAddMessageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_ai_message import OpenAIMessage


T = TypeVar("T", bound="ClientInboundMessageAddMessage")


@_attrs_define
class ClientInboundMessageAddMessage:
    """
    Attributes:
        type_ (ClientInboundMessageAddMessageType): This is the type of the message. Send "add-message" message to add a
            message to the conversation history.
        message (OpenAIMessage):
        trigger_response_enabled (Union[Unset, bool]): This is the flag to trigger a response, or to insert the message
            into the conversation history silently. Defaults to `true`.

            Usage:
            - Use `true` to trigger a response.
            - Use `false` to insert the message into the conversation history silently.

            @default true
    """

    type_: ClientInboundMessageAddMessageType
    message: "OpenAIMessage"
    trigger_response_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        message = self.message.to_dict()

        trigger_response_enabled = self.trigger_response_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "message": message,
            }
        )
        if trigger_response_enabled is not UNSET:
            field_dict["triggerResponseEnabled"] = trigger_response_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_ai_message import OpenAIMessage

        d = dict(src_dict)
        type_ = ClientInboundMessageAddMessageType(d.pop("type"))

        message = OpenAIMessage.from_dict(d.pop("message"))

        trigger_response_enabled = d.pop("triggerResponseEnabled", UNSET)

        client_inbound_message_add_message = cls(
            type_=type_,
            message=message,
            trigger_response_enabled=trigger_response_enabled,
        )

        client_inbound_message_add_message.additional_properties = d
        return client_inbound_message_add_message

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
