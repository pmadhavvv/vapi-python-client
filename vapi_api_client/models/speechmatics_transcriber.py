from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.speechmatics_transcriber_language import SpeechmaticsTranscriberLanguage
from ..models.speechmatics_transcriber_model import SpeechmaticsTranscriberModel
from ..models.speechmatics_transcriber_provider import SpeechmaticsTranscriberProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpeechmaticsTranscriber")


@_attrs_define
class SpeechmaticsTranscriber:
    """
    Attributes:
        provider (SpeechmaticsTranscriberProvider): This is the transcription provider that will be used.
        model (Union[Unset, SpeechmaticsTranscriberModel]): This is the model that will be used for the transcription.
        language (Union[Unset, SpeechmaticsTranscriberLanguage]):
    """

    provider: SpeechmaticsTranscriberProvider
    model: Union[Unset, SpeechmaticsTranscriberModel] = UNSET
    language: Union[Unset, SpeechmaticsTranscriberLanguage] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        model: Union[Unset, str] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.value

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
        if model is not UNSET:
            field_dict["model"] = model
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = SpeechmaticsTranscriberProvider(d.pop("provider"))

        _model = d.pop("model", UNSET)
        model: Union[Unset, SpeechmaticsTranscriberModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = SpeechmaticsTranscriberModel(_model)

        _language = d.pop("language", UNSET)
        language: Union[Unset, SpeechmaticsTranscriberLanguage]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = SpeechmaticsTranscriberLanguage(_language)

        speechmatics_transcriber = cls(
            provider=provider,
            model=model,
            language=language,
        )

        speechmatics_transcriber.additional_properties = d
        return speechmatics_transcriber

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
