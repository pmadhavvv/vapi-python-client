from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_message_workflow_node_started_type import ClientMessageWorkflowNodeStartedType

if TYPE_CHECKING:
    from ..models.client_message_workflow_node_started_node import ClientMessageWorkflowNodeStartedNode


T = TypeVar("T", bound="ClientMessageWorkflowNodeStarted")


@_attrs_define
class ClientMessageWorkflowNodeStarted:
    """
    Attributes:
        type_ (ClientMessageWorkflowNodeStartedType): This is the type of the message. "workflow.node.started" is sent
            when the active node changes.
        node (ClientMessageWorkflowNodeStartedNode): This is the active node.
    """

    type_: ClientMessageWorkflowNodeStartedType
    node: "ClientMessageWorkflowNodeStartedNode"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        node = self.node.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "node": node,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.client_message_workflow_node_started_node import ClientMessageWorkflowNodeStartedNode

        d = src_dict.copy()
        type_ = ClientMessageWorkflowNodeStartedType(d.pop("type"))

        node = ClientMessageWorkflowNodeStartedNode.from_dict(d.pop("node"))

        client_message_workflow_node_started = cls(
            type_=type_,
            node=node,
        )

        client_message_workflow_node_started.additional_properties = d
        return client_message_workflow_node_started

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
