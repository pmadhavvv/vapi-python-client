from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessagePlan")


@_attrs_define
class MessagePlan:
    """
    Attributes:
        idle_messages (Union[Unset, list[str]]): This are the messages that the assistant will speak when the user
            hasn't responded for `idleTimeoutSeconds`. Each time the timeout is triggered, a random message will be chosen
            from this array.

            Usage:
            - If user gets distracted and doesn't respond for a while, this can be used to grab their attention.
            - If the transcriber doesn't pick up what the user said, this can be used to ask the user to repeat themselves.
            (From the perspective of the assistant, the conversation is idle since it didn't "hear" any user messages.)

            @default null (no idle message is spoken)
        idle_message_max_spoken_count (Union[Unset, float]): This determines the maximum number of times `idleMessages`
            can be spoken during the call.

            @default 3
        idle_timeout_seconds (Union[Unset, float]): This is the timeout in seconds before a message from `idleMessages`
            is spoken. The clock starts when the assistant finishes speaking and remains active until the user speaks.

            @default 10
        silence_timeout_message (Union[Unset, str]): This is the message that the assistant will say if the call ends
            due to silence.

            If unspecified, it will hang up without saying anything.
    """

    idle_messages: Union[Unset, list[str]] = UNSET
    idle_message_max_spoken_count: Union[Unset, float] = UNSET
    idle_timeout_seconds: Union[Unset, float] = UNSET
    silence_timeout_message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idle_messages: Union[Unset, list[str]] = UNSET
        if not isinstance(self.idle_messages, Unset):
            idle_messages = self.idle_messages

        idle_message_max_spoken_count = self.idle_message_max_spoken_count

        idle_timeout_seconds = self.idle_timeout_seconds

        silence_timeout_message = self.silence_timeout_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idle_messages is not UNSET:
            field_dict["idleMessages"] = idle_messages
        if idle_message_max_spoken_count is not UNSET:
            field_dict["idleMessageMaxSpokenCount"] = idle_message_max_spoken_count
        if idle_timeout_seconds is not UNSET:
            field_dict["idleTimeoutSeconds"] = idle_timeout_seconds
        if silence_timeout_message is not UNSET:
            field_dict["silenceTimeoutMessage"] = silence_timeout_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        idle_messages = cast(list[str], d.pop("idleMessages", UNSET))

        idle_message_max_spoken_count = d.pop("idleMessageMaxSpokenCount", UNSET)

        idle_timeout_seconds = d.pop("idleTimeoutSeconds", UNSET)

        silence_timeout_message = d.pop("silenceTimeoutMessage", UNSET)

        message_plan = cls(
            idle_messages=idle_messages,
            idle_message_max_spoken_count=idle_message_max_spoken_count,
            idle_timeout_seconds=idle_timeout_seconds,
            silence_timeout_message=silence_timeout_message,
        )

        message_plan.additional_properties = d
        return message_plan

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
