from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_inbound_message_say_type import ClientInboundMessageSayType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientInboundMessageSay")


@_attrs_define
class ClientInboundMessageSay:
    """
    Attributes:
        type_ (Union[Unset, ClientInboundMessageSayType]): This is the type of the message. Send "say" message to make
            the assistant say something.
        content (Union[Unset, str]): This is the content to say.
        end_call_after_spoken (Union[Unset, bool]): This is the flag to end call after content is spoken.
    """

    type_: Union[Unset, ClientInboundMessageSayType] = UNSET
    content: Union[Unset, str] = UNSET
    end_call_after_spoken: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        content = self.content

        end_call_after_spoken = self.end_call_after_spoken

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if content is not UNSET:
            field_dict["content"] = content
        if end_call_after_spoken is not UNSET:
            field_dict["endCallAfterSpoken"] = end_call_after_spoken

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ClientInboundMessageSayType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ClientInboundMessageSayType(_type_)

        content = d.pop("content", UNSET)

        end_call_after_spoken = d.pop("endCallAfterSpoken", UNSET)

        client_inbound_message_say = cls(
            type_=type_,
            content=content,
            end_call_after_spoken=end_call_after_spoken,
        )

        client_inbound_message_say.additional_properties = d
        return client_inbound_message_say

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
