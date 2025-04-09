from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assembly_ai_transcriber_language import AssemblyAITranscriberLanguage
from ..models.assembly_ai_transcriber_provider import AssemblyAITranscriberProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssemblyAITranscriber")


@_attrs_define
class AssemblyAITranscriber:
    """
    Attributes:
        provider (AssemblyAITranscriberProvider): This is the transcription provider that will be used.
        language (Union[Unset, AssemblyAITranscriberLanguage]): This is the language that will be set for the
            transcription.
        realtime_url (Union[Unset, str]): The WebSocket URL that the transcriber connects to.
        word_boost (Union[Unset, list[str]]): Add up to 2500 characters of custom vocabulary.
        end_utterance_silence_threshold (Union[Unset, float]): The duration of the end utterance silence threshold in
            milliseconds.
        disable_partial_transcripts (Union[Unset, bool]): Disable partial transcripts.
            Set to `true` to not receive partial transcripts. Defaults to `false`.
    """

    provider: AssemblyAITranscriberProvider
    language: Union[Unset, AssemblyAITranscriberLanguage] = UNSET
    realtime_url: Union[Unset, str] = UNSET
    word_boost: Union[Unset, list[str]] = UNSET
    end_utterance_silence_threshold: Union[Unset, float] = UNSET
    disable_partial_transcripts: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        realtime_url = self.realtime_url

        word_boost: Union[Unset, list[str]] = UNSET
        if not isinstance(self.word_boost, Unset):
            word_boost = self.word_boost

        end_utterance_silence_threshold = self.end_utterance_silence_threshold

        disable_partial_transcripts = self.disable_partial_transcripts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if realtime_url is not UNSET:
            field_dict["realtimeUrl"] = realtime_url
        if word_boost is not UNSET:
            field_dict["wordBoost"] = word_boost
        if end_utterance_silence_threshold is not UNSET:
            field_dict["endUtteranceSilenceThreshold"] = end_utterance_silence_threshold
        if disable_partial_transcripts is not UNSET:
            field_dict["disablePartialTranscripts"] = disable_partial_transcripts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = AssemblyAITranscriberProvider(d.pop("provider"))

        _language = d.pop("language", UNSET)
        language: Union[Unset, AssemblyAITranscriberLanguage]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = AssemblyAITranscriberLanguage(_language)

        realtime_url = d.pop("realtimeUrl", UNSET)

        word_boost = cast(list[str], d.pop("wordBoost", UNSET))

        end_utterance_silence_threshold = d.pop("endUtteranceSilenceThreshold", UNSET)

        disable_partial_transcripts = d.pop("disablePartialTranscripts", UNSET)

        assembly_ai_transcriber = cls(
            provider=provider,
            language=language,
            realtime_url=realtime_url,
            word_boost=word_boost,
            end_utterance_silence_threshold=end_utterance_silence_threshold,
            disable_partial_transcripts=disable_partial_transcripts,
        )

        assembly_ai_transcriber.additional_properties = d
        return assembly_ai_transcriber

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
