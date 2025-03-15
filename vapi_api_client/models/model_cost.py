from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_cost_type import ModelCostType

if TYPE_CHECKING:
    from ..models.model_cost_model import ModelCostModel


T = TypeVar("T", bound="ModelCost")


@_attrs_define
class ModelCost:
    """
    Attributes:
        type_ (ModelCostType): This is the type of cost, always 'model' for this class.
        model (ModelCostModel): This is the model that was used during the call.

            This matches one of the following:
            - `call.assistant.model`,
            - `call.assistantId->model`,
            - `call.squad[n].assistant.model`,
            - `call.squad[n].assistantId->model`,
            - `call.squadId->[n].assistant.model`,
            - `call.squadId->[n].assistantId->model`.
        prompt_tokens (float): This is the number of prompt tokens used in the call. These should be total prompt tokens
            used in the call for single assistant calls, while squad calls will have multiple model costs one for each
            assistant that was used.
        completion_tokens (float): This is the number of completion tokens generated in the call. These should be total
            completion tokens used in the call for single assistant calls, while squad calls will have multiple model costs
            one for each assistant that was used.
        cost (float): This is the cost of the component in USD.
    """

    type_: ModelCostType
    model: "ModelCostModel"
    prompt_tokens: float
    completion_tokens: float
    cost: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        model = self.model.to_dict()

        prompt_tokens = self.prompt_tokens

        completion_tokens = self.completion_tokens

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "model": model,
                "promptTokens": prompt_tokens,
                "completionTokens": completion_tokens,
                "cost": cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.model_cost_model import ModelCostModel

        d = src_dict.copy()
        type_ = ModelCostType(d.pop("type"))

        model = ModelCostModel.from_dict(d.pop("model"))

        prompt_tokens = d.pop("promptTokens")

        completion_tokens = d.pop("completionTokens")

        cost = d.pop("cost")

        model_cost = cls(
            type_=type_,
            model=model,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            cost=cost,
        )

        model_cost.additional_properties = d
        return model_cost

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
