from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.structured_data_plan import StructuredDataPlan
    from ..models.success_evaluation_plan import SuccessEvaluationPlan
    from ..models.summary_plan import SummaryPlan


T = TypeVar("T", bound="AnalysisPlan")


@_attrs_define
class AnalysisPlan:
    """
    Attributes:
        summary_plan (Union[Unset, SummaryPlan]):
        structured_data_plan (Union[Unset, StructuredDataPlan]):
        success_evaluation_plan (Union[Unset, SuccessEvaluationPlan]):
    """

    summary_plan: Union[Unset, "SummaryPlan"] = UNSET
    structured_data_plan: Union[Unset, "StructuredDataPlan"] = UNSET
    success_evaluation_plan: Union[Unset, "SuccessEvaluationPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.summary_plan, Unset):
            summary_plan = self.summary_plan.to_dict()

        structured_data_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.structured_data_plan, Unset):
            structured_data_plan = self.structured_data_plan.to_dict()

        success_evaluation_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.success_evaluation_plan, Unset):
            success_evaluation_plan = self.success_evaluation_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary_plan is not UNSET:
            field_dict["summaryPlan"] = summary_plan
        if structured_data_plan is not UNSET:
            field_dict["structuredDataPlan"] = structured_data_plan
        if success_evaluation_plan is not UNSET:
            field_dict["successEvaluationPlan"] = success_evaluation_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structured_data_plan import StructuredDataPlan
        from ..models.success_evaluation_plan import SuccessEvaluationPlan
        from ..models.summary_plan import SummaryPlan

        d = dict(src_dict)
        _summary_plan = d.pop("summaryPlan", UNSET)
        summary_plan: Union[Unset, SummaryPlan]
        if isinstance(_summary_plan, Unset):
            summary_plan = UNSET
        else:
            summary_plan = SummaryPlan.from_dict(_summary_plan)

        _structured_data_plan = d.pop("structuredDataPlan", UNSET)
        structured_data_plan: Union[Unset, StructuredDataPlan]
        if isinstance(_structured_data_plan, Unset):
            structured_data_plan = UNSET
        else:
            structured_data_plan = StructuredDataPlan.from_dict(_structured_data_plan)

        _success_evaluation_plan = d.pop("successEvaluationPlan", UNSET)
        success_evaluation_plan: Union[Unset, SuccessEvaluationPlan]
        if isinstance(_success_evaluation_plan, Unset):
            success_evaluation_plan = UNSET
        else:
            success_evaluation_plan = SuccessEvaluationPlan.from_dict(_success_evaluation_plan)

        analysis_plan = cls(
            summary_plan=summary_plan,
            structured_data_plan=structured_data_plan,
            success_evaluation_plan=success_evaluation_plan,
        )

        analysis_plan.additional_properties = d
        return analysis_plan

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
