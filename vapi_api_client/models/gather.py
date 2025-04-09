from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gather_type import GatherType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gather_metadata import GatherMetadata
    from ..models.hook import Hook
    from ..models.json_schema import JsonSchema


T = TypeVar("T", bound="Gather")


@_attrs_define
class Gather:
    """
    Attributes:
        type_ (GatherType):
        output (JsonSchema):
        name (str):
        confirm_content (Union[Unset, bool]): This is whether or not the workflow should read back the gathered data to
            the user, and ask about its correctness.
        hooks (Union[Unset, list['Hook']]): This is a list of hooks for a task.
            Each hook is a list of tasks to run on a trigger (such as on start, on failure, etc).
            Only Say is supported for now.
        max_retries (Union[Unset, float]): This is the number of times we should try to gather the information from the
            user before we failover to the fail path. An example of this would be a user refusing to give their phone number
            for privacy reasons, and then going down a different path on account of this
        literal_template (Union[Unset, str]): This is a liquid templating string. On the first call to Gather, the
            template will be filled out with variables from the context, and will be spoken verbatim to the user. An example
            would be "Base on your zipcode, it looks like you could be in one of these counties: {{ counties | join: ", "
            }}. Which one do you live in?"
        metadata (Union[Unset, GatherMetadata]): This is for metadata you want to store on the task.
    """

    type_: GatherType
    output: "JsonSchema"
    name: str
    confirm_content: Union[Unset, bool] = UNSET
    hooks: Union[Unset, list["Hook"]] = UNSET
    max_retries: Union[Unset, float] = UNSET
    literal_template: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GatherMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        output = self.output.to_dict()

        name = self.name

        confirm_content = self.confirm_content

        hooks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.hooks, Unset):
            hooks = []
            for hooks_item_data in self.hooks:
                hooks_item = hooks_item_data.to_dict()
                hooks.append(hooks_item)

        max_retries = self.max_retries

        literal_template = self.literal_template

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "output": output,
                "name": name,
            }
        )
        if confirm_content is not UNSET:
            field_dict["confirmContent"] = confirm_content
        if hooks is not UNSET:
            field_dict["hooks"] = hooks
        if max_retries is not UNSET:
            field_dict["maxRetries"] = max_retries
        if literal_template is not UNSET:
            field_dict["literalTemplate"] = literal_template
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gather_metadata import GatherMetadata
        from ..models.hook import Hook
        from ..models.json_schema import JsonSchema

        d = dict(src_dict)
        type_ = GatherType(d.pop("type"))

        output = JsonSchema.from_dict(d.pop("output"))

        name = d.pop("name")

        confirm_content = d.pop("confirmContent", UNSET)

        hooks = []
        _hooks = d.pop("hooks", UNSET)
        for hooks_item_data in _hooks or []:
            hooks_item = Hook.from_dict(hooks_item_data)

            hooks.append(hooks_item)

        max_retries = d.pop("maxRetries", UNSET)

        literal_template = d.pop("literalTemplate", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GatherMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GatherMetadata.from_dict(_metadata)

        gather = cls(
            type_=type_,
            output=output,
            name=name,
            confirm_content=confirm_content,
            hooks=hooks,
            max_retries=max_retries,
            literal_template=literal_template,
            metadata=metadata,
        )

        gather.additional_properties = d
        return gather

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
