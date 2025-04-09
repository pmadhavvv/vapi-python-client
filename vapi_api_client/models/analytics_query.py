from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analytics_query_group_by import AnalyticsQueryGroupBy
from ..models.analytics_query_table import AnalyticsQueryTable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_operation import AnalyticsOperation
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="AnalyticsQuery")


@_attrs_define
class AnalyticsQuery:
    """
    Attributes:
        table (AnalyticsQueryTable): This is the table you want to query.
        name (str): This is the name of the query. This will be used to identify the query in the response.
        operations (list['AnalyticsOperation']): This is the list of operations you want to perform.
        group_by (Union[Unset, AnalyticsQueryGroupBy]): This is the list of columns you want to group by.
        time_range (Union[Unset, TimeRange]):
    """

    table: AnalyticsQueryTable
    name: str
    operations: list["AnalyticsOperation"]
    group_by: Union[Unset, AnalyticsQueryGroupBy] = UNSET
    time_range: Union[Unset, "TimeRange"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table = self.table.value

        name = self.name

        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.to_dict()
            operations.append(operations_item)

        group_by: Union[Unset, str] = UNSET
        if not isinstance(self.group_by, Unset):
            group_by = self.group_by.value

        time_range: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "table": table,
                "name": name,
                "operations": operations,
            }
        )
        if group_by is not UNSET:
            field_dict["groupBy"] = group_by
        if time_range is not UNSET:
            field_dict["timeRange"] = time_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_operation import AnalyticsOperation
        from ..models.time_range import TimeRange

        d = dict(src_dict)
        table = AnalyticsQueryTable(d.pop("table"))

        name = d.pop("name")

        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:
            operations_item = AnalyticsOperation.from_dict(operations_item_data)

            operations.append(operations_item)

        _group_by = d.pop("groupBy", UNSET)
        group_by: Union[Unset, AnalyticsQueryGroupBy]
        if isinstance(_group_by, Unset):
            group_by = UNSET
        else:
            group_by = AnalyticsQueryGroupBy(_group_by)

        _time_range = d.pop("timeRange", UNSET)
        time_range: Union[Unset, TimeRange]
        if isinstance(_time_range, Unset):
            time_range = UNSET
        else:
            time_range = TimeRange.from_dict(_time_range)

        analytics_query = cls(
            table=table,
            name=name,
            operations=operations,
            group_by=group_by,
            time_range=time_range,
        )

        analytics_query.additional_properties = d
        return analytics_query

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
