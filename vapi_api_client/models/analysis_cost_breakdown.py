from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalysisCostBreakdown")


@_attrs_define
class AnalysisCostBreakdown:
    """
    Attributes:
        summary (Union[Unset, float]): This is the cost to summarize the call.
        summary_prompt_tokens (Union[Unset, float]): This is the number of prompt tokens used to summarize the call.
        summary_completion_tokens (Union[Unset, float]): This is the number of completion tokens used to summarize the
            call.
        structured_data (Union[Unset, float]): This is the cost to extract structured data from the call.
        structured_data_prompt_tokens (Union[Unset, float]): This is the number of prompt tokens used to extract
            structured data from the call.
        structured_data_completion_tokens (Union[Unset, float]): This is the number of completion tokens used to extract
            structured data from the call.
        success_evaluation (Union[Unset, float]): This is the cost to evaluate if the call was successful.
        success_evaluation_prompt_tokens (Union[Unset, float]): This is the number of prompt tokens used to evaluate if
            the call was successful.
        success_evaluation_completion_tokens (Union[Unset, float]): This is the number of completion tokens used to
            evaluate if the call was successful.
    """

    summary: Union[Unset, float] = UNSET
    summary_prompt_tokens: Union[Unset, float] = UNSET
    summary_completion_tokens: Union[Unset, float] = UNSET
    structured_data: Union[Unset, float] = UNSET
    structured_data_prompt_tokens: Union[Unset, float] = UNSET
    structured_data_completion_tokens: Union[Unset, float] = UNSET
    success_evaluation: Union[Unset, float] = UNSET
    success_evaluation_prompt_tokens: Union[Unset, float] = UNSET
    success_evaluation_completion_tokens: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary

        summary_prompt_tokens = self.summary_prompt_tokens

        summary_completion_tokens = self.summary_completion_tokens

        structured_data = self.structured_data

        structured_data_prompt_tokens = self.structured_data_prompt_tokens

        structured_data_completion_tokens = self.structured_data_completion_tokens

        success_evaluation = self.success_evaluation

        success_evaluation_prompt_tokens = self.success_evaluation_prompt_tokens

        success_evaluation_completion_tokens = self.success_evaluation_completion_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary is not UNSET:
            field_dict["summary"] = summary
        if summary_prompt_tokens is not UNSET:
            field_dict["summaryPromptTokens"] = summary_prompt_tokens
        if summary_completion_tokens is not UNSET:
            field_dict["summaryCompletionTokens"] = summary_completion_tokens
        if structured_data is not UNSET:
            field_dict["structuredData"] = structured_data
        if structured_data_prompt_tokens is not UNSET:
            field_dict["structuredDataPromptTokens"] = structured_data_prompt_tokens
        if structured_data_completion_tokens is not UNSET:
            field_dict["structuredDataCompletionTokens"] = structured_data_completion_tokens
        if success_evaluation is not UNSET:
            field_dict["successEvaluation"] = success_evaluation
        if success_evaluation_prompt_tokens is not UNSET:
            field_dict["successEvaluationPromptTokens"] = success_evaluation_prompt_tokens
        if success_evaluation_completion_tokens is not UNSET:
            field_dict["successEvaluationCompletionTokens"] = success_evaluation_completion_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        summary = d.pop("summary", UNSET)

        summary_prompt_tokens = d.pop("summaryPromptTokens", UNSET)

        summary_completion_tokens = d.pop("summaryCompletionTokens", UNSET)

        structured_data = d.pop("structuredData", UNSET)

        structured_data_prompt_tokens = d.pop("structuredDataPromptTokens", UNSET)

        structured_data_completion_tokens = d.pop("structuredDataCompletionTokens", UNSET)

        success_evaluation = d.pop("successEvaluation", UNSET)

        success_evaluation_prompt_tokens = d.pop("successEvaluationPromptTokens", UNSET)

        success_evaluation_completion_tokens = d.pop("successEvaluationCompletionTokens", UNSET)

        analysis_cost_breakdown = cls(
            summary=summary,
            summary_prompt_tokens=summary_prompt_tokens,
            summary_completion_tokens=summary_completion_tokens,
            structured_data=structured_data,
            structured_data_prompt_tokens=structured_data_prompt_tokens,
            structured_data_completion_tokens=structured_data_completion_tokens,
            success_evaluation=success_evaluation,
            success_evaluation_prompt_tokens=success_evaluation_prompt_tokens,
            success_evaluation_completion_tokens=success_evaluation_completion_tokens,
        )

        analysis_cost_breakdown.additional_properties = d
        return analysis_cost_breakdown

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
