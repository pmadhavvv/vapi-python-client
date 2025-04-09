from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.logic_edge_condition_type import LogicEdgeConditionType

T = TypeVar("T", bound="LogicEdgeCondition")


@_attrs_define
class LogicEdgeCondition:
    """
    Attributes:
        type_ (LogicEdgeConditionType):
        liquid (str):
    """

    type_: LogicEdgeConditionType
    liquid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        liquid = self.liquid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "liquid": liquid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = LogicEdgeConditionType(d.pop("type"))

        liquid = d.pop("liquid")

        logic_edge_condition = cls(
            type_=type_,
            liquid=liquid,
        )

        logic_edge_condition.additional_properties = d
        return logic_edge_condition

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
