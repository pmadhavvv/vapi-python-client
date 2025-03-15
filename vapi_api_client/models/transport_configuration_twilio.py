from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transport_configuration_twilio_provider import TransportConfigurationTwilioProvider
from ..models.transport_configuration_twilio_recording_channels import TransportConfigurationTwilioRecordingChannels
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransportConfigurationTwilio")


@_attrs_define
class TransportConfigurationTwilio:
    """
    Attributes:
        provider (TransportConfigurationTwilioProvider):
        timeout (Union[Unset, float]): The integer number of seconds that we should allow the phone to ring before
            assuming there is no answer.
            The default is `60` seconds and the maximum is `600` seconds.
            For some call flows, we will add a 5-second buffer to the timeout value you provide.
            For this reason, a timeout value of 10 seconds could result in an actual timeout closer to 15 seconds.
            You can set this to a short time, such as `15` seconds, to hang up before reaching an answering machine or
            voicemail.

            @default 60 Example: 60.
        record (Union[Unset, bool]): Whether to record the call.
            Can be `true` to record the phone call, or `false` to not.
            The default is `false`.

            @default false
        recording_channels (Union[Unset, TransportConfigurationTwilioRecordingChannels]): The number of channels in the
            final recording.
            Can be: `mono` or `dual`.
            The default is `mono`.
            `mono` records both legs of the call in a single channel of the recording file.
            `dual` records each leg to a separate channel of the recording file.
            The first channel of a dual-channel recording contains the parent call and the second channel contains the child
            call.

            @default 'mono' Example: mono.
    """

    provider: TransportConfigurationTwilioProvider
    timeout: Union[Unset, float] = UNSET
    record: Union[Unset, bool] = UNSET
    recording_channels: Union[Unset, TransportConfigurationTwilioRecordingChannels] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        timeout = self.timeout

        record = self.record

        recording_channels: Union[Unset, str] = UNSET
        if not isinstance(self.recording_channels, Unset):
            recording_channels = self.recording_channels.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if record is not UNSET:
            field_dict["record"] = record
        if recording_channels is not UNSET:
            field_dict["recordingChannels"] = recording_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = TransportConfigurationTwilioProvider(d.pop("provider"))

        timeout = d.pop("timeout", UNSET)

        record = d.pop("record", UNSET)

        _recording_channels = d.pop("recordingChannels", UNSET)
        recording_channels: Union[Unset, TransportConfigurationTwilioRecordingChannels]
        if isinstance(_recording_channels, Unset):
            recording_channels = UNSET
        else:
            recording_channels = TransportConfigurationTwilioRecordingChannels(_recording_channels)

        transport_configuration_twilio = cls(
            provider=provider,
            timeout=timeout,
            record=record,
            recording_channels=recording_channels,
        )

        transport_configuration_twilio.additional_properties = d
        return transport_configuration_twilio

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
