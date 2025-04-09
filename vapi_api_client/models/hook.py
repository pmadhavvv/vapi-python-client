from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hook_on import HookOn

if TYPE_CHECKING:
    from ..models.say_hook import SayHook


T = TypeVar("T", bound="Hook")


@_attrs_define
class Hook:
    """
    Attributes:
        on (HookOn):
        do (list['SayHook']):
    """

    on: HookOn
    do: list["SayHook"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        on = self.on.value

        do = []
        for do_item_data in self.do:
            do_item = do_item_data.to_dict()
            do.append(do_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "on": on,
                "do": do,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.say_hook import SayHook

        d = dict(src_dict)
        on = HookOn(d.pop("on"))

        do = []
        _do = d.pop("do")
        for do_item_data in _do:
            do_item = SayHook.from_dict(do_item_data)

            do.append(do_item)

        hook = cls(
            on=on,
            do=do,
        )

        hook.additional_properties = d
        return hook

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
