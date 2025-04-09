from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SystemMessage")


@_attrs_define
class SystemMessage:
    """
    Attributes:
        role (str): The role of the system in the conversation.
        message (str): The message content from the system.
        time (float): The timestamp when the message was sent.
        seconds_from_start (float): The number of seconds from the start of the conversation.
    """

    role: str
    message: str
    time: float
    seconds_from_start: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        message = self.message

        time = self.time

        seconds_from_start = self.seconds_from_start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "message": message,
                "time": time,
                "secondsFromStart": seconds_from_start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = d.pop("role")

        message = d.pop("message")

        time = d.pop("time")

        seconds_from_start = d.pop("secondsFromStart")

        system_message = cls(
            role=role,
            message=message,
            time=time,
            seconds_from_start=seconds_from_start,
        )

        system_message.additional_properties = d
        return system_message

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
