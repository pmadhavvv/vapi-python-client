from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_edge_condition import AIEdgeCondition
    from ..models.edge_metadata import EdgeMetadata
    from ..models.failed_edge_condition import FailedEdgeCondition
    from ..models.logic_edge_condition import LogicEdgeCondition


T = TypeVar("T", bound="Edge")


@_attrs_define
class Edge:
    """
    Attributes:
        from_ (str):
        to (str):
        condition (Union['AIEdgeCondition', 'FailedEdgeCondition', 'LogicEdgeCondition', Unset]):
        metadata (Union[Unset, EdgeMetadata]): This is for metadata you want to store on the edge.
    """

    from_: str
    to: str
    condition: Union["AIEdgeCondition", "FailedEdgeCondition", "LogicEdgeCondition", Unset] = UNSET
    metadata: Union[Unset, "EdgeMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ai_edge_condition import AIEdgeCondition
        from ..models.logic_edge_condition import LogicEdgeCondition

        from_ = self.from_

        to = self.to

        condition: Union[Unset, dict[str, Any]]
        if isinstance(self.condition, Unset):
            condition = UNSET
        elif isinstance(self.condition, AIEdgeCondition):
            condition = self.condition.to_dict()
        elif isinstance(self.condition, LogicEdgeCondition):
            condition = self.condition.to_dict()
        else:
            condition = self.condition.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
            }
        )
        if condition is not UNSET:
            field_dict["condition"] = condition
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.ai_edge_condition import AIEdgeCondition
        from ..models.edge_metadata import EdgeMetadata
        from ..models.failed_edge_condition import FailedEdgeCondition
        from ..models.logic_edge_condition import LogicEdgeCondition

        d = src_dict.copy()
        from_ = d.pop("from")

        to = d.pop("to")

        def _parse_condition(
            data: object,
        ) -> Union["AIEdgeCondition", "FailedEdgeCondition", "LogicEdgeCondition", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                condition_type_0 = AIEdgeCondition.from_dict(data)

                return condition_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                condition_type_1 = LogicEdgeCondition.from_dict(data)

                return condition_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            condition_type_2 = FailedEdgeCondition.from_dict(data)

            return condition_type_2

        condition = _parse_condition(d.pop("condition", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, EdgeMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = EdgeMetadata.from_dict(_metadata)

        edge = cls(
            from_=from_,
            to=to,
            condition=condition,
            metadata=metadata,
        )

        edge.additional_properties = d
        return edge

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
