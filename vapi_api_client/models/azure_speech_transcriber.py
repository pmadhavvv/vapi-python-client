from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.azure_speech_transcriber_language import AzureSpeechTranscriberLanguage
from ..models.azure_speech_transcriber_provider import AzureSpeechTranscriberProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="AzureSpeechTranscriber")


@_attrs_define
class AzureSpeechTranscriber:
    """
    Attributes:
        provider (AzureSpeechTranscriberProvider): This is the transcription provider that will be used.
        language (Union[Unset, AzureSpeechTranscriberLanguage]): This is the language that will be set for the
            transcription. The list of languages Azure supports can be found here: https://learn.microsoft.com/en-
            us/azure/ai-services/speech-service/language-support?tabs=stt
    """

    provider: AzureSpeechTranscriberProvider
    language: Union[Unset, AzureSpeechTranscriberLanguage] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = AzureSpeechTranscriberProvider(d.pop("provider"))

        _language = d.pop("language", UNSET)
        language: Union[Unset, AzureSpeechTranscriberLanguage]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = AzureSpeechTranscriberLanguage(_language)

        azure_speech_transcriber = cls(
            provider=provider,
            language=language,
        )

        azure_speech_transcriber.additional_properties = d
        return azure_speech_transcriber

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
