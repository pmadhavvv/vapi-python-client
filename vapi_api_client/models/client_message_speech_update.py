from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_message_speech_update_role import ClientMessageSpeechUpdateRole
from ..models.client_message_speech_update_status import ClientMessageSpeechUpdateStatus
from ..models.client_message_speech_update_type import ClientMessageSpeechUpdateType

T = TypeVar("T", bound="ClientMessageSpeechUpdate")


@_attrs_define
class ClientMessageSpeechUpdate:
    """
    Attributes:
        type_ (ClientMessageSpeechUpdateType): This is the type of the message. "speech-update" is sent whenever
            assistant or user start or stop speaking.
        status (ClientMessageSpeechUpdateStatus): This is the status of the speech update.
        role (ClientMessageSpeechUpdateRole): This is the role which the speech update is for.
    """

    type_: ClientMessageSpeechUpdateType
    status: ClientMessageSpeechUpdateStatus
    role: ClientMessageSpeechUpdateRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        status = self.status.value

        role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "status": status,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ClientMessageSpeechUpdateType(d.pop("type"))

        status = ClientMessageSpeechUpdateStatus(d.pop("status"))

        role = ClientMessageSpeechUpdateRole(d.pop("role"))

        client_message_speech_update = cls(
            type_=type_,
            status=status,
            role=role,
        )

        client_message_speech_update.additional_properties = d
        return client_message_speech_update

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
