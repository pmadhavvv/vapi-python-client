from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analytics_operation_column import AnalyticsOperationColumn
from ..models.analytics_operation_operation import AnalyticsOperationOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsOperation")


@_attrs_define
class AnalyticsOperation:
    """
    Attributes:
        operation (AnalyticsOperationOperation): This is the aggregation operation you want to perform.
        column (AnalyticsOperationColumn): This is the columns you want to perform the aggregation operation on.
        alias (Union[Unset, str]): This is the alias for column name returned. Defaults to `${operation}${column}`.
    """

    operation: AnalyticsOperationOperation
    column: AnalyticsOperationColumn
    alias: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation = self.operation.value

        column = self.column.value

        alias = self.alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
                "column": column,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation = AnalyticsOperationOperation(d.pop("operation"))

        column = AnalyticsOperationColumn(d.pop("column"))

        alias = d.pop("alias", UNSET)

        analytics_operation = cls(
            operation=operation,
            column=column,
            alias=alias,
        )

        analytics_operation.additional_properties = d
        return analytics_operation

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
