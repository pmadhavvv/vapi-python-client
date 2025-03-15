from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completion_message_metadata_task_state import ChatCompletionMessageMetadataTaskState


T = TypeVar("T", bound="ChatCompletionMessageMetadata")


@_attrs_define
class ChatCompletionMessageMetadata:
    """
    Attributes:
        task_name (str):
        task_type (str):
        task_output (str):
        task_state (Union[Unset, ChatCompletionMessageMetadataTaskState]):
        node_trace (Union[Unset, list[str]]):
    """

    task_name: str
    task_type: str
    task_output: str
    task_state: Union[Unset, "ChatCompletionMessageMetadataTaskState"] = UNSET
    node_trace: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_name = self.task_name

        task_type = self.task_type

        task_output = self.task_output

        task_state: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.task_state, Unset):
            task_state = self.task_state.to_dict()

        node_trace: Union[Unset, list[str]] = UNSET
        if not isinstance(self.node_trace, Unset):
            node_trace = self.node_trace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taskName": task_name,
                "taskType": task_type,
                "taskOutput": task_output,
            }
        )
        if task_state is not UNSET:
            field_dict["taskState"] = task_state
        if node_trace is not UNSET:
            field_dict["nodeTrace"] = node_trace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.chat_completion_message_metadata_task_state import ChatCompletionMessageMetadataTaskState

        d = src_dict.copy()
        task_name = d.pop("taskName")

        task_type = d.pop("taskType")

        task_output = d.pop("taskOutput")

        _task_state = d.pop("taskState", UNSET)
        task_state: Union[Unset, ChatCompletionMessageMetadataTaskState]
        if isinstance(_task_state, Unset):
            task_state = UNSET
        else:
            task_state = ChatCompletionMessageMetadataTaskState.from_dict(_task_state)

        node_trace = cast(list[str], d.pop("nodeTrace", UNSET))

        chat_completion_message_metadata = cls(
            task_name=task_name,
            task_type=task_type,
            task_output=task_output,
            task_state=task_state,
            node_trace=node_trace,
        )

        chat_completion_message_metadata.additional_properties = d
        return chat_completion_message_metadata

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
