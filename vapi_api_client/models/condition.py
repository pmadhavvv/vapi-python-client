from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.condition_operator import ConditionOperator

if TYPE_CHECKING:
    from ..models.condition_value import ConditionValue


T = TypeVar("T", bound="Condition")


@_attrs_define
class Condition:
    """
    Attributes:
        operator (ConditionOperator): This is the operator you want to use to compare the parameter and value.
        param (str): This is the name of the parameter that you want to check.
        value (ConditionValue): This is the value you want to compare against the parameter.
    """

    operator: ConditionOperator
    param: str
    value: "ConditionValue"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator.value

        param = self.param

        value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operator": operator,
                "param": param,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.condition_value import ConditionValue

        d = src_dict.copy()
        operator = ConditionOperator(d.pop("operator"))

        param = d.pop("param")

        value = ConditionValue.from_dict(d.pop("value"))

        condition = cls(
            operator=operator,
            param=param,
            value=value,
        )

        condition.additional_properties = d
        return condition

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
