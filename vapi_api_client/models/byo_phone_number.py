import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.byo_phone_number_provider import ByoPhoneNumberProvider
from ..models.byo_phone_number_status import ByoPhoneNumberStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server import Server
    from ..models.transfer_destination_number import TransferDestinationNumber
    from ..models.transfer_destination_sip import TransferDestinationSip


T = TypeVar("T", bound="ByoPhoneNumber")


@_attrs_define
class ByoPhoneNumber:
    r"""
    Attributes:
        provider (ByoPhoneNumberProvider): This is to bring your own phone numbers from your own SIP trunks or Carriers.
        id (str): This is the unique identifier for the phone number.
        org_id (str): This is the unique identifier for the org that this phone number belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the phone number was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the phone number was last updated.
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
        status (Union[Unset, ByoPhoneNumberStatus]): This is the status of the phone number.
        name (Union[Unset, str]): This is the name of the phone number. This is just for your own reference.
        assistant_id (Union[Unset, str]): This is the assistant that will be used for incoming calls to this phone
            number.

            If neither `assistantId` nor `squadId` is set, `assistant-request` will be sent to your Server URL. Check
            `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.
        squad_id (Union[Unset, str]): This is the squad that will be used for incoming calls to this phone number.

            If neither `assistantId` nor `squadId` is set, `assistant-request` will be sent to your Server URL. Check
            `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.
        server (Union[Unset, Server]):
        number (Union[Unset, str]): This is the number of the customer.
    """

    provider: ByoPhoneNumberProvider
    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    credential_id: str
    fallback_destination: Union["TransferDestinationNumber", "TransferDestinationSip", Unset] = UNSET
    number_e164_check_enabled: Union[Unset, bool] = UNSET
    status: Union[Unset, ByoPhoneNumberStatus] = UNSET
    name: Union[Unset, str] = UNSET
    assistant_id: Union[Unset, str] = UNSET
    squad_id: Union[Unset, str] = UNSET
    server: Union[Unset, "Server"] = UNSET
    number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transfer_destination_number import TransferDestinationNumber

        provider = self.provider.value

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        credential_id = self.credential_id

        fallback_destination: Union[Unset, dict[str, Any]]
        if isinstance(self.fallback_destination, Unset):
            fallback_destination = UNSET
        elif isinstance(self.fallback_destination, TransferDestinationNumber):
            fallback_destination = self.fallback_destination.to_dict()
        else:
            fallback_destination = self.fallback_destination.to_dict()

        number_e164_check_enabled = self.number_e164_check_enabled

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        name = self.name

        assistant_id = self.assistant_id

        squad_id = self.squad_id

        server: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "credentialId": credential_id,
            }
        )
        if fallback_destination is not UNSET:
            field_dict["fallbackDestination"] = fallback_destination
        if number_e164_check_enabled is not UNSET:
            field_dict["numberE164CheckEnabled"] = number_e164_check_enabled
        if status is not UNSET:
            field_dict["status"] = status
        if name is not UNSET:
            field_dict["name"] = name
        if assistant_id is not UNSET:
            field_dict["assistantId"] = assistant_id
        if squad_id is not UNSET:
            field_dict["squadId"] = squad_id
        if server is not UNSET:
            field_dict["server"] = server
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.server import Server
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_sip import TransferDestinationSip

        d = src_dict.copy()
        provider = ByoPhoneNumberProvider(d.pop("provider"))

        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

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

        _status = d.pop("status", UNSET)
        status: Union[Unset, ByoPhoneNumberStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ByoPhoneNumberStatus(_status)

        name = d.pop("name", UNSET)

        assistant_id = d.pop("assistantId", UNSET)

        squad_id = d.pop("squadId", UNSET)

        _server = d.pop("server", UNSET)
        server: Union[Unset, Server]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = Server.from_dict(_server)

        number = d.pop("number", UNSET)

        byo_phone_number = cls(
            provider=provider,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            credential_id=credential_id,
            fallback_destination=fallback_destination,
            number_e164_check_enabled=number_e164_check_enabled,
            status=status,
            name=name,
            assistant_id=assistant_id,
            squad_id=squad_id,
            server=server,
            number=number,
        )

        byo_phone_number.additional_properties = d
        return byo_phone_number

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
