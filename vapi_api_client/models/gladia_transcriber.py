from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gladia_transcriber_language import GladiaTranscriberLanguage
from ..models.gladia_transcriber_language_behaviour_type_0 import GladiaTranscriberLanguageBehaviourType0
from ..models.gladia_transcriber_model_type_0 import GladiaTranscriberModelType0
from ..models.gladia_transcriber_provider import GladiaTranscriberProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="GladiaTranscriber")


@_attrs_define
class GladiaTranscriber:
    """
    Attributes:
        provider (GladiaTranscriberProvider): This is the transcription provider that will be used.
        model (Union[GladiaTranscriberModelType0, Unset]): This is the Gladia model that will be used. Default is 'fast'
        language_behaviour (Union[GladiaTranscriberLanguageBehaviourType0, Unset]): Defines how the transcription model
            detects the audio language. Default value is 'automatic single language'.
        language (Union[Unset, GladiaTranscriberLanguage]): Defines the language to use for the transcription. Required
            when languageBehaviour is 'manual'.
        transcription_hint (Union[Unset, str]): Provides a custom vocabulary to the model to improve accuracy of
            transcribing context specific words, technical terms, names, etc. If empty, this argument is ignored.
            ⚠️ Warning ⚠️: Please be aware that the transcription_hint field has a character limit of 600. If you provide a
            transcription_hint longer than 600 characters, it will be automatically truncated to meet this limit. Example:
            custom vocabulary.
        prosody (Union[Unset, bool]): If prosody is true, you will get a transcription that can contain prosodies i.e.
            (laugh) (giggles) (malefic laugh) (toss) (music)… Default value is false.
        audio_enhancer (Union[Unset, bool]): If true, audio will be pre-processed to improve accuracy but latency will
            increase. Default value is false.
    """

    provider: GladiaTranscriberProvider
    model: Union[GladiaTranscriberModelType0, Unset] = UNSET
    language_behaviour: Union[GladiaTranscriberLanguageBehaviourType0, Unset] = UNSET
    language: Union[Unset, GladiaTranscriberLanguage] = UNSET
    transcription_hint: Union[Unset, str] = UNSET
    prosody: Union[Unset, bool] = UNSET
    audio_enhancer: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        model: Union[Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model.value

        language_behaviour: Union[Unset, str]
        if isinstance(self.language_behaviour, Unset):
            language_behaviour = UNSET
        else:
            language_behaviour = self.language_behaviour.value

        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        transcription_hint = self.transcription_hint

        prosody = self.prosody

        audio_enhancer = self.audio_enhancer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if language_behaviour is not UNSET:
            field_dict["languageBehaviour"] = language_behaviour
        if language is not UNSET:
            field_dict["language"] = language
        if transcription_hint is not UNSET:
            field_dict["transcriptionHint"] = transcription_hint
        if prosody is not UNSET:
            field_dict["prosody"] = prosody
        if audio_enhancer is not UNSET:
            field_dict["audioEnhancer"] = audio_enhancer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = GladiaTranscriberProvider(d.pop("provider"))

        def _parse_model(data: object) -> Union[GladiaTranscriberModelType0, Unset]:
            if isinstance(data, Unset):
                return data
            if not isinstance(data, str):
                raise TypeError()
            model_type_0 = GladiaTranscriberModelType0(data)

            return model_type_0

        model = _parse_model(d.pop("model", UNSET))

        def _parse_language_behaviour(data: object) -> Union[GladiaTranscriberLanguageBehaviourType0, Unset]:
            if isinstance(data, Unset):
                return data
            if not isinstance(data, str):
                raise TypeError()
            language_behaviour_type_0 = GladiaTranscriberLanguageBehaviourType0(data)

            return language_behaviour_type_0

        language_behaviour = _parse_language_behaviour(d.pop("languageBehaviour", UNSET))

        _language = d.pop("language", UNSET)
        language: Union[Unset, GladiaTranscriberLanguage]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = GladiaTranscriberLanguage(_language)

        transcription_hint = d.pop("transcriptionHint", UNSET)

        prosody = d.pop("prosody", UNSET)

        audio_enhancer = d.pop("audioEnhancer", UNSET)

        gladia_transcriber = cls(
            provider=provider,
            model=model,
            language_behaviour=language_behaviour,
            language=language,
            transcription_hint=transcription_hint,
            prosody=prosody,
            audio_enhancer=audio_enhancer,
        )

        gladia_transcriber.additional_properties = d
        return gladia_transcriber

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
