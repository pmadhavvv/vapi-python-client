from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.success_evaluation_plan_rubric import SuccessEvaluationPlanRubric
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.success_evaluation_plan_messages_item import SuccessEvaluationPlanMessagesItem


T = TypeVar("T", bound="SuccessEvaluationPlan")


@_attrs_define
class SuccessEvaluationPlan:
    r"""
    Attributes:
        rubric (Union[Unset, SuccessEvaluationPlanRubric]): This enforces the rubric of the evaluation. The output is
            stored in `call.analysis.successEvaluation`.

            Options include:
            - 'NumericScale': A scale of 1 to 10.
            - 'DescriptiveScale': A scale of Excellent, Good, Fair, Poor.
            - 'Checklist': A checklist of criteria and their status.
            - 'Matrix': A grid that evaluates multiple criteria across different performance levels.
            - 'PercentageScale': A scale of 0% to 100%.
            - 'LikertScale': A scale of Strongly Agree, Agree, Neutral, Disagree, Strongly Disagree.
            - 'AutomaticRubric': Automatically break down evaluation into several criteria, each with its own score.
            - 'PassFail': A simple 'true' if call passed, 'false' if not.

            Default is 'PassFail'.
        messages (Union[Unset, list['SuccessEvaluationPlanMessagesItem']]): These are the messages used to generate the
            success evaluation.

            @default: ```
            [
              {
                "role": "system",
                "content": "You are an expert call evaluator. You will be given a transcript of a call and the system prompt
            of the AI participant. Determine if the call was successful based on the objectives inferred from the system
            prompt. DO NOT return anything except the result.\n\nRubric:\\n{{rubric}}\n\nOnly respond with the result."
              },
              {
                "role": "user",
                "content": "Here is the transcript:\n\n{{transcript}}\n\n"
              },
              {
                "role": "user",
                "content": "Here was the system prompt of the call:\n\n{{systemPrompt}}\n\n"
              }
            ]```

            You can customize by providing any messages you want.

            Here are the template variables available:
            - {{transcript}}: the transcript of the call from `call.artifact.transcript`- {{systemPrompt}}: the system
            prompt of the call from `assistant.model.messages[type=system].content`- {{rubric}}: the rubric of the success
            evaluation from `successEvaluationPlan.rubric`
        enabled (Union[Unset, bool]): This determines whether a success evaluation is generated and stored in
            `call.analysis.successEvaluation`. Defaults to true.

            Usage:
            - If you want to disable the success evaluation, set this to false.

            @default true
        timeout_seconds (Union[Unset, float]): This is how long the request is tried before giving up. When request
            times out, `call.analysis.successEvaluation` will be empty.

            Usage:
            - To guarantee the success evaluation is generated, set this value high. Note, this will delay the end of call
            report in cases where model is slow to respond.

            @default 5 seconds
    """

    rubric: Union[Unset, SuccessEvaluationPlanRubric] = UNSET
    messages: Union[Unset, list["SuccessEvaluationPlanMessagesItem"]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    timeout_seconds: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rubric: Union[Unset, str] = UNSET
        if not isinstance(self.rubric, Unset):
            rubric = self.rubric.value

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
        if rubric is not UNSET:
            field_dict["rubric"] = rubric
        if messages is not UNSET:
            field_dict["messages"] = messages
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.success_evaluation_plan_messages_item import SuccessEvaluationPlanMessagesItem

        d = dict(src_dict)
        _rubric = d.pop("rubric", UNSET)
        rubric: Union[Unset, SuccessEvaluationPlanRubric]
        if isinstance(_rubric, Unset):
            rubric = UNSET
        else:
            rubric = SuccessEvaluationPlanRubric(_rubric)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = SuccessEvaluationPlanMessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        enabled = d.pop("enabled", UNSET)

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        success_evaluation_plan = cls(
            rubric=rubric,
            messages=messages,
            enabled=enabled,
            timeout_seconds=timeout_seconds,
        )

        success_evaluation_plan.additional_properties = d
        return success_evaluation_plan

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
