import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.time_range_step import TimeRangeStep
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeRange")


@_attrs_define
class TimeRange:
    """
    Attributes:
        step (Union[Unset, TimeRangeStep]): This is the time step for aggregations.

            If not provided, defaults to returning for the entire time range.
        start (Union[Unset, datetime.datetime]): This is the start date for the time range.

            If not provided, defaults to the 7 days ago.
        end (Union[Unset, datetime.datetime]): This is the end date for the time range.

            If not provided, defaults to now.
        timezone (Union[Unset, str]): This is the timezone you want to set for the query.

            If not provided, defaults to UTC.
    """

    step: Union[Unset, TimeRangeStep] = UNSET
    start: Union[Unset, datetime.datetime] = UNSET
    end: Union[Unset, datetime.datetime] = UNSET
    timezone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step: Union[Unset, str] = UNSET
        if not isinstance(self.step, Unset):
            step = self.step.value

        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: Union[Unset, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if step is not UNSET:
            field_dict["step"] = step
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _step = d.pop("step", UNSET)
        step: Union[Unset, TimeRangeStep]
        if isinstance(_step, Unset):
            step = UNSET
        else:
            step = TimeRangeStep(_step)

        _start = d.pop("start", UNSET)
        start: Union[Unset, datetime.datetime]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        _end = d.pop("end", UNSET)
        end: Union[Unset, datetime.datetime]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        timezone = d.pop("timezone", UNSET)

        time_range = cls(
            step=step,
            start=start,
            end=end,
            timezone=timezone,
        )

        time_range.additional_properties = d
        return time_range

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
