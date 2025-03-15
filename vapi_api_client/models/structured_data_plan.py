from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_schema import JsonSchema
    from ..models.structured_data_plan_messages_item import StructuredDataPlanMessagesItem


T = TypeVar("T", bound="StructuredDataPlan")


@_attrs_define
class StructuredDataPlan:
    r"""
    Attributes:
        messages (Union[Unset, list['StructuredDataPlanMessagesItem']]): These are the messages used to generate the
            structured data.

            @default: ```
            [
              {
                "role": "system",
                "content": "You are an expert data extractor. You will be given a transcript of a call. Extract structured
            data per the JSON Schema. DO NOT return anything except the structured data.\n\nJson
            Schema:\\n{{schema}}\n\nOnly respond with the JSON."
              },
              {
                "role": "user",
                "content": "Here is the transcript:\n\n{{transcript}}\n\n"
              }
            ]```

            You can customize by providing any messages you want.

            Here are the template variables available:
            - {{transcript}}: the transcript of the call from `call.artifact.transcript`- {{systemPrompt}}: the system
            prompt of the call from `assistant.model.messages[type=system].content`- {{schema}}: the schema of the
            structured data from `structuredDataPlan.schema`
        enabled (Union[Unset, bool]): This determines whether structured data is generated and stored in
            `call.analysis.structuredData`. Defaults to false.

            Usage:
            - If you want to extract structured data, set this to true and provide a `schema`.

            @default false
        schema (Union[Unset, JsonSchema]):
        timeout_seconds (Union[Unset, float]): This is how long the request is tried before giving up. When request
            times out, `call.analysis.structuredData` will be empty.

            Usage:
            - To guarantee the structured data is generated, set this value high. Note, this will delay the end of call
            report in cases where model is slow to respond.

            @default 5 seconds
    """

    messages: Union[Unset, list["StructuredDataPlanMessagesItem"]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    schema: Union[Unset, "JsonSchema"] = UNSET
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

        schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        timeout_seconds = self.timeout_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if messages is not UNSET:
            field_dict["messages"] = messages
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if schema is not UNSET:
            field_dict["schema"] = schema
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.json_schema import JsonSchema
        from ..models.structured_data_plan_messages_item import StructuredDataPlanMessagesItem

        d = src_dict.copy()
        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = StructuredDataPlanMessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        enabled = d.pop("enabled", UNSET)

        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, JsonSchema]
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = JsonSchema.from_dict(_schema)

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        structured_data_plan = cls(
            messages=messages,
            enabled=enabled,
            schema=schema,
            timeout_seconds=timeout_seconds,
        )

        structured_data_plan.additional_properties = d
        return structured_data_plan

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
