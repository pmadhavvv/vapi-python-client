from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cartesia_experimental_controls_emotion import CartesiaExperimentalControlsEmotion
from ..models.cartesia_experimental_controls_speed import CartesiaExperimentalControlsSpeed
from ..types import UNSET, Unset

T = TypeVar("T", bound="CartesiaExperimentalControls")


@_attrs_define
class CartesiaExperimentalControls:
    """
    Attributes:
        speed (Union[Unset, CartesiaExperimentalControlsSpeed]):  Example: normal.
        emotion (Union[Unset, CartesiaExperimentalControlsEmotion]):  Example: ['happiness:high'].
    """

    speed: Union[Unset, CartesiaExperimentalControlsSpeed] = UNSET
    emotion: Union[Unset, CartesiaExperimentalControlsEmotion] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        speed: Union[Unset, str] = UNSET
        if not isinstance(self.speed, Unset):
            speed = self.speed.value

        emotion: Union[Unset, str] = UNSET
        if not isinstance(self.emotion, Unset):
            emotion = self.emotion.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if speed is not UNSET:
            field_dict["speed"] = speed
        if emotion is not UNSET:
            field_dict["emotion"] = emotion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _speed = d.pop("speed", UNSET)
        speed: Union[Unset, CartesiaExperimentalControlsSpeed]
        if isinstance(_speed, Unset):
            speed = UNSET
        else:
            speed = CartesiaExperimentalControlsSpeed(_speed)

        _emotion = d.pop("emotion", UNSET)
        emotion: Union[Unset, CartesiaExperimentalControlsEmotion]
        if isinstance(_emotion, Unset):
            emotion = UNSET
        else:
            emotion = CartesiaExperimentalControlsEmotion(_emotion)

        cartesia_experimental_controls = cls(
            speed=speed,
            emotion=emotion,
        )

        cartesia_experimental_controls.additional_properties = d
        return cartesia_experimental_controls

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
