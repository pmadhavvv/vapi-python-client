from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_org_dto_channel import CreateOrgDTOChannel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server import Server


T = TypeVar("T", bound="CreateOrgDTO")


@_attrs_define
class CreateOrgDTO:
    """
    Attributes:
        hipaa_enabled (Union[Unset, bool]): When this is enabled, no logs, recordings, or transcriptions will be stored.
            At the end of the call, you will still receive an end-of-call-report message to store on your server. Defaults
            to false.
            When HIPAA is enabled, only OpenAI/Custom LLM or Azure Providers will be available for LLM and Voice
            respectively.
            This is due to the compliance requirements of HIPAA. Other providers may not meet these requirements.
        subscription_id (Union[Unset, str]): This is the ID of the subscription the org belongs to.
        name (Union[Unset, str]): This is the name of the org. This is just for your own reference.
        channel (Union[Unset, CreateOrgDTOChannel]): This is the channel of the org. There is the cluster the API
            traffic for the org will be directed.
        billing_limit (Union[Unset, float]): This is the monthly billing limit for the org. To go beyond $1000/mo,
            please contact us at support@vapi.ai.
        server (Union[Unset, Server]):
        concurrency_limit (Union[Unset, float]): This is the concurrency limit for the org. This is the maximum number
            of calls that can be active at any given time. To go beyond 10, please contact us at support@vapi.ai.
    """

    hipaa_enabled: Union[Unset, bool] = UNSET
    subscription_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    channel: Union[Unset, CreateOrgDTOChannel] = UNSET
    billing_limit: Union[Unset, float] = UNSET
    server: Union[Unset, "Server"] = UNSET
    concurrency_limit: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hipaa_enabled = self.hipaa_enabled

        subscription_id = self.subscription_id

        name = self.name

        channel: Union[Unset, str] = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value

        billing_limit = self.billing_limit

        server: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        concurrency_limit = self.concurrency_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hipaa_enabled is not UNSET:
            field_dict["hipaaEnabled"] = hipaa_enabled
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if name is not UNSET:
            field_dict["name"] = name
        if channel is not UNSET:
            field_dict["channel"] = channel
        if billing_limit is not UNSET:
            field_dict["billingLimit"] = billing_limit
        if server is not UNSET:
            field_dict["server"] = server
        if concurrency_limit is not UNSET:
            field_dict["concurrencyLimit"] = concurrency_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server import Server

        d = dict(src_dict)
        hipaa_enabled = d.pop("hipaaEnabled", UNSET)

        subscription_id = d.pop("subscriptionId", UNSET)

        name = d.pop("name", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: Union[Unset, CreateOrgDTOChannel]
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = CreateOrgDTOChannel(_channel)

        billing_limit = d.pop("billingLimit", UNSET)

        _server = d.pop("server", UNSET)
        server: Union[Unset, Server]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = Server.from_dict(_server)

        concurrency_limit = d.pop("concurrencyLimit", UNSET)

        create_org_dto = cls(
            hipaa_enabled=hipaa_enabled,
            subscription_id=subscription_id,
            name=name,
            channel=channel,
            billing_limit=billing_limit,
            server=server,
            concurrency_limit=concurrency_limit,
        )

        create_org_dto.additional_properties = d
        return create_org_dto

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
