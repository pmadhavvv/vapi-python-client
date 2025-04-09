from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.google_voicemail_detection_plan_provider import GoogleVoicemailDetectionPlanProvider

T = TypeVar("T", bound="GoogleVoicemailDetectionPlan")


@_attrs_define
class GoogleVoicemailDetectionPlan:
    """
    Attributes:
        provider (GoogleVoicemailDetectionPlanProvider): This is the provider to use for voicemail detection.
        voicemail_expected_duration_seconds (float): This is how long should we listen in order to determine if we were
            sent to voicemail or not?

            @default 15
    """

    provider: GoogleVoicemailDetectionPlanProvider
    voicemail_expected_duration_seconds: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        voicemail_expected_duration_seconds = self.voicemail_expected_duration_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "voicemailExpectedDurationSeconds": voicemail_expected_duration_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = GoogleVoicemailDetectionPlanProvider(d.pop("provider"))

        voicemail_expected_duration_seconds = d.pop("voicemailExpectedDurationSeconds")

        google_voicemail_detection_plan = cls(
            provider=provider,
            voicemail_expected_duration_seconds=voicemail_expected_duration_seconds,
        )

        google_voicemail_detection_plan.additional_properties = d
        return google_voicemail_detection_plan

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
