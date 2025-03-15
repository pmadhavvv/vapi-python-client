from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_vapi_phone_number_dto_provider import CreateVapiPhoneNumberDTOProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server import Server
    from ..models.sip_authentication import SipAuthentication
    from ..models.transfer_destination_number import TransferDestinationNumber
    from ..models.transfer_destination_sip import TransferDestinationSip


T = TypeVar("T", bound="CreateVapiPhoneNumberDTO")


@_attrs_define
class CreateVapiPhoneNumberDTO:
    """
    Attributes:
        provider (CreateVapiPhoneNumberDTOProvider): This is to create free SIP phone numbers on Vapi.
        fallback_destination (Union['TransferDestinationNumber', 'TransferDestinationSip', Unset]): This is the fallback
            destination an inbound call will be transferred to if:
            1. `assistantId` is not set
            2. `squadId` is not set
            3. and, `assistant-request` message to the `serverUrl` fails

            If this is not set and above conditions are met, the inbound call is hung up with an error message.
        number_desired_area_code (Union[Unset, str]): This is the area code of the phone number to purchase.
        sip_uri (Union[Unset, str]): This is the SIP URI of the phone number. You can SIP INVITE this. The assistant
            attached to this number will answer.

            This is case-insensitive.
        authentication (Union[Unset, SipAuthentication]):
        name (Union[Unset, str]): This is the name of the phone number. This is just for your own reference.
        assistant_id (Union[Unset, str]): This is the assistant that will be used for incoming calls to this phone
            number.

            If neither `assistantId` nor `squadId` is set, `assistant-request` will be sent to your Server URL. Check
            `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.
        squad_id (Union[Unset, str]): This is the squad that will be used for incoming calls to this phone number.

            If neither `assistantId` nor `squadId` is set, `assistant-request` will be sent to your Server URL. Check
            `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.
        server (Union[Unset, Server]):
    """

    provider: CreateVapiPhoneNumberDTOProvider
    fallback_destination: Union["TransferDestinationNumber", "TransferDestinationSip", Unset] = UNSET
    number_desired_area_code: Union[Unset, str] = UNSET
    sip_uri: Union[Unset, str] = UNSET
    authentication: Union[Unset, "SipAuthentication"] = UNSET
    name: Union[Unset, str] = UNSET
    assistant_id: Union[Unset, str] = UNSET
    squad_id: Union[Unset, str] = UNSET
    server: Union[Unset, "Server"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transfer_destination_number import TransferDestinationNumber

        provider = self.provider.value

        fallback_destination: Union[Unset, dict[str, Any]]
        if isinstance(self.fallback_destination, Unset):
            fallback_destination = UNSET
        elif isinstance(self.fallback_destination, TransferDestinationNumber):
            fallback_destination = self.fallback_destination.to_dict()
        else:
            fallback_destination = self.fallback_destination.to_dict()

        number_desired_area_code = self.number_desired_area_code

        sip_uri = self.sip_uri

        authentication: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = self.authentication.to_dict()

        name = self.name

        assistant_id = self.assistant_id

        squad_id = self.squad_id

        server: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if fallback_destination is not UNSET:
            field_dict["fallbackDestination"] = fallback_destination
        if number_desired_area_code is not UNSET:
            field_dict["numberDesiredAreaCode"] = number_desired_area_code
        if sip_uri is not UNSET:
            field_dict["sipUri"] = sip_uri
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if name is not UNSET:
            field_dict["name"] = name
        if assistant_id is not UNSET:
            field_dict["assistantId"] = assistant_id
        if squad_id is not UNSET:
            field_dict["squadId"] = squad_id
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.server import Server
        from ..models.sip_authentication import SipAuthentication
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_sip import TransferDestinationSip

        d = src_dict.copy()
        provider = CreateVapiPhoneNumberDTOProvider(d.pop("provider"))

        def _parse_fallback_destination(
            data: object,
        ) -> Union["TransferDestinationNumber", "TransferDestinationSip", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fallback_destination_type_0 = TransferDestinationNumber.from_dict(data)

                return fallback_destination_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            fallback_destination_type_1 = TransferDestinationSip.from_dict(data)

            return fallback_destination_type_1

        fallback_destination = _parse_fallback_destination(d.pop("fallbackDestination", UNSET))

        number_desired_area_code = d.pop("numberDesiredAreaCode", UNSET)

        sip_uri = d.pop("sipUri", UNSET)

        _authentication = d.pop("authentication", UNSET)
        authentication: Union[Unset, SipAuthentication]
        if isinstance(_authentication, Unset):
            authentication = UNSET
        else:
            authentication = SipAuthentication.from_dict(_authentication)

        name = d.pop("name", UNSET)

        assistant_id = d.pop("assistantId", UNSET)

        squad_id = d.pop("squadId", UNSET)

        _server = d.pop("server", UNSET)
        server: Union[Unset, Server]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = Server.from_dict(_server)

        create_vapi_phone_number_dto = cls(
            provider=provider,
            fallback_destination=fallback_destination,
            number_desired_area_code=number_desired_area_code,
            sip_uri=sip_uri,
            authentication=authentication,
            name=name,
            assistant_id=assistant_id,
            squad_id=squad_id,
            server=server,
        )

        create_vapi_phone_number_dto.additional_properties = d
        return create_vapi_phone_number_dto

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
