from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completion_message import ChatCompletionMessage
    from ..models.create_workflow_dto import CreateWorkflowDTO


T = TypeVar("T", bound="ChatCompletionsDTO")


@_attrs_define
class ChatCompletionsDTO:
    """
    Attributes:
        messages (list['ChatCompletionMessage']):
        workflow_id (Union[Unset, str]):
        workflow (Union[Unset, CreateWorkflowDTO]):
    """

    messages: list["ChatCompletionMessage"]
    workflow_id: Union[Unset, str] = UNSET
    workflow: Union[Unset, "CreateWorkflowDTO"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        workflow_id = self.workflow_id

        workflow: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messages": messages,
            }
        )
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.chat_completion_message import ChatCompletionMessage
        from ..models.create_workflow_dto import CreateWorkflowDTO

        d = src_dict.copy()
        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = ChatCompletionMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        workflow_id = d.pop("workflowId", UNSET)

        _workflow = d.pop("workflow", UNSET)
        workflow: Union[Unset, CreateWorkflowDTO]
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = CreateWorkflowDTO.from_dict(_workflow)

        chat_completions_dto = cls(
            messages=messages,
            workflow_id=workflow_id,
            workflow=workflow,
        )

        chat_completions_dto.additional_properties = d
        return chat_completions_dto

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
