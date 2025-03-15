from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analysis_cost_analysis_type import AnalysisCostAnalysisType
from ..models.analysis_cost_type import AnalysisCostType

if TYPE_CHECKING:
    from ..models.analysis_cost_model import AnalysisCostModel


T = TypeVar("T", bound="AnalysisCost")


@_attrs_define
class AnalysisCost:
    """
    Attributes:
        type_ (AnalysisCostType): This is the type of cost, always 'analysis' for this class.
        analysis_type (AnalysisCostAnalysisType): This is the type of analysis performed.
        model (AnalysisCostModel): This is the model that was used to perform the analysis.
        prompt_tokens (float): This is the number of prompt tokens used in the analysis.
        completion_tokens (float): This is the number of completion tokens generated in the analysis.
        cost (float): This is the cost of the component in USD.
    """

    type_: AnalysisCostType
    analysis_type: AnalysisCostAnalysisType
    model: "AnalysisCostModel"
    prompt_tokens: float
    completion_tokens: float
    cost: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        analysis_type = self.analysis_type.value

        model = self.model.to_dict()

        prompt_tokens = self.prompt_tokens

        completion_tokens = self.completion_tokens

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "analysisType": analysis_type,
                "model": model,
                "promptTokens": prompt_tokens,
                "completionTokens": completion_tokens,
                "cost": cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.analysis_cost_model import AnalysisCostModel

        d = src_dict.copy()
        type_ = AnalysisCostType(d.pop("type"))

        analysis_type = AnalysisCostAnalysisType(d.pop("analysisType"))

        model = AnalysisCostModel.from_dict(d.pop("model"))

        prompt_tokens = d.pop("promptTokens")

        completion_tokens = d.pop("completionTokens")

        cost = d.pop("cost")

        analysis_cost = cls(
            type_=type_,
            analysis_type=analysis_type,
            model=model,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            cost=cost,
        )

        analysis_cost.additional_properties = d
        return analysis_cost

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
