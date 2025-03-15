from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_byo_phone_number_dto_provider import CreateByoPhoneNumberDTOProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server import Server
    from ..models.transfer_destination_number import TransferDestinationNumber
    from ..models.transfer_destination_sip import TransferDestinationSip


T = TypeVar("T", bound="CreateByoPhoneNumberDTO")


@_attrs_define
class CreateByoPhoneNumberDTO:
    r"""
    Attributes:
        provider (CreateByoPhoneNumberDTOProvider): This is to bring your own phone numbers from your own SIP trunks or
            Carriers.
        credential_id (str): This is the credential of your own SIP trunk or Carrier (type `byo-sip-trunk`) which can be
            used to make calls to this phone number.

            You can add the SIP trunk or Carrier credential in the Provider Credentials page on the Dashboard to get the
            credentialId.
        fallback_destination (Union['TransferDestinationNumber', 'TransferDestinationSip', Unset]): This is the fallback
            destination an inbound call will be transferred to if:
            1. `assistantId` is not set
            2. `squadId` is not set
            3. and, `assistant-request` message to the `serverUrl` fails

            If this is not set and above conditions are met, the inbound call is hung up with an error message.
        number_e164_check_enabled (Union[Unset, bool]): This is the flag to toggle the E164 check for the `number`
            field. This is an advanced property which should be used if you know your use case requires it.

            Use cases:
            - `false`: To allow non-E164 numbers like `+001234567890`, `1234`, or `abc`. This is useful for dialing out to
            non-E164 numbers on your SIP trunks.
            - `true` (default): To allow only E164 numbers like `+14155551234`. This is standard for PSTN calls.

            If `false`, the `number` is still required to only contain alphanumeric characters (regex:
            `/^\+?[a-zA-Z0-9]+$/`).

            @default true (E164 check is enabled)
        number (Union[Unset, str]): This is the number of the customer.
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

    provider: CreateByoPhoneNumberDTOProvider
    credential_id: str
    fallback_destination: Union["TransferDestinationNumber", "TransferDestinationSip", Unset] = UNSET
    number_e164_check_enabled: Union[Unset, bool] = UNSET
    number: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    assistant_id: Union[Unset, str] = UNSET
    squad_id: Union[Unset, str] = UNSET
    server: Union[Unset, "Server"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transfer_destination_number import TransferDestinationNumber

        provider = self.provider.value

        credential_id = self.credential_id

        fallback_destination: Union[Unset, dict[str, Any]]
        if isinstance(self.fallback_destination, Unset):
            fallback_destination = UNSET
        elif isinstance(self.fallback_destination, TransferDestinationNumber):
            fallback_destination = self.fallback_destination.to_dict()
        else:
            fallback_destination = self.fallback_destination.to_dict()

        number_e164_check_enabled = self.number_e164_check_enabled

        number = self.number

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
                "credentialId": credential_id,
            }
        )
        if fallback_destination is not UNSET:
            field_dict["fallbackDestination"] = fallback_destination
        if number_e164_check_enabled is not UNSET:
            field_dict["numberE164CheckEnabled"] = number_e164_check_enabled
        if number is not UNSET:
            field_dict["number"] = number
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
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_sip import TransferDestinationSip

        d = src_dict.copy()
        provider = CreateByoPhoneNumberDTOProvider(d.pop("provider"))

        credential_id = d.pop("credentialId")

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

        number_e164_check_enabled = d.pop("numberE164CheckEnabled", UNSET)

        number = d.pop("number", UNSET)

        name = d.pop("name", UNSET)

        assistant_id = d.pop("assistantId", UNSET)

        squad_id = d.pop("squadId", UNSET)

        _server = d.pop("server", UNSET)
        server: Union[Unset, Server]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = Server.from_dict(_server)

        create_byo_phone_number_dto = cls(
            provider=provider,
            credential_id=credential_id,
            fallback_destination=fallback_destination,
            number_e164_check_enabled=number_e164_check_enabled,
            number=number,
            name=name,
            assistant_id=assistant_id,
            squad_id=squad_id,
            server=server,
        )

        create_byo_phone_number_dto.additional_properties = d
        return create_byo_phone_number_dto

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
