from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.log_request_http_method import LogRequestHttpMethod
from ..models.log_resource import LogResource
from ..models.log_type import LogType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error
    from ..models.log_request_body import LogRequestBody
    from ..models.log_request_headers import LogRequestHeaders
    from ..models.log_response_body import LogResponseBody


T = TypeVar("T", bound="Log")


@_attrs_define
class Log:
    """
    Attributes:
        time (str): This is the timestamp at which the log was written.
        org_id (str): This is the unique identifier for the org that this log belongs to.
        type_ (LogType): This is the type of the log.
        webhook_type (Union[Unset, str]): This is the type of the webhook, given the log is from a webhook.
        resource (Union[Unset, LogResource]): This is the specific resource, relevant only to API logs.
        request_duration_seconds (Union[Unset, float]): 'This is how long the request took.
        request_started_at (Union[Unset, str]): This is the timestamp at which the request began.
        request_finished_at (Union[Unset, str]): This is the timestamp at which the request finished.
        request_body (Union[Unset, LogRequestBody]): This is the body of the request.
        request_http_method (Union[Unset, LogRequestHttpMethod]): This is the request method.
        request_url (Union[Unset, str]): This is the request URL.
        request_path (Union[Unset, str]): This is the request path.
        request_query (Union[Unset, str]): This is the request query.
        response_http_code (Union[Unset, float]): This the HTTP status code of the response.
        request_ip_address (Union[Unset, str]): This is the request IP address.
        request_origin (Union[Unset, str]): This is the origin of the request
        response_body (Union[Unset, LogResponseBody]): This is the body of the response.
        request_headers (Union[Unset, LogRequestHeaders]): These are the headers of the request.
        error (Union[Unset, Error]):
        assistant_id (Union[Unset, str]): This is the ID of the assistant.
        phone_number_id (Union[Unset, str]): This is the ID of the phone number.
        customer_id (Union[Unset, str]): This is the ID of the customer.
        squad_id (Union[Unset, str]): This is the ID of the squad.
        call_id (Union[Unset, str]): This is the ID of the call.
    """

    time: str
    org_id: str
    type_: LogType
    webhook_type: Union[Unset, str] = UNSET
    resource: Union[Unset, LogResource] = UNSET
    request_duration_seconds: Union[Unset, float] = UNSET
    request_started_at: Union[Unset, str] = UNSET
    request_finished_at: Union[Unset, str] = UNSET
    request_body: Union[Unset, "LogRequestBody"] = UNSET
    request_http_method: Union[Unset, LogRequestHttpMethod] = UNSET
    request_url: Union[Unset, str] = UNSET
    request_path: Union[Unset, str] = UNSET
    request_query: Union[Unset, str] = UNSET
    response_http_code: Union[Unset, float] = UNSET
    request_ip_address: Union[Unset, str] = UNSET
    request_origin: Union[Unset, str] = UNSET
    response_body: Union[Unset, "LogResponseBody"] = UNSET
    request_headers: Union[Unset, "LogRequestHeaders"] = UNSET
    error: Union[Unset, "Error"] = UNSET
    assistant_id: Union[Unset, str] = UNSET
    phone_number_id: Union[Unset, str] = UNSET
    customer_id: Union[Unset, str] = UNSET
    squad_id: Union[Unset, str] = UNSET
    call_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        org_id = self.org_id

        type_ = self.type_.value

        webhook_type = self.webhook_type

        resource: Union[Unset, str] = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.value

        request_duration_seconds = self.request_duration_seconds

        request_started_at = self.request_started_at

        request_finished_at = self.request_finished_at

        request_body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.request_body, Unset):
            request_body = self.request_body.to_dict()

        request_http_method: Union[Unset, str] = UNSET
        if not isinstance(self.request_http_method, Unset):
            request_http_method = self.request_http_method.value

        request_url = self.request_url

        request_path = self.request_path

        request_query = self.request_query

        response_http_code = self.response_http_code

        request_ip_address = self.request_ip_address

        request_origin = self.request_origin

        response_body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.response_body, Unset):
            response_body = self.response_body.to_dict()

        request_headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.request_headers, Unset):
            request_headers = self.request_headers.to_dict()

        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        assistant_id = self.assistant_id

        phone_number_id = self.phone_number_id

        customer_id = self.customer_id

        squad_id = self.squad_id

        call_id = self.call_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
                "orgId": org_id,
                "type": type_,
            }
        )
        if webhook_type is not UNSET:
            field_dict["webhookType"] = webhook_type
        if resource is not UNSET:
            field_dict["resource"] = resource
        if request_duration_seconds is not UNSET:
            field_dict["requestDurationSeconds"] = request_duration_seconds
        if request_started_at is not UNSET:
            field_dict["requestStartedAt"] = request_started_at
        if request_finished_at is not UNSET:
            field_dict["requestFinishedAt"] = request_finished_at
        if request_body is not UNSET:
            field_dict["requestBody"] = request_body
        if request_http_method is not UNSET:
            field_dict["requestHttpMethod"] = request_http_method
        if request_url is not UNSET:
            field_dict["requestUrl"] = request_url
        if request_path is not UNSET:
            field_dict["requestPath"] = request_path
        if request_query is not UNSET:
            field_dict["requestQuery"] = request_query
        if response_http_code is not UNSET:
            field_dict["responseHttpCode"] = response_http_code
        if request_ip_address is not UNSET:
            field_dict["requestIpAddress"] = request_ip_address
        if request_origin is not UNSET:
            field_dict["requestOrigin"] = request_origin
        if response_body is not UNSET:
            field_dict["responseBody"] = response_body
        if request_headers is not UNSET:
            field_dict["requestHeaders"] = request_headers
        if error is not UNSET:
            field_dict["error"] = error
        if assistant_id is not UNSET:
            field_dict["assistantId"] = assistant_id
        if phone_number_id is not UNSET:
            field_dict["phoneNumberId"] = phone_number_id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if squad_id is not UNSET:
            field_dict["squadId"] = squad_id
        if call_id is not UNSET:
            field_dict["callId"] = call_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error import Error
        from ..models.log_request_body import LogRequestBody
        from ..models.log_request_headers import LogRequestHeaders
        from ..models.log_response_body import LogResponseBody

        d = dict(src_dict)
        time = d.pop("time")

        org_id = d.pop("orgId")

        type_ = LogType(d.pop("type"))

        webhook_type = d.pop("webhookType", UNSET)

        _resource = d.pop("resource", UNSET)
        resource: Union[Unset, LogResource]
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = LogResource(_resource)

        request_duration_seconds = d.pop("requestDurationSeconds", UNSET)

        request_started_at = d.pop("requestStartedAt", UNSET)

        request_finished_at = d.pop("requestFinishedAt", UNSET)

        _request_body = d.pop("requestBody", UNSET)
        request_body: Union[Unset, LogRequestBody]
        if isinstance(_request_body, Unset):
            request_body = UNSET
        else:
            request_body = LogRequestBody.from_dict(_request_body)

        _request_http_method = d.pop("requestHttpMethod", UNSET)
        request_http_method: Union[Unset, LogRequestHttpMethod]
        if isinstance(_request_http_method, Unset):
            request_http_method = UNSET
        else:
            request_http_method = LogRequestHttpMethod(_request_http_method)

        request_url = d.pop("requestUrl", UNSET)

        request_path = d.pop("requestPath", UNSET)

        request_query = d.pop("requestQuery", UNSET)

        response_http_code = d.pop("responseHttpCode", UNSET)

        request_ip_address = d.pop("requestIpAddress", UNSET)

        request_origin = d.pop("requestOrigin", UNSET)

        _response_body = d.pop("responseBody", UNSET)
        response_body: Union[Unset, LogResponseBody]
        if isinstance(_response_body, Unset):
            response_body = UNSET
        else:
            response_body = LogResponseBody.from_dict(_response_body)

        _request_headers = d.pop("requestHeaders", UNSET)
        request_headers: Union[Unset, LogRequestHeaders]
        if isinstance(_request_headers, Unset):
            request_headers = UNSET
        else:
            request_headers = LogRequestHeaders.from_dict(_request_headers)

        _error = d.pop("error", UNSET)
        error: Union[Unset, Error]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = Error.from_dict(_error)

        assistant_id = d.pop("assistantId", UNSET)

        phone_number_id = d.pop("phoneNumberId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        squad_id = d.pop("squadId", UNSET)

        call_id = d.pop("callId", UNSET)

        log = cls(
            time=time,
            org_id=org_id,
            type_=type_,
            webhook_type=webhook_type,
            resource=resource,
            request_duration_seconds=request_duration_seconds,
            request_started_at=request_started_at,
            request_finished_at=request_finished_at,
            request_body=request_body,
            request_http_method=request_http_method,
            request_url=request_url,
            request_path=request_path,
            request_query=request_query,
            response_http_code=response_http_code,
            request_ip_address=request_ip_address,
            request_origin=request_origin,
            response_body=response_body,
            request_headers=request_headers,
            error=error,
            assistant_id=assistant_id,
            phone_number_id=phone_number_id,
            customer_id=customer_id,
            squad_id=squad_id,
            call_id=call_id,
        )

        log.additional_properties = d
        return log

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
