from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BotMessage")


@_attrs_define
class BotMessage:
    """
    Attributes:
        role (str): The role of the bot in the conversation.
        message (str): The message content from the bot.
        time (float): The timestamp when the message was sent.
        end_time (float): The timestamp when the message ended.
        seconds_from_start (float): The number of seconds from the start of the conversation.
        source (Union[Unset, str]): The source of the message.
        duration (Union[Unset, float]): The duration of the message in seconds.
    """

    role: str
    message: str
    time: float
    end_time: float
    seconds_from_start: float
    source: Union[Unset, str] = UNSET
    duration: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        message = self.message

        time = self.time

        end_time = self.end_time

        seconds_from_start = self.seconds_from_start

        source = self.source

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
        if source is not UNSET:
            field_dict["source"] = source
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = d.pop("role")

        message = d.pop("message")

        time = d.pop("time")

        end_time = d.pop("endTime")

        seconds_from_start = d.pop("secondsFromStart")

        source = d.pop("source", UNSET)

        duration = d.pop("duration", UNSET)

        bot_message = cls(
            role=role,
            message=message,
            time=time,
            end_time=end_time,
            seconds_from_start=seconds_from_start,
            source=source,
            duration=duration,
        )

        bot_message.additional_properties = d
        return bot_message

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
