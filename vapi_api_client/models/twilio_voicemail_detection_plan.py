from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.twilio_voicemail_detection_plan_provider import TwilioVoicemailDetectionPlanProvider
from ..models.twilio_voicemail_detection_plan_voicemail_detection_types import (
    TwilioVoicemailDetectionPlanVoicemailDetectionTypes,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TwilioVoicemailDetectionPlan")


@_attrs_define
class TwilioVoicemailDetectionPlan:
    """
    Attributes:
        provider (TwilioVoicemailDetectionPlanProvider): This is the provider to use for voicemail detection.
        voicemail_detection_types (Union[Unset, TwilioVoicemailDetectionPlanVoicemailDetectionTypes]): These are the AMD
            messages from Twilio that are considered as voicemail. Default is ['machine_end_beep', 'machine_end_silence'].

            @default {Array} ['machine_end_beep', 'machine_end_silence'] Example: ['machine_end_beep',
            'machine_end_silence'].
        enabled (Union[Unset, bool]): This sets whether the assistant should detect voicemail. Defaults to true.

            @default true
        machine_detection_timeout (Union[Unset, float]): The number of seconds that Twilio should attempt to perform
            answering machine detection before timing out and returning AnsweredBy as unknown. Default is 30 seconds.

            Increasing this value will provide the engine more time to make a determination. This can be useful when
            DetectMessageEnd is provided in the MachineDetection parameter and there is an expectation of long answering
            machine greetings that can exceed 30 seconds.

            Decreasing this value will reduce the amount of time the engine has to make a determination. This can be
            particularly useful when the Enable option is provided in the MachineDetection parameter and you want to limit
            the time for initial detection.

            Check the [Twilio docs](https://www.twilio.com/docs/voice/answering-machine-detection#optional-api-tuning-
            parameters) for more info.

            @default 30
        machine_detection_speech_threshold (Union[Unset, float]): The number of milliseconds that is used as the
            measuring stick for the length of the speech activity. Durations lower than this value will be interpreted as a
            human, longer as a machine. Default is 2400 milliseconds.

            Increasing this value will reduce the chance of a False Machine (detected machine, actually human) for a long
            human greeting (e.g., a business greeting) but increase the time it takes to detect a machine.

            Decreasing this value will reduce the chances of a False Human (detected human, actually machine) for short
            voicemail greetings. The value of this parameter may need to be reduced by more than 1000ms to detect very short
            voicemail greetings. A reduction of that significance can result in increased False Machine detections.
            Adjusting the MachineDetectionSpeechEndThreshold is likely the better approach for short voicemails. Decreasing
            MachineDetectionSpeechThreshold will also reduce the time it takes to detect a machine.

            Check the [Twilio docs](https://www.twilio.com/docs/voice/answering-machine-detection#optional-api-tuning-
            parameters) for more info.

            @default 2400
        machine_detection_speech_end_threshold (Union[Unset, float]): The number of milliseconds of silence after speech
            activity at which point the speech activity is considered complete. Default is 1200 milliseconds.

            Increasing this value will typically be used to better address the short voicemail greeting scenarios. For short
            voicemails, there is typically 1000-2000ms of audio followed by 1200-2400ms of silence and then additional audio
            before the beep. Increasing the MachineDetectionSpeechEndThreshold to ~2500ms will treat the 1200-2400ms of
            silence as a gap in the greeting but not the end of the greeting and will result in a machine detection. The
            downsides of such a change include:
            - Increasing the delay for human detection by the amount you increase this parameter, e.g., a change of 1200ms
            to 2500ms increases human detection delay by 1300ms.
            - Cases where a human has two utterances separated by a period of silence (e.g. a "Hello", then 2000ms of
            silence, and another "Hello") may be interpreted as a machine.

            Decreasing this value will result in faster human detection. The consequence is that it can lead to increased
            False Human (detected human, actually machine) detections because a silence gap in a voicemail greeting (not
            necessarily just in short voicemail scenarios) can be incorrectly interpreted as the end of speech.

            Check the [Twilio docs](https://www.twilio.com/docs/voice/answering-machine-detection#optional-api-tuning-
            parameters) for more info.

            @default 1200
        machine_detection_silence_timeout (Union[Unset, float]): The number of milliseconds of initial silence after
            which an unknown AnsweredBy result will be returned. Default is 5000 milliseconds.

            Increasing this value will result in waiting for a longer period of initial silence before returning an
            'unknown' AMD result.

            Decreasing this value will result in waiting for a shorter period of initial silence before returning an
            'unknown' AMD result.

            Check the [Twilio docs](https://www.twilio.com/docs/voice/answering-machine-detection#optional-api-tuning-
            parameters) for more info.

            @default 5000
    """

    provider: TwilioVoicemailDetectionPlanProvider
    voicemail_detection_types: Union[Unset, TwilioVoicemailDetectionPlanVoicemailDetectionTypes] = UNSET
    enabled: Union[Unset, bool] = UNSET
    machine_detection_timeout: Union[Unset, float] = UNSET
    machine_detection_speech_threshold: Union[Unset, float] = UNSET
    machine_detection_speech_end_threshold: Union[Unset, float] = UNSET
    machine_detection_silence_timeout: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        voicemail_detection_types: Union[Unset, str] = UNSET
        if not isinstance(self.voicemail_detection_types, Unset):
            voicemail_detection_types = self.voicemail_detection_types.value

        enabled = self.enabled

        machine_detection_timeout = self.machine_detection_timeout

        machine_detection_speech_threshold = self.machine_detection_speech_threshold

        machine_detection_speech_end_threshold = self.machine_detection_speech_end_threshold

        machine_detection_silence_timeout = self.machine_detection_silence_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if voicemail_detection_types is not UNSET:
            field_dict["voicemailDetectionTypes"] = voicemail_detection_types
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if machine_detection_timeout is not UNSET:
            field_dict["machineDetectionTimeout"] = machine_detection_timeout
        if machine_detection_speech_threshold is not UNSET:
            field_dict["machineDetectionSpeechThreshold"] = machine_detection_speech_threshold
        if machine_detection_speech_end_threshold is not UNSET:
            field_dict["machineDetectionSpeechEndThreshold"] = machine_detection_speech_end_threshold
        if machine_detection_silence_timeout is not UNSET:
            field_dict["machineDetectionSilenceTimeout"] = machine_detection_silence_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = TwilioVoicemailDetectionPlanProvider(d.pop("provider"))

        _voicemail_detection_types = d.pop("voicemailDetectionTypes", UNSET)
        voicemail_detection_types: Union[Unset, TwilioVoicemailDetectionPlanVoicemailDetectionTypes]
        if isinstance(_voicemail_detection_types, Unset):
            voicemail_detection_types = UNSET
        else:
            voicemail_detection_types = TwilioVoicemailDetectionPlanVoicemailDetectionTypes(_voicemail_detection_types)

        enabled = d.pop("enabled", UNSET)

        machine_detection_timeout = d.pop("machineDetectionTimeout", UNSET)

        machine_detection_speech_threshold = d.pop("machineDetectionSpeechThreshold", UNSET)

        machine_detection_speech_end_threshold = d.pop("machineDetectionSpeechEndThreshold", UNSET)

        machine_detection_silence_timeout = d.pop("machineDetectionSilenceTimeout", UNSET)

        twilio_voicemail_detection_plan = cls(
            provider=provider,
            voicemail_detection_types=voicemail_detection_types,
            enabled=enabled,
            machine_detection_timeout=machine_detection_timeout,
            machine_detection_speech_threshold=machine_detection_speech_threshold,
            machine_detection_speech_end_threshold=machine_detection_speech_end_threshold,
            machine_detection_silence_timeout=machine_detection_silence_timeout,
        )

        twilio_voicemail_detection_plan.additional_properties = d
        return twilio_voicemail_detection_plan

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
