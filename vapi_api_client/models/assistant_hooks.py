from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assistant_hooks_on import AssistantHooksOn
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_hook_action_base import AssistantHookActionBase
    from ..models.assistant_hook_filter import AssistantHookFilter


T = TypeVar("T", bound="AssistantHooks")


@_attrs_define
class AssistantHooks:
    """
    Attributes:
        on (AssistantHooksOn): This is the event that triggers this hook
        do (list['AssistantHookActionBase']): This is the set of actions to perform when the hook triggers
        filters (Union[Unset, list['AssistantHookFilter']]): This is the set of filters that must match for the hook to
            trigger
    """

    on: AssistantHooksOn
    do: list["AssistantHookActionBase"]
    filters: Union[Unset, list["AssistantHookFilter"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        on = self.on.value

        do = []
        for do_item_data in self.do:
            do_item = do_item_data.to_dict()
            do.append(do_item)

        filters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "on": on,
                "do": do,
            }
        )
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.assistant_hook_action_base import AssistantHookActionBase
        from ..models.assistant_hook_filter import AssistantHookFilter

        d = src_dict.copy()
        on = AssistantHooksOn(d.pop("on"))

        do = []
        _do = d.pop("do")
        for do_item_data in _do:
            do_item = AssistantHookActionBase.from_dict(do_item_data)

            do.append(do_item)

        filters = []
        _filters = d.pop("filters", UNSET)
        for filters_item_data in _filters or []:
            filters_item = AssistantHookFilter.from_dict(filters_item_data)

            filters.append(filters_item)

        assistant_hooks = cls(
            on=on,
            do=do,
            filters=filters,
        )

        assistant_hooks.additional_properties = d
        return assistant_hooks

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
