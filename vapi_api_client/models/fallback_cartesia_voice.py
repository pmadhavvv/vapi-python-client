from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fallback_cartesia_voice_language import FallbackCartesiaVoiceLanguage
from ..models.fallback_cartesia_voice_model import FallbackCartesiaVoiceModel
from ..models.fallback_cartesia_voice_provider import FallbackCartesiaVoiceProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cartesia_experimental_controls import CartesiaExperimentalControls
    from ..models.chunk_plan import ChunkPlan


T = TypeVar("T", bound="FallbackCartesiaVoice")


@_attrs_define
class FallbackCartesiaVoice:
    """
    Attributes:
        provider (FallbackCartesiaVoiceProvider): This is the voice provider that will be used.
        voice_id (str): The ID of the particular voice you want to use.
        model (Union[Unset, FallbackCartesiaVoiceModel]): This is the model that will be used. This is optional and will
            default to the correct model for the voiceId. Example: sonic-english.
        language (Union[Unset, FallbackCartesiaVoiceLanguage]): This is the language that will be used. This is optional
            and will default to the correct language for the voiceId. Example: en.
        experimental_controls (Union[Unset, CartesiaExperimentalControls]):
        chunk_plan (Union[Unset, ChunkPlan]):
    """

    provider: FallbackCartesiaVoiceProvider
    voice_id: str
    model: Union[Unset, FallbackCartesiaVoiceModel] = UNSET
    language: Union[Unset, FallbackCartesiaVoiceLanguage] = UNSET
    experimental_controls: Union[Unset, "CartesiaExperimentalControls"] = UNSET
    chunk_plan: Union[Unset, "ChunkPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        voice_id = self.voice_id

        model: Union[Unset, str] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.value

        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        experimental_controls: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.experimental_controls, Unset):
            experimental_controls = self.experimental_controls.to_dict()

        chunk_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.chunk_plan, Unset):
            chunk_plan = self.chunk_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "voiceId": voice_id,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if language is not UNSET:
            field_dict["language"] = language
        if experimental_controls is not UNSET:
            field_dict["experimentalControls"] = experimental_controls
        if chunk_plan is not UNSET:
            field_dict["chunkPlan"] = chunk_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cartesia_experimental_controls import CartesiaExperimentalControls
        from ..models.chunk_plan import ChunkPlan

        d = src_dict.copy()
        provider = FallbackCartesiaVoiceProvider(d.pop("provider"))

        voice_id = d.pop("voiceId")

        _model = d.pop("model", UNSET)
        model: Union[Unset, FallbackCartesiaVoiceModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = FallbackCartesiaVoiceModel(_model)

        _language = d.pop("language", UNSET)
        language: Union[Unset, FallbackCartesiaVoiceLanguage]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = FallbackCartesiaVoiceLanguage(_language)

        _experimental_controls = d.pop("experimentalControls", UNSET)
        experimental_controls: Union[Unset, CartesiaExperimentalControls]
        if isinstance(_experimental_controls, Unset):
            experimental_controls = UNSET
        else:
            experimental_controls = CartesiaExperimentalControls.from_dict(_experimental_controls)

        _chunk_plan = d.pop("chunkPlan", UNSET)
        chunk_plan: Union[Unset, ChunkPlan]
        if isinstance(_chunk_plan, Unset):
            chunk_plan = UNSET
        else:
            chunk_plan = ChunkPlan.from_dict(_chunk_plan)

        fallback_cartesia_voice = cls(
            provider=provider,
            voice_id=voice_id,
            model=model,
            language=language,
            experimental_controls=experimental_controls,
            chunk_plan=chunk_plan,
        )

        fallback_cartesia_voice.additional_properties = d
        return fallback_cartesia_voice

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
