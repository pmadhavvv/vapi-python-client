from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserMessage")


@_attrs_define
class UserMessage:
    """
    Attributes:
        role (str): The role of the user in the conversation.
        message (str): The message content from the user.
        time (float): The timestamp when the message was sent.
        end_time (float): The timestamp when the message ended.
        seconds_from_start (float): The number of seconds from the start of the conversation.
        duration (Union[Unset, float]): The duration of the message in seconds.
    """

    role: str
    message: str
    time: float
    end_time: float
    seconds_from_start: float
    duration: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        message = self.message

        time = self.time

        end_time = self.end_time

        seconds_from_start = self.seconds_from_start

        duration = self.duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "message": message,
                "time": time,
                "endTime": end_time,
                "secondsFromStart": seconds_from_start,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        role = d.pop("role")

        message = d.pop("message")

        time = d.pop("time")

        end_time = d.pop("endTime")

        seconds_from_start = d.pop("secondsFromStart")

        duration = d.pop("duration", UNSET)

        user_message = cls(
            role=role,
            message=message,
            time=time,
            end_time=end_time,
            seconds_from_start=seconds_from_start,
            duration=duration,
        )

        user_message.additional_properties = d
        return user_message

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
