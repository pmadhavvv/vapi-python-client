from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.summary_plan_messages_item import SummaryPlanMessagesItem


T = TypeVar("T", bound="SummaryPlan")


@_attrs_define
class SummaryPlan:
    r"""
    Attributes:
        messages (Union[Unset, list['SummaryPlanMessagesItem']]): These are the messages used to generate the summary.

            @default: ```
            [
              {
                "role": "system",
                "content": "You are an expert note-taker. You will be given a transcript of a call. Summarize the call in
            2-3 sentences. DO NOT return anything except the summary."
              },
              {
                "role": "user",
                "content": "Here is the transcript:\n\n{{transcript}}\n\n"
              }
            ]```

            You can customize by providing any messages you want.

            Here are the template variables available:
            - {{transcript}}: The transcript of the call from `call.artifact.transcript`- {{systemPrompt}}: The system
            prompt of the call from `assistant.model.messages[type=system].content`
        enabled (Union[Unset, bool]): This determines whether a summary is generated and stored in
            `call.analysis.summary`. Defaults to true.

            Usage:
            - If you want to disable the summary, set this to false.

            @default true
        timeout_seconds (Union[Unset, float]): This is how long the request is tried before giving up. When request
            times out, `call.analysis.summary` will be empty.

            Usage:
            - To guarantee the summary is generated, set this value high. Note, this will delay the end of call report in
            cases where model is slow to respond.

            @default 5 seconds
    """

    messages: Union[Unset, list["SummaryPlanMessagesItem"]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    timeout_seconds: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        enabled = self.enabled

        timeout_seconds = self.timeout_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if messages is not UNSET:
            field_dict["messages"] = messages
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.summary_plan_messages_item import SummaryPlanMessagesItem

        d = dict(src_dict)
        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = SummaryPlanMessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        enabled = d.pop("enabled", UNSET)

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        summary_plan = cls(
            messages=messages,
            enabled=enabled,
            timeout_seconds=timeout_seconds,
        )

        summary_plan.additional_properties = d
        return summary_plan

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
