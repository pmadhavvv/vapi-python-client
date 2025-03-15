from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.logging_controller_logs_delete_query_type import LoggingControllerLogsDeleteQueryType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: Union[Unset, LoggingControllerLogsDeleteQueryType] = UNSET,
    assistant_id: Union[Unset, str] = UNSET,
    phone_number_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    squad_id: Union[Unset, str] = UNSET,
    call_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["assistantId"] = assistant_id

    params["phoneNumberId"] = phone_number_id

    params["customerId"] = customer_id

    params["squadId"] = squad_id

    params["callId"] = call_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, LoggingControllerLogsDeleteQueryType] = UNSET,
    assistant_id: Union[Unset, str] = UNSET,
    phone_number_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    squad_id: Union[Unset, str] = UNSET,
    call_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Delete Logs

    Args:
        type_ (Union[Unset, LoggingControllerLogsDeleteQueryType]):
        assistant_id (Union[Unset, str]):
        phone_number_id (Union[Unset, str]):
        customer_id (Union[Unset, str]):
        squad_id (Union[Unset, str]):
        call_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        type_=type_,
        assistant_id=assistant_id,
        phone_number_id=phone_number_id,
        customer_id=customer_id,
        squad_id=squad_id,
        call_id=call_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, LoggingControllerLogsDeleteQueryType] = UNSET,
    assistant_id: Union[Unset, str] = UNSET,
    phone_number_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    squad_id: Union[Unset, str] = UNSET,
    call_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Delete Logs

    Args:
        type_ (Union[Unset, LoggingControllerLogsDeleteQueryType]):
        assistant_id (Union[Unset, str]):
        phone_number_id (Union[Unset, str]):
        customer_id (Union[Unset, str]):
        squad_id (Union[Unset, str]):
        call_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        type_=type_,
        assistant_id=assistant_id,
        phone_number_id=phone_number_id,
        customer_id=customer_id,
        squad_id=squad_id,
        call_id=call_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
