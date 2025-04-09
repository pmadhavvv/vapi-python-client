from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metrics_bill_daily_breakdown import MetricsBillDailyBreakdown
    from ..models.metrics_call_count_daily_breakdown import MetricsCallCountDailyBreakdown
    from ..models.metrics_call_minutes_average_daily_breakdown import MetricsCallMinutesAverageDailyBreakdown
    from ..models.metrics_call_minutes_daily_breakdown import MetricsCallMinutesDailyBreakdown


T = TypeVar("T", bound="Metrics")


@_attrs_define
class Metrics:
    """
    Attributes:
        org_id (str):
        range_start (str):
        range_end (str):
        bill (float):
        bill_within_billing_limit (bool):
        bill_daily_breakdown (MetricsBillDailyBreakdown):
        call_active (float):
        call_active_within_concurrency_limit (bool):
        call_minutes (float):
        call_minutes_daily_breakdown (MetricsCallMinutesDailyBreakdown):
        call_minutes_average (float):
        call_minutes_average_daily_breakdown (MetricsCallMinutesAverageDailyBreakdown):
        call_count (float):
        call_count_daily_breakdown (MetricsCallCountDailyBreakdown):
    """

    org_id: str
    range_start: str
    range_end: str
    bill: float
    bill_within_billing_limit: bool
    bill_daily_breakdown: "MetricsBillDailyBreakdown"
    call_active: float
    call_active_within_concurrency_limit: bool
    call_minutes: float
    call_minutes_daily_breakdown: "MetricsCallMinutesDailyBreakdown"
    call_minutes_average: float
    call_minutes_average_daily_breakdown: "MetricsCallMinutesAverageDailyBreakdown"
    call_count: float
    call_count_daily_breakdown: "MetricsCallCountDailyBreakdown"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        range_start = self.range_start

        range_end = self.range_end

        bill = self.bill

        bill_within_billing_limit = self.bill_within_billing_limit

        bill_daily_breakdown = self.bill_daily_breakdown.to_dict()

        call_active = self.call_active

        call_active_within_concurrency_limit = self.call_active_within_concurrency_limit

        call_minutes = self.call_minutes

        call_minutes_daily_breakdown = self.call_minutes_daily_breakdown.to_dict()

        call_minutes_average = self.call_minutes_average

        call_minutes_average_daily_breakdown = self.call_minutes_average_daily_breakdown.to_dict()

        call_count = self.call_count

        call_count_daily_breakdown = self.call_count_daily_breakdown.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orgId": org_id,
                "rangeStart": range_start,
                "rangeEnd": range_end,
                "bill": bill,
                "billWithinBillingLimit": bill_within_billing_limit,
                "billDailyBreakdown": bill_daily_breakdown,
                "callActive": call_active,
                "callActiveWithinConcurrencyLimit": call_active_within_concurrency_limit,
                "callMinutes": call_minutes,
                "callMinutesDailyBreakdown": call_minutes_daily_breakdown,
                "callMinutesAverage": call_minutes_average,
                "callMinutesAverageDailyBreakdown": call_minutes_average_daily_breakdown,
                "callCount": call_count,
                "callCountDailyBreakdown": call_count_daily_breakdown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metrics_bill_daily_breakdown import MetricsBillDailyBreakdown
        from ..models.metrics_call_count_daily_breakdown import MetricsCallCountDailyBreakdown
        from ..models.metrics_call_minutes_average_daily_breakdown import MetricsCallMinutesAverageDailyBreakdown
        from ..models.metrics_call_minutes_daily_breakdown import MetricsCallMinutesDailyBreakdown

        d = dict(src_dict)
        org_id = d.pop("orgId")

        range_start = d.pop("rangeStart")

        range_end = d.pop("rangeEnd")

        bill = d.pop("bill")

        bill_within_billing_limit = d.pop("billWithinBillingLimit")

        bill_daily_breakdown = MetricsBillDailyBreakdown.from_dict(d.pop("billDailyBreakdown"))

        call_active = d.pop("callActive")

        call_active_within_concurrency_limit = d.pop("callActiveWithinConcurrencyLimit")

        call_minutes = d.pop("callMinutes")

        call_minutes_daily_breakdown = MetricsCallMinutesDailyBreakdown.from_dict(d.pop("callMinutesDailyBreakdown"))

        call_minutes_average = d.pop("callMinutesAverage")

        call_minutes_average_daily_breakdown = MetricsCallMinutesAverageDailyBreakdown.from_dict(
            d.pop("callMinutesAverageDailyBreakdown")
        )

        call_count = d.pop("callCount")

        call_count_daily_breakdown = MetricsCallCountDailyBreakdown.from_dict(d.pop("callCountDailyBreakdown"))

        metrics = cls(
            org_id=org_id,
            range_start=range_start,
            range_end=range_end,
            bill=bill,
            bill_within_billing_limit=bill_within_billing_limit,
            bill_daily_breakdown=bill_daily_breakdown,
            call_active=call_active,
            call_active_within_concurrency_limit=call_active_within_concurrency_limit,
            call_minutes=call_minutes,
            call_minutes_daily_breakdown=call_minutes_daily_breakdown,
            call_minutes_average=call_minutes_average,
            call_minutes_average_daily_breakdown=call_minutes_average_daily_breakdown,
            call_count=call_count,
            call_count_daily_breakdown=call_count_daily_breakdown,
        )

        metrics.additional_properties = d
        return metrics

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
