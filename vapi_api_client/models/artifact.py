from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bot_message import BotMessage
    from ..models.open_ai_message import OpenAIMessage
    from ..models.system_message import SystemMessage
    from ..models.tool_call_message import ToolCallMessage
    from ..models.tool_call_result_message import ToolCallResultMessage
    from ..models.user_message import UserMessage


T = TypeVar("T", bound="Artifact")


@_attrs_define
class Artifact:
    """
    Attributes:
        messages (Union[Unset, list[Union['BotMessage', 'SystemMessage', 'ToolCallMessage', 'ToolCallResultMessage',
            'UserMessage']]]): These are the messages that were spoken during the call.
        messages_open_ai_formatted (Union[Unset, list['OpenAIMessage']]): These are the messages that were spoken during
            the call, formatted for OpenAI.
        recording_url (Union[Unset, str]): This is the recording url for the call. To enable, set
            `assistant.artifactPlan.recordingEnabled`.
        stereo_recording_url (Union[Unset, str]): This is the stereo recording url for the call. To enable, set
            `assistant.artifactPlan.recordingEnabled`.
        video_recording_url (Union[Unset, str]): This is video recording url for the call. To enable, set
            `assistant.artifactPlan.videoRecordingEnabled`.
        video_recording_start_delay_seconds (Union[Unset, float]): This is video recording start delay in ms. To enable,
            set `assistant.artifactPlan.videoRecordingEnabled`. This can be used to align the playback of the recording with
            artifact.messages timestamps.
        transcript (Union[Unset, str]): This is the transcript of the call. This is derived from `artifact.messages` but
            provided for convenience.
        pcap_url (Union[Unset, str]): This is the packet capture url for the call. This is only available for `phone`
            type calls where phone number's provider is `vapi` or `byo-phone-number`.
    """

    messages: Union[
        Unset, list[Union["BotMessage", "SystemMessage", "ToolCallMessage", "ToolCallResultMessage", "UserMessage"]]
    ] = UNSET
    messages_open_ai_formatted: Union[Unset, list["OpenAIMessage"]] = UNSET
    recording_url: Union[Unset, str] = UNSET
    stereo_recording_url: Union[Unset, str] = UNSET
    video_recording_url: Union[Unset, str] = UNSET
    video_recording_start_delay_seconds: Union[Unset, float] = UNSET
    transcript: Union[Unset, str] = UNSET
    pcap_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bot_message import BotMessage
        from ..models.system_message import SystemMessage
        from ..models.tool_call_message import ToolCallMessage
        from ..models.user_message import UserMessage

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item: dict[str, Any]
                if isinstance(messages_item_data, UserMessage):
                    messages_item = messages_item_data.to_dict()
                elif isinstance(messages_item_data, SystemMessage):
                    messages_item = messages_item_data.to_dict()
                elif isinstance(messages_item_data, BotMessage):
                    messages_item = messages_item_data.to_dict()
                elif isinstance(messages_item_data, ToolCallMessage):
                    messages_item = messages_item_data.to_dict()
                else:
                    messages_item = messages_item_data.to_dict()

                messages.append(messages_item)

        messages_open_ai_formatted: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages_open_ai_formatted, Unset):
            messages_open_ai_formatted = []
            for messages_open_ai_formatted_item_data in self.messages_open_ai_formatted:
                messages_open_ai_formatted_item = messages_open_ai_formatted_item_data.to_dict()
                messages_open_ai_formatted.append(messages_open_ai_formatted_item)

        recording_url = self.recording_url

        stereo_recording_url = self.stereo_recording_url

        video_recording_url = self.video_recording_url

        video_recording_start_delay_seconds = self.video_recording_start_delay_seconds

        transcript = self.transcript

        pcap_url = self.pcap_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if messages is not UNSET:
            field_dict["messages"] = messages
        if messages_open_ai_formatted is not UNSET:
            field_dict["messagesOpenAIFormatted"] = messages_open_ai_formatted
        if recording_url is not UNSET:
            field_dict["recordingUrl"] = recording_url
        if stereo_recording_url is not UNSET:
            field_dict["stereoRecordingUrl"] = stereo_recording_url
        if video_recording_url is not UNSET:
            field_dict["videoRecordingUrl"] = video_recording_url
        if video_recording_start_delay_seconds is not UNSET:
            field_dict["videoRecordingStartDelaySeconds"] = video_recording_start_delay_seconds
        if transcript is not UNSET:
            field_dict["transcript"] = transcript
        if pcap_url is not UNSET:
            field_dict["pcapUrl"] = pcap_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.bot_message import BotMessage
        from ..models.open_ai_message import OpenAIMessage
        from ..models.system_message import SystemMessage
        from ..models.tool_call_message import ToolCallMessage
        from ..models.tool_call_result_message import ToolCallResultMessage
        from ..models.user_message import UserMessage

        d = src_dict.copy()
        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:

            def _parse_messages_item(
                data: object,
            ) -> Union["BotMessage", "SystemMessage", "ToolCallMessage", "ToolCallResultMessage", "UserMessage"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_0 = UserMessage.from_dict(data)

                    return messages_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_1 = SystemMessage.from_dict(data)

                    return messages_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_2 = BotMessage.from_dict(data)

                    return messages_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_3 = ToolCallMessage.from_dict(data)

                    return messages_item_type_3
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                messages_item_type_4 = ToolCallResultMessage.from_dict(data)

                return messages_item_type_4

            messages_item = _parse_messages_item(messages_item_data)

            messages.append(messages_item)

        messages_open_ai_formatted = []
        _messages_open_ai_formatted = d.pop("messagesOpenAIFormatted", UNSET)
        for messages_open_ai_formatted_item_data in _messages_open_ai_formatted or []:
            messages_open_ai_formatted_item = OpenAIMessage.from_dict(messages_open_ai_formatted_item_data)

            messages_open_ai_formatted.append(messages_open_ai_formatted_item)

        recording_url = d.pop("recordingUrl", UNSET)

        stereo_recording_url = d.pop("stereoRecordingUrl", UNSET)

        video_recording_url = d.pop("videoRecordingUrl", UNSET)

        video_recording_start_delay_seconds = d.pop("videoRecordingStartDelaySeconds", UNSET)

        transcript = d.pop("transcript", UNSET)

        pcap_url = d.pop("pcapUrl", UNSET)

        artifact = cls(
            messages=messages,
            messages_open_ai_formatted=messages_open_ai_formatted,
            recording_url=recording_url,
            stereo_recording_url=stereo_recording_url,
            video_recording_url=video_recording_url,
            video_recording_start_delay_seconds=video_recording_start_delay_seconds,
            transcript=transcript,
            pcap_url=pcap_url,
        )

        artifact.additional_properties = d
        return artifact

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
