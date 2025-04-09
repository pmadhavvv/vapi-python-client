from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_request import ApiRequest
    from ..models.edge import Edge
    from ..models.gather import Gather
    from ..models.hangup import Hangup
    from ..models.say import Say
    from ..models.transfer import Transfer


T = TypeVar("T", bound="CreateWorkflowDTO")


@_attrs_define
class CreateWorkflowDTO:
    """
    Attributes:
        nodes (list[Union['ApiRequest', 'Gather', 'Hangup', 'Say', 'Transfer']]):
        name (str):
        edges (list['Edge']):
    """

    nodes: list[Union["ApiRequest", "Gather", "Hangup", "Say", "Transfer"]]
    name: str
    edges: list["Edge"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_request import ApiRequest
        from ..models.gather import Gather
        from ..models.hangup import Hangup
        from ..models.say import Say

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item: dict[str, Any]
            if isinstance(nodes_item_data, Say):
                nodes_item = nodes_item_data.to_dict()
            elif isinstance(nodes_item_data, Gather):
                nodes_item = nodes_item_data.to_dict()
            elif isinstance(nodes_item_data, ApiRequest):
                nodes_item = nodes_item_data.to_dict()
            elif isinstance(nodes_item_data, Hangup):
                nodes_item = nodes_item_data.to_dict()
            else:
                nodes_item = nodes_item_data.to_dict()

            nodes.append(nodes_item)

        name = self.name

        edges = []
        for edges_item_data in self.edges:
            edges_item = edges_item_data.to_dict()
            edges.append(edges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodes": nodes,
                "name": name,
                "edges": edges,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_request import ApiRequest
        from ..models.edge import Edge
        from ..models.gather import Gather
        from ..models.hangup import Hangup
        from ..models.say import Say
        from ..models.transfer import Transfer

        d = dict(src_dict)
        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:

            def _parse_nodes_item(data: object) -> Union["ApiRequest", "Gather", "Hangup", "Say", "Transfer"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    nodes_item_type_0 = Say.from_dict(data)

                    return nodes_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    nodes_item_type_1 = Gather.from_dict(data)

                    return nodes_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    nodes_item_type_2 = ApiRequest.from_dict(data)

                    return nodes_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    nodes_item_type_3 = Hangup.from_dict(data)

                    return nodes_item_type_3
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                nodes_item_type_4 = Transfer.from_dict(data)

                return nodes_item_type_4

            nodes_item = _parse_nodes_item(nodes_item_data)

            nodes.append(nodes_item)

        name = d.pop("name")

        edges = []
        _edges = d.pop("edges")
        for edges_item_data in _edges:
            edges_item = Edge.from_dict(edges_item_data)

            edges.append(edges_item)

        create_workflow_dto = cls(
            nodes=nodes,
            name=name,
            edges=edges,
        )

        create_workflow_dto.additional_properties = d
        return create_workflow_dto

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
