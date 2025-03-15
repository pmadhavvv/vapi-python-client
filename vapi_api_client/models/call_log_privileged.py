import datetime
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.call_log_privileged_level import CallLogPrivilegedLevel

T = TypeVar("T", bound="CallLogPrivileged")


@_attrs_define
class CallLogPrivileged:
    """
    Attributes:
        call_id (str): This is the unique identifier for the call.
        org_id (str): This is the unique identifier for the org that this call log belongs to.
        log (str): This is the log message associated with the call.
        level (CallLogPrivilegedLevel): This is the level of the log message.
        time (datetime.datetime): This is the ISO 8601 date-time string of when the log was created.
    """

    call_id: str
    org_id: str
    log: str
    level: CallLogPrivilegedLevel
    time: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_id = self.call_id

        org_id = self.org_id

        log = self.log

        level = self.level.value

        time = self.time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "callId": call_id,
                "orgId": org_id,
                "log": log,
                "level": level,
                "time": time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        call_id = d.pop("callId")

        org_id = d.pop("orgId")

        log = d.pop("log")

        level = CallLogPrivilegedLevel(d.pop("level"))

        time = isoparse(d.pop("time"))

        call_log_privileged = cls(
            call_id=call_id,
            org_id=org_id,
            log=log,
            level=level,
            time=time,
        )

        call_log_privileged.additional_properties = d
        return call_log_privileged

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
