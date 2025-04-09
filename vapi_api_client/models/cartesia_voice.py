from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cartesia_voice_language import CartesiaVoiceLanguage
from ..models.cartesia_voice_model import CartesiaVoiceModel
from ..models.cartesia_voice_provider import CartesiaVoiceProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cartesia_experimental_controls import CartesiaExperimentalControls
    from ..models.chunk_plan import ChunkPlan
    from ..models.fallback_plan import FallbackPlan


T = TypeVar("T", bound="CartesiaVoice")


@_attrs_define
class CartesiaVoice:
    """
    Attributes:
        provider (CartesiaVoiceProvider): This is the voice provider that will be used.
        voice_id (str): The ID of the particular voice you want to use.
        model (Union[Unset, CartesiaVoiceModel]): This is the model that will be used. This is optional and will default
            to the correct model for the voiceId. Example: sonic-english.
        language (Union[Unset, CartesiaVoiceLanguage]): This is the language that will be used. This is optional and
            will default to the correct language for the voiceId. Example: en.
        experimental_controls (Union[Unset, CartesiaExperimentalControls]):
        chunk_plan (Union[Unset, ChunkPlan]):
        fallback_plan (Union[Unset, FallbackPlan]):
    """

    provider: CartesiaVoiceProvider
    voice_id: str
    model: Union[Unset, CartesiaVoiceModel] = UNSET
    language: Union[Unset, CartesiaVoiceLanguage] = UNSET
    experimental_controls: Union[Unset, "CartesiaExperimentalControls"] = UNSET
    chunk_plan: Union[Unset, "ChunkPlan"] = UNSET
    fallback_plan: Union[Unset, "FallbackPlan"] = UNSET
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

        fallback_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fallback_plan, Unset):
            fallback_plan = self.fallback_plan.to_dict()

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
        if fallback_plan is not UNSET:
            field_dict["fallbackPlan"] = fallback_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cartesia_experimental_controls import CartesiaExperimentalControls
        from ..models.chunk_plan import ChunkPlan
        from ..models.fallback_plan import FallbackPlan

        d = dict(src_dict)
        provider = CartesiaVoiceProvider(d.pop("provider"))

        voice_id = d.pop("voiceId")

        _model = d.pop("model", UNSET)
        model: Union[Unset, CartesiaVoiceModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = CartesiaVoiceModel(_model)

        _language = d.pop("language", UNSET)
        language: Union[Unset, CartesiaVoiceLanguage]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = CartesiaVoiceLanguage(_language)

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

        _fallback_plan = d.pop("fallbackPlan", UNSET)
        fallback_plan: Union[Unset, FallbackPlan]
        if isinstance(_fallback_plan, Unset):
            fallback_plan = UNSET
        else:
            fallback_plan = FallbackPlan.from_dict(_fallback_plan)

        cartesia_voice = cls(
            provider=provider,
            voice_id=voice_id,
            model=model,
            language=language,
            experimental_controls=experimental_controls,
            chunk_plan=chunk_plan,
            fallback_plan=fallback_plan,
        )

        cartesia_voice.additional_properties = d
        return cartesia_voice

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
