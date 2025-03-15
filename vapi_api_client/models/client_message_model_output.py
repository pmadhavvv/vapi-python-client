from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_message_model_output_type import ClientMessageModelOutputType

if TYPE_CHECKING:
    from ..models.client_message_model_output_output import ClientMessageModelOutputOutput


T = TypeVar("T", bound="ClientMessageModelOutput")


@_attrs_define
class ClientMessageModelOutput:
    """
    Attributes:
        type_ (ClientMessageModelOutputType): This is the type of the message. "model-output" is sent as the model
            outputs tokens.
        output (ClientMessageModelOutputOutput): This is the output of the model. It can be a token or tool call.
    """

    type_: ClientMessageModelOutputType
    output: "ClientMessageModelOutputOutput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        output = self.output.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "output": output,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.client_message_model_output_output import ClientMessageModelOutputOutput

        d = src_dict.copy()
        type_ = ClientMessageModelOutputType(d.pop("type"))

        output = ClientMessageModelOutputOutput.from_dict(d.pop("output"))

        client_message_model_output = cls(
            type_=type_,
            output=output,
        )

        client_message_model_output.additional_properties = d
        return client_message_model_output

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
