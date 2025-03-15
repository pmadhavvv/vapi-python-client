from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.eleven_labs_transcriber_language import ElevenLabsTranscriberLanguage
from ..models.eleven_labs_transcriber_model import ElevenLabsTranscriberModel
from ..models.eleven_labs_transcriber_provider import ElevenLabsTranscriberProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="ElevenLabsTranscriber")


@_attrs_define
class ElevenLabsTranscriber:
    """
    Attributes:
        provider (ElevenLabsTranscriberProvider): This is the transcription provider that will be used.
        model (Union[Unset, ElevenLabsTranscriberModel]): This is the model that will be used for the transcription.
        language (Union[Unset, ElevenLabsTranscriberLanguage]):
    """

    provider: ElevenLabsTranscriberProvider
    model: Union[Unset, ElevenLabsTranscriberModel] = UNSET
    language: Union[Unset, ElevenLabsTranscriberLanguage] = UNSET
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = ElevenLabsTranscriberProvider(d.pop("provider"))

        _model = d.pop("model", UNSET)
        model: Union[Unset, ElevenLabsTranscriberModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = ElevenLabsTranscriberModel(_model)

        _language = d.pop("language", UNSET)
        language: Union[Unset, ElevenLabsTranscriberLanguage]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = ElevenLabsTranscriberLanguage(_language)

        eleven_labs_transcriber = cls(
            provider=provider,
            model=model,
            language=language,
        )

        eleven_labs_transcriber.additional_properties = d
        return eleven_labs_transcriber

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
