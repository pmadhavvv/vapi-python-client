from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerMessageStatusUpdateInboundPhoneCallDebuggingArtifacts")


@_attrs_define
class ServerMessageStatusUpdateInboundPhoneCallDebuggingArtifacts:
    """This is the inbound phone call debugging artifacts. This is only sent if the status is "ended" and there was an
    error accepting the inbound phone call.

    This will include any errors related to the "assistant-request" if one was made.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        server_message_status_update_inbound_phone_call_debugging_artifacts = cls()

        server_message_status_update_inbound_phone_call_debugging_artifacts.additional_properties = d
        return server_message_status_update_inbound_phone_call_debugging_artifacts

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
