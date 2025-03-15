from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transcript_plan import TranscriptPlan


T = TypeVar("T", bound="ArtifactPlan")


@_attrs_define
class ArtifactPlan:
    """
    Attributes:
        recording_enabled (Union[Unset, bool]): This determines whether assistant's calls are recorded. Defaults to
            true.

            Usage:
            - If you don't want to record the calls, set this to false.
            - If you want to record the calls when `assistant.hipaaEnabled` (deprecated) or
            `assistant.compliancePlan.hipaaEnabled` explicity set this to true and make sure to provide S3 or GCP
            credentials on the Provider Credentials page in the Dashboard.

            You can find the recording at `call.artifact.recordingUrl` and `call.artifact.stereoRecordingUrl` after the call
            is ended.

            @default true Example: True.
        video_recording_enabled (Union[Unset, bool]): This determines whether the video is recorded during the call.
            Defaults to false. Only relevant for `webCall` type.

            You can find the video recording at `call.artifact.videoRecordingUrl` after the call is ended.

            @default false
        pcap_enabled (Union[Unset, bool]): This determines whether the SIP packet capture is enabled. Defaults to true.
            Only relevant for `phone` type calls where phone number's provider is `vapi` or `byo-phone-number`.

            You can find the packet capture at `call.artifact.pcapUrl` after the call is ended.

            @default true Example: True.
        pcap_s3_path_prefix (Union[Unset, str]): This is the path where the SIP packet capture will be uploaded. This is
            only used if you have provided S3 or GCP credentials on the Provider Credentials page in the Dashboard.

            If credential.s3PathPrefix or credential.bucketPlan.path is set, this will append to it.

            Usage:
            - If you want to upload the packet capture to a specific path, set this to the path. Example: `/my-assistant-
            captures`.
            - If you want to upload the packet capture to the root of the bucket, set this to `/`.

            @default '/' Example: /pcaps.
        transcript_plan (Union[Unset, TranscriptPlan]):
        recording_path (Union[Unset, str]): This is the path where the recording will be uploaded. This is only used if
            you have provided S3 or GCP credentials on the Provider Credentials page in the Dashboard.

            If credential.s3PathPrefix or credential.bucketPlan.path is set, this will append to it.

            Usage:
            - If you want to upload the recording to a specific path, set this to the path. Example: `/my-assistant-
            recordings`.
            - If you want to upload the recording to the root of the bucket, set this to `/`.

            @default '/'
    """

    recording_enabled: Union[Unset, bool] = UNSET
    video_recording_enabled: Union[Unset, bool] = UNSET
    pcap_enabled: Union[Unset, bool] = UNSET
    pcap_s3_path_prefix: Union[Unset, str] = UNSET
    transcript_plan: Union[Unset, "TranscriptPlan"] = UNSET
    recording_path: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recording_enabled = self.recording_enabled

        video_recording_enabled = self.video_recording_enabled

        pcap_enabled = self.pcap_enabled

        pcap_s3_path_prefix = self.pcap_s3_path_prefix

        transcript_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.transcript_plan, Unset):
            transcript_plan = self.transcript_plan.to_dict()

        recording_path = self.recording_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recording_enabled is not UNSET:
            field_dict["recordingEnabled"] = recording_enabled
        if video_recording_enabled is not UNSET:
            field_dict["videoRecordingEnabled"] = video_recording_enabled
        if pcap_enabled is not UNSET:
            field_dict["pcapEnabled"] = pcap_enabled
        if pcap_s3_path_prefix is not UNSET:
            field_dict["pcapS3PathPrefix"] = pcap_s3_path_prefix
        if transcript_plan is not UNSET:
            field_dict["transcriptPlan"] = transcript_plan
        if recording_path is not UNSET:
            field_dict["recordingPath"] = recording_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.transcript_plan import TranscriptPlan

        d = src_dict.copy()
        recording_enabled = d.pop("recordingEnabled", UNSET)

        video_recording_enabled = d.pop("videoRecordingEnabled", UNSET)

        pcap_enabled = d.pop("pcapEnabled", UNSET)

        pcap_s3_path_prefix = d.pop("pcapS3PathPrefix", UNSET)

        _transcript_plan = d.pop("transcriptPlan", UNSET)
        transcript_plan: Union[Unset, TranscriptPlan]
        if isinstance(_transcript_plan, Unset):
            transcript_plan = UNSET
        else:
            transcript_plan = TranscriptPlan.from_dict(_transcript_plan)

        recording_path = d.pop("recordingPath", UNSET)

        artifact_plan = cls(
            recording_enabled=recording_enabled,
            video_recording_enabled=video_recording_enabled,
            pcap_enabled=pcap_enabled,
            pcap_s3_path_prefix=pcap_s3_path_prefix,
            transcript_plan=transcript_plan,
            recording_path=recording_path,
        )

        artifact_plan.additional_properties = d
        return artifact_plan

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
