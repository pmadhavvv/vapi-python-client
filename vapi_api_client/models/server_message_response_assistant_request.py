from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_overrides import AssistantOverrides
    from ..models.create_assistant_dto import CreateAssistantDTO
    from ..models.create_squad_dto import CreateSquadDTO
    from ..models.transfer_destination_number import TransferDestinationNumber
    from ..models.transfer_destination_sip import TransferDestinationSip


T = TypeVar("T", bound="ServerMessageResponseAssistantRequest")


@_attrs_define
class ServerMessageResponseAssistantRequest:
    """
    Attributes:
        destination (Union['TransferDestinationNumber', 'TransferDestinationSip', Unset]): This is the destination to
            transfer the inbound call to. This will immediately transfer without using any assistants.

            If this is sent, `assistantId`, `assistant`, `squadId`, and `squad` are ignored.
        assistant_id (Union[None, Unset, str]): This is the assistant that will be used for the call. To use a transient
            assistant, use `assistant` instead.
        assistant (Union[Unset, CreateAssistantDTO]):
        assistant_overrides (Union[Unset, AssistantOverrides]):
        squad_id (Union[Unset, str]): This is the squad that will be used for the call. To use a transient squad, use
            `squad` instead.
        squad (Union[Unset, CreateSquadDTO]):
        error (Union[Unset, str]): This is the error if the call shouldn't be accepted. This is spoken to the customer.

            If this is sent, `assistantId`, `assistant`, `squadId`, `squad`, and `destination` are ignored.
    """

    destination: Union["TransferDestinationNumber", "TransferDestinationSip", Unset] = UNSET
    assistant_id: Union[None, Unset, str] = UNSET
    assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    assistant_overrides: Union[Unset, "AssistantOverrides"] = UNSET
    squad_id: Union[Unset, str] = UNSET
    squad: Union[Unset, "CreateSquadDTO"] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transfer_destination_number import TransferDestinationNumber

        destination: Union[Unset, dict[str, Any]]
        if isinstance(self.destination, Unset):
            destination = UNSET
        elif isinstance(self.destination, TransferDestinationNumber):
            destination = self.destination.to_dict()
        else:
            destination = self.destination.to_dict()

        assistant_id: Union[None, Unset, str]
        if isinstance(self.assistant_id, Unset):
            assistant_id = UNSET
        else:
            assistant_id = self.assistant_id

        assistant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assistant, Unset):
            assistant = self.assistant.to_dict()

        assistant_overrides: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assistant_overrides, Unset):
            assistant_overrides = self.assistant_overrides.to_dict()

        squad_id = self.squad_id

        squad: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.squad, Unset):
            squad = self.squad.to_dict()

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination is not UNSET:
            field_dict["destination"] = destination
        if assistant_id is not UNSET:
            field_dict["assistantId"] = assistant_id
        if assistant is not UNSET:
            field_dict["assistant"] = assistant
        if assistant_overrides is not UNSET:
            field_dict["assistantOverrides"] = assistant_overrides
        if squad_id is not UNSET:
            field_dict["squadId"] = squad_id
        if squad is not UNSET:
            field_dict["squad"] = squad
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.assistant_overrides import AssistantOverrides
        from ..models.create_assistant_dto import CreateAssistantDTO
        from ..models.create_squad_dto import CreateSquadDTO
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_sip import TransferDestinationSip

        d = src_dict.copy()

        def _parse_destination(data: object) -> Union["TransferDestinationNumber", "TransferDestinationSip", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                destination_type_0 = TransferDestinationNumber.from_dict(data)

                return destination_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            destination_type_1 = TransferDestinationSip.from_dict(data)

            return destination_type_1

        destination = _parse_destination(d.pop("destination", UNSET))

        def _parse_assistant_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assistant_id = _parse_assistant_id(d.pop("assistantId", UNSET))

        _assistant = d.pop("assistant", UNSET)
        assistant: Union[Unset, CreateAssistantDTO]
        if isinstance(_assistant, Unset):
            assistant = UNSET
        else:
            assistant = CreateAssistantDTO.from_dict(_assistant)

        _assistant_overrides = d.pop("assistantOverrides", UNSET)
        assistant_overrides: Union[Unset, AssistantOverrides]
        if isinstance(_assistant_overrides, Unset):
            assistant_overrides = UNSET
        else:
            assistant_overrides = AssistantOverrides.from_dict(_assistant_overrides)

        squad_id = d.pop("squadId", UNSET)

        _squad = d.pop("squad", UNSET)
        squad: Union[Unset, CreateSquadDTO]
        if isinstance(_squad, Unset):
            squad = UNSET
        else:
            squad = CreateSquadDTO.from_dict(_squad)

        error = d.pop("error", UNSET)

        server_message_response_assistant_request = cls(
            destination=destination,
            assistant_id=assistant_id,
            assistant=assistant,
            assistant_overrides=assistant_overrides,
            squad_id=squad_id,
            squad=squad,
            error=error,
        )

        server_message_response_assistant_request.additional_properties = d
        return server_message_response_assistant_request

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
