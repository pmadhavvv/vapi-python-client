from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.analytics_query import AnalyticsQuery


T = TypeVar("T", bound="AnalyticsQueryDTO")


@_attrs_define
class AnalyticsQueryDTO:
    """
    Attributes:
        queries (list['AnalyticsQuery']): This is the list of metric queries you want to perform.
    """

    queries: list["AnalyticsQuery"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queries = []
        for queries_item_data in self.queries:
            queries_item = queries_item_data.to_dict()
            queries.append(queries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queries": queries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.analytics_query import AnalyticsQuery

        d = src_dict.copy()
        queries = []
        _queries = d.pop("queries")
        for queries_item_data in _queries:
            queries_item = AnalyticsQuery.from_dict(queries_item_data)

            queries.append(queries_item)

        analytics_query_dto = cls(
            queries=queries,
        )

        analytics_query_dto.additional_properties = d
        return analytics_query_dto

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
