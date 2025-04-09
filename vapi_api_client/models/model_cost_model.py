from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelCostModel")


@_attrs_define
class ModelCostModel:
    """This is the model that was used during the call.

    This matches one of the following:
    - `call.assistant.model`,
    - `call.assistantId->model`,
    - `call.squad[n].assistant.model`,
    - `call.squad[n].assistantId->model`,
    - `call.squadId->[n].assistant.model`,
    - `call.squadId->[n].assistantId->model`.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_cost_model = cls()

        model_cost_model.additional_properties = d
        return model_cost_model

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
