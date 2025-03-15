from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analysis_structured_data import AnalysisStructuredData


T = TypeVar("T", bound="Analysis")


@_attrs_define
class Analysis:
    """
    Attributes:
        summary (Union[Unset, str]): This is the summary of the call. Customize by setting
            `assistant.analysisPlan.summaryPrompt`.
        structured_data (Union[Unset, AnalysisStructuredData]): This is the structured data extracted from the call.
            Customize by setting `assistant.analysisPlan.structuredDataPrompt` and/or
            `assistant.analysisPlan.structuredDataSchema`.
        success_evaluation (Union[Unset, str]): This is the evaluation of the call. Customize by setting
            `assistant.analysisPlan.successEvaluationPrompt` and/or `assistant.analysisPlan.successEvaluationRubric`.
    """

    summary: Union[Unset, str] = UNSET
    structured_data: Union[Unset, "AnalysisStructuredData"] = UNSET
    success_evaluation: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary

        structured_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.structured_data, Unset):
            structured_data = self.structured_data.to_dict()

        success_evaluation = self.success_evaluation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary is not UNSET:
            field_dict["summary"] = summary
        if structured_data is not UNSET:
            field_dict["structuredData"] = structured_data
        if success_evaluation is not UNSET:
            field_dict["successEvaluation"] = success_evaluation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.analysis_structured_data import AnalysisStructuredData

        d = src_dict.copy()
        summary = d.pop("summary", UNSET)

        _structured_data = d.pop("structuredData", UNSET)
        structured_data: Union[Unset, AnalysisStructuredData]
        if isinstance(_structured_data, Unset):
            structured_data = UNSET
        else:
            structured_data = AnalysisStructuredData.from_dict(_structured_data)

        success_evaluation = d.pop("successEvaluation", UNSET)

        analysis = cls(
            summary=summary,
            structured_data=structured_data,
            success_evaluation=success_evaluation,
        )

        analysis.additional_properties = d
        return analysis

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
