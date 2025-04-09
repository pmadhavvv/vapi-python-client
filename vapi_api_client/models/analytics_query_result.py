from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.analytics_query_result_result_item import AnalyticsQueryResultResultItem
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="AnalyticsQueryResult")


@_attrs_define
class AnalyticsQueryResult:
    """
    Attributes:
        name (str): This is the unique key for the query.
        time_range (TimeRange):
        result (list['AnalyticsQueryResultResultItem']): This is the result of the query, a list of unique groups with
            result of their aggregations.

            Example:
            "result": [
              { "date": "2023-01-01", "assistantId": "123", "endedReason": "customer-ended-call", "sumDuration": 120,
            "avgCost": 10.5 },
              { "date": "2023-01-02", "assistantId": "123", "endedReason": "customer-did-not-give-microphone-permission",
            "sumDuration": 0, "avgCost": 0 },
              // Additional results
            ]
    """

    name: str
    time_range: "TimeRange"
    result: list["AnalyticsQueryResultResultItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        time_range = self.time_range.to_dict()

        result = []
        for result_item_data in self.result:
            result_item = result_item_data.to_dict()
            result.append(result_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "timeRange": time_range,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_query_result_result_item import AnalyticsQueryResultResultItem
        from ..models.time_range import TimeRange

        d = dict(src_dict)
        name = d.pop("name")

        time_range = TimeRange.from_dict(d.pop("timeRange"))

        result = []
        _result = d.pop("result")
        for result_item_data in _result:
            result_item = AnalyticsQueryResultResultItem.from_dict(result_item_data)

            result.append(result_item)

        analytics_query_result = cls(
            name=name,
            time_range=time_range,
            result=result,
        )

        analytics_query_result.additional_properties = d
        return analytics_query_result

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
