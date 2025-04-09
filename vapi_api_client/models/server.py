from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backoff_plan import BackoffPlan
    from ..models.server_headers import ServerHeaders


T = TypeVar("T", bound="Server")


@_attrs_define
class Server:
    """
    Attributes:
        url (str): API endpoint to send requests to.
        timeout_seconds (Union[Unset, float]): This is the timeout in seconds for the request to your server. Defaults
            to 20 seconds.

            @default 20 Example: 20.
        secret (Union[Unset, str]): This is the secret you can set that Vapi will send with every request to your
            server. Will be sent as a header called x-vapi-secret.

            Same precedence logic as server.
        headers (Union[Unset, ServerHeaders]): These are the custom headers to include in the request sent to your
            server.

            Each key-value pair represents a header name and its value.
        backoff_plan (Union[Unset, BackoffPlan]):
    """

    url: str
    timeout_seconds: Union[Unset, float] = UNSET
    secret: Union[Unset, str] = UNSET
    headers: Union[Unset, "ServerHeaders"] = UNSET
    backoff_plan: Union[Unset, "BackoffPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        timeout_seconds = self.timeout_seconds

        secret = self.secret

        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        backoff_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backoff_plan, Unset):
            backoff_plan = self.backoff_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds
        if secret is not UNSET:
            field_dict["secret"] = secret
        if headers is not UNSET:
            field_dict["headers"] = headers
        if backoff_plan is not UNSET:
            field_dict["backoffPlan"] = backoff_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backoff_plan import BackoffPlan
        from ..models.server_headers import ServerHeaders

        d = dict(src_dict)
        url = d.pop("url")

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        secret = d.pop("secret", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, ServerHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = ServerHeaders.from_dict(_headers)

        _backoff_plan = d.pop("backoffPlan", UNSET)
        backoff_plan: Union[Unset, BackoffPlan]
        if isinstance(_backoff_plan, Unset):
            backoff_plan = UNSET
        else:
            backoff_plan = BackoffPlan.from_dict(_backoff_plan)

        server = cls(
            url=url,
            timeout_seconds=timeout_seconds,
            secret=secret,
            headers=headers,
            backoff_plan=backoff_plan,
        )

        server.additional_properties = d
        return server

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
