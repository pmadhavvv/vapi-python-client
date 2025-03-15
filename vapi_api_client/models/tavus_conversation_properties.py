from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TavusConversationProperties")


@_attrs_define
class TavusConversationProperties:
    """
    Attributes:
        max_call_duration (Union[Unset, float]): The maximum duration of the call in seconds. The default
            `maxCallDuration` is 3600 seconds (1 hour).
            Once the time limit specified by this parameter has been reached, the conversation will automatically shut down.
        participant_left_timeout (Union[Unset, float]): The duration in seconds after which the call will be
            automatically shut down once the last participant leaves.
        participant_absent_timeout (Union[Unset, float]): Starting from conversation creation, the duration in seconds
            after which the call will be automatically shut down if no participant joins the call.
            Default is 300 seconds (5 minutes).
        enable_recording (Union[Unset, bool]): If true, the user will be able to record the conversation.
        enable_transcription (Union[Unset, bool]): If true, the user will be able to transcribe the conversation.
            You can find more instructions on displaying transcriptions if you are using your custom DailyJS components
            here.
            You need to have an event listener on Daily that listens for `app-messages`.
        apply_greenscreen (Union[Unset, bool]): If true, the background will be replaced with a greenscreen (RGB values:
            `[0, 255, 155]`).
            You can use WebGL on the frontend to make the greenscreen transparent or change its color.
        language (Union[Unset, str]): The language of the conversation. Please provide the **full language name**, not
            the two-letter code.
            If you are using your own TTS voice, please ensure it supports the language you provide.
            If you are using a stock replica or default persona, please note that only ElevenLabs and Cartesia supported
            languages are available.
            You can find a full list of supported languages for Cartesia here, for ElevenLabs here, and for PlayHT here.
        recording_s3_bucket_name (Union[Unset, str]): The name of the S3 bucket where the recording will be stored.
        recording_s3_bucket_region (Union[Unset, str]): The region of the S3 bucket where the recording will be stored.
        aws_assume_role_arn (Union[Unset, str]): The ARN of the role that will be assumed to access the S3 bucket.
    """

    max_call_duration: Union[Unset, float] = UNSET
    participant_left_timeout: Union[Unset, float] = UNSET
    participant_absent_timeout: Union[Unset, float] = UNSET
    enable_recording: Union[Unset, bool] = UNSET
    enable_transcription: Union[Unset, bool] = UNSET
    apply_greenscreen: Union[Unset, bool] = UNSET
    language: Union[Unset, str] = UNSET
    recording_s3_bucket_name: Union[Unset, str] = UNSET
    recording_s3_bucket_region: Union[Unset, str] = UNSET
    aws_assume_role_arn: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_call_duration = self.max_call_duration

        participant_left_timeout = self.participant_left_timeout

        participant_absent_timeout = self.participant_absent_timeout

        enable_recording = self.enable_recording

        enable_transcription = self.enable_transcription

        apply_greenscreen = self.apply_greenscreen

        language = self.language

        recording_s3_bucket_name = self.recording_s3_bucket_name

        recording_s3_bucket_region = self.recording_s3_bucket_region

        aws_assume_role_arn = self.aws_assume_role_arn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_call_duration is not UNSET:
            field_dict["maxCallDuration"] = max_call_duration
        if participant_left_timeout is not UNSET:
            field_dict["participantLeftTimeout"] = participant_left_timeout
        if participant_absent_timeout is not UNSET:
            field_dict["participantAbsentTimeout"] = participant_absent_timeout
        if enable_recording is not UNSET:
            field_dict["enableRecording"] = enable_recording
        if enable_transcription is not UNSET:
            field_dict["enableTranscription"] = enable_transcription
        if apply_greenscreen is not UNSET:
            field_dict["applyGreenscreen"] = apply_greenscreen
        if language is not UNSET:
            field_dict["language"] = language
        if recording_s3_bucket_name is not UNSET:
            field_dict["recordingS3BucketName"] = recording_s3_bucket_name
        if recording_s3_bucket_region is not UNSET:
            field_dict["recordingS3BucketRegion"] = recording_s3_bucket_region
        if aws_assume_role_arn is not UNSET:
            field_dict["awsAssumeRoleArn"] = aws_assume_role_arn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        max_call_duration = d.pop("maxCallDuration", UNSET)

        participant_left_timeout = d.pop("participantLeftTimeout", UNSET)

        participant_absent_timeout = d.pop("participantAbsentTimeout", UNSET)

        enable_recording = d.pop("enableRecording", UNSET)

        enable_transcription = d.pop("enableTranscription", UNSET)

        apply_greenscreen = d.pop("applyGreenscreen", UNSET)

        language = d.pop("language", UNSET)

        recording_s3_bucket_name = d.pop("recordingS3BucketName", UNSET)

        recording_s3_bucket_region = d.pop("recordingS3BucketRegion", UNSET)

        aws_assume_role_arn = d.pop("awsAssumeRoleArn", UNSET)

        tavus_conversation_properties = cls(
            max_call_duration=max_call_duration,
            participant_left_timeout=participant_left_timeout,
            participant_absent_timeout=participant_absent_timeout,
            enable_recording=enable_recording,
            enable_transcription=enable_transcription,
            apply_greenscreen=apply_greenscreen,
            language=language,
            recording_s3_bucket_name=recording_s3_bucket_name,
            recording_s3_bucket_region=recording_s3_bucket_region,
            aws_assume_role_arn=aws_assume_role_arn,
        )

        tavus_conversation_properties.additional_properties = d
        return tavus_conversation_properties

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
