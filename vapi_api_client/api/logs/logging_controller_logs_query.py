import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.logging_controller_logs_query_sort_order import LoggingControllerLogsQuerySortOrder
from ...models.logging_controller_logs_query_type import LoggingControllerLogsQueryType
from ...models.logs_paginated_response import LogsPaginatedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: Union[Unset, LoggingControllerLogsQueryType] = UNSET,
    webhook_type: Union[Unset, str] = UNSET,
    assistant_id: Union[Unset, str] = UNSET,
    phone_number_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    squad_id: Union[Unset, str] = UNSET,
    call_id: Union[Unset, str] = UNSET,
    page: Union[Unset, float] = UNSET,
    sort_order: Union[Unset, LoggingControllerLogsQuerySortOrder] = UNSET,
    limit: Union[Unset, float] = UNSET,
    created_at_gt: Union[Unset, datetime.datetime] = UNSET,
    created_at_lt: Union[Unset, datetime.datetime] = UNSET,
    created_at_ge: Union[Unset, datetime.datetime] = UNSET,
    created_at_le: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_ge: Union[Unset, datetime.datetime] = UNSET,
    updated_at_le: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["webhookType"] = webhook_type

    params["assistantId"] = assistant_id

    params["phoneNumberId"] = phone_number_id

    params["customerId"] = customer_id

    params["squadId"] = squad_id

    params["callId"] = call_id

    params["page"] = page

    json_sort_order: Union[Unset, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params["limit"] = limit

    json_created_at_gt: Union[Unset, str] = UNSET
    if not isinstance(created_at_gt, Unset):
        json_created_at_gt = created_at_gt.isoformat()
    params["createdAtGt"] = json_created_at_gt

    json_created_at_lt: Union[Unset, str] = UNSET
    if not isinstance(created_at_lt, Unset):
        json_created_at_lt = created_at_lt.isoformat()
    params["createdAtLt"] = json_created_at_lt

    json_created_at_ge: Union[Unset, str] = UNSET
    if not isinstance(created_at_ge, Unset):
        json_created_at_ge = created_at_ge.isoformat()
    params["createdAtGe"] = json_created_at_ge

    json_created_at_le: Union[Unset, str] = UNSET
    if not isinstance(created_at_le, Unset):
        json_created_at_le = created_at_le.isoformat()
    params["createdAtLe"] = json_created_at_le

    json_updated_at_gt: Union[Unset, str] = UNSET
    if not isinstance(updated_at_gt, Unset):
        json_updated_at_gt = updated_at_gt.isoformat()
    params["updatedAtGt"] = json_updated_at_gt

    json_updated_at_lt: Union[Unset, str] = UNSET
    if not isinstance(updated_at_lt, Unset):
        json_updated_at_lt = updated_at_lt.isoformat()
    params["updatedAtLt"] = json_updated_at_lt

    json_updated_at_ge: Union[Unset, str] = UNSET
    if not isinstance(updated_at_ge, Unset):
        json_updated_at_ge = updated_at_ge.isoformat()
    params["updatedAtGe"] = json_updated_at_ge

    json_updated_at_le: Union[Unset, str] = UNSET
    if not isinstance(updated_at_le, Unset):
        json_updated_at_le = updated_at_le.isoformat()
    params["updatedAtLe"] = json_updated_at_le

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[LogsPaginatedResponse]:
    if response.status_code == 200:
        response_200 = LogsPaginatedResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[LogsPaginatedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, LoggingControllerLogsQueryType] = UNSET,
    webhook_type: Union[Unset, str] = UNSET,
    assistant_id: Union[Unset, str] = UNSET,
    phone_number_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    squad_id: Union[Unset, str] = UNSET,
    call_id: Union[Unset, str] = UNSET,
    page: Union[Unset, float] = UNSET,
    sort_order: Union[Unset, LoggingControllerLogsQuerySortOrder] = UNSET,
    limit: Union[Unset, float] = UNSET,
    created_at_gt: Union[Unset, datetime.datetime] = UNSET,
    created_at_lt: Union[Unset, datetime.datetime] = UNSET,
    created_at_ge: Union[Unset, datetime.datetime] = UNSET,
    created_at_le: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_ge: Union[Unset, datetime.datetime] = UNSET,
    updated_at_le: Union[Unset, datetime.datetime] = UNSET,
) -> Response[LogsPaginatedResponse]:
    """Get Logs

    Args:
        type_ (Union[Unset, LoggingControllerLogsQueryType]):
        webhook_type (Union[Unset, str]):
        assistant_id (Union[Unset, str]):
        phone_number_id (Union[Unset, str]):
        customer_id (Union[Unset, str]):
        squad_id (Union[Unset, str]):
        call_id (Union[Unset, str]):
        page (Union[Unset, float]):
        sort_order (Union[Unset, LoggingControllerLogsQuerySortOrder]):
        limit (Union[Unset, float]):
        created_at_gt (Union[Unset, datetime.datetime]):
        created_at_lt (Union[Unset, datetime.datetime]):
        created_at_ge (Union[Unset, datetime.datetime]):
        created_at_le (Union[Unset, datetime.datetime]):
        updated_at_gt (Union[Unset, datetime.datetime]):
        updated_at_lt (Union[Unset, datetime.datetime]):
        updated_at_ge (Union[Unset, datetime.datetime]):
        updated_at_le (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogsPaginatedResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        webhook_type=webhook_type,
        assistant_id=assistant_id,
        phone_number_id=phone_number_id,
        customer_id=customer_id,
        squad_id=squad_id,
        call_id=call_id,
        page=page,
        sort_order=sort_order,
        limit=limit,
        created_at_gt=created_at_gt,
        created_at_lt=created_at_lt,
        created_at_ge=created_at_ge,
        created_at_le=created_at_le,
        updated_at_gt=updated_at_gt,
        updated_at_lt=updated_at_lt,
        updated_at_ge=updated_at_ge,
        updated_at_le=updated_at_le,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, LoggingControllerLogsQueryType] = UNSET,
    webhook_type: Union[Unset, str] = UNSET,
    assistant_id: Union[Unset, str] = UNSET,
    phone_number_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    squad_id: Union[Unset, str] = UNSET,
    call_id: Union[Unset, str] = UNSET,
    page: Union[Unset, float] = UNSET,
    sort_order: Union[Unset, LoggingControllerLogsQuerySortOrder] = UNSET,
    limit: Union[Unset, float] = UNSET,
    created_at_gt: Union[Unset, datetime.datetime] = UNSET,
    created_at_lt: Union[Unset, datetime.datetime] = UNSET,
    created_at_ge: Union[Unset, datetime.datetime] = UNSET,
    created_at_le: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_ge: Union[Unset, datetime.datetime] = UNSET,
    updated_at_le: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[LogsPaginatedResponse]:
    """Get Logs

    Args:
        type_ (Union[Unset, LoggingControllerLogsQueryType]):
        webhook_type (Union[Unset, str]):
        assistant_id (Union[Unset, str]):
        phone_number_id (Union[Unset, str]):
        customer_id (Union[Unset, str]):
        squad_id (Union[Unset, str]):
        call_id (Union[Unset, str]):
        page (Union[Unset, float]):
        sort_order (Union[Unset, LoggingControllerLogsQuerySortOrder]):
        limit (Union[Unset, float]):
        created_at_gt (Union[Unset, datetime.datetime]):
        created_at_lt (Union[Unset, datetime.datetime]):
        created_at_ge (Union[Unset, datetime.datetime]):
        created_at_le (Union[Unset, datetime.datetime]):
        updated_at_gt (Union[Unset, datetime.datetime]):
        updated_at_lt (Union[Unset, datetime.datetime]):
        updated_at_ge (Union[Unset, datetime.datetime]):
        updated_at_le (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogsPaginatedResponse
    """

    return sync_detailed(
        client=client,
        type_=type_,
        webhook_type=webhook_type,
        assistant_id=assistant_id,
        phone_number_id=phone_number_id,
        customer_id=customer_id,
        squad_id=squad_id,
        call_id=call_id,
        page=page,
        sort_order=sort_order,
        limit=limit,
        created_at_gt=created_at_gt,
        created_at_lt=created_at_lt,
        created_at_ge=created_at_ge,
        created_at_le=created_at_le,
        updated_at_gt=updated_at_gt,
        updated_at_lt=updated_at_lt,
        updated_at_ge=updated_at_ge,
        updated_at_le=updated_at_le,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, LoggingControllerLogsQueryType] = UNSET,
    webhook_type: Union[Unset, str] = UNSET,
    assistant_id: Union[Unset, str] = UNSET,
    phone_number_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    squad_id: Union[Unset, str] = UNSET,
    call_id: Union[Unset, str] = UNSET,
    page: Union[Unset, float] = UNSET,
    sort_order: Union[Unset, LoggingControllerLogsQuerySortOrder] = UNSET,
    limit: Union[Unset, float] = UNSET,
    created_at_gt: Union[Unset, datetime.datetime] = UNSET,
    created_at_lt: Union[Unset, datetime.datetime] = UNSET,
    created_at_ge: Union[Unset, datetime.datetime] = UNSET,
    created_at_le: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_ge: Union[Unset, datetime.datetime] = UNSET,
    updated_at_le: Union[Unset, datetime.datetime] = UNSET,
) -> Response[LogsPaginatedResponse]:
    """Get Logs

    Args:
        type_ (Union[Unset, LoggingControllerLogsQueryType]):
        webhook_type (Union[Unset, str]):
        assistant_id (Union[Unset, str]):
        phone_number_id (Union[Unset, str]):
        customer_id (Union[Unset, str]):
        squad_id (Union[Unset, str]):
        call_id (Union[Unset, str]):
        page (Union[Unset, float]):
        sort_order (Union[Unset, LoggingControllerLogsQuerySortOrder]):
        limit (Union[Unset, float]):
        created_at_gt (Union[Unset, datetime.datetime]):
        created_at_lt (Union[Unset, datetime.datetime]):
        created_at_ge (Union[Unset, datetime.datetime]):
        created_at_le (Union[Unset, datetime.datetime]):
        updated_at_gt (Union[Unset, datetime.datetime]):
        updated_at_lt (Union[Unset, datetime.datetime]):
        updated_at_ge (Union[Unset, datetime.datetime]):
        updated_at_le (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogsPaginatedResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        webhook_type=webhook_type,
        assistant_id=assistant_id,
        phone_number_id=phone_number_id,
        customer_id=customer_id,
        squad_id=squad_id,
        call_id=call_id,
        page=page,
        sort_order=sort_order,
        limit=limit,
        created_at_gt=created_at_gt,
        created_at_lt=created_at_lt,
        created_at_ge=created_at_ge,
        created_at_le=created_at_le,
        updated_at_gt=updated_at_gt,
        updated_at_lt=updated_at_lt,
        updated_at_ge=updated_at_ge,
        updated_at_le=updated_at_le,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, LoggingControllerLogsQueryType] = UNSET,
    webhook_type: Union[Unset, str] = UNSET,
    assistant_id: Union[Unset, str] = UNSET,
    phone_number_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    squad_id: Union[Unset, str] = UNSET,
    call_id: Union[Unset, str] = UNSET,
    page: Union[Unset, float] = UNSET,
    sort_order: Union[Unset, LoggingControllerLogsQuerySortOrder] = UNSET,
    limit: Union[Unset, float] = UNSET,
    created_at_gt: Union[Unset, datetime.datetime] = UNSET,
    created_at_lt: Union[Unset, datetime.datetime] = UNSET,
    created_at_ge: Union[Unset, datetime.datetime] = UNSET,
    created_at_le: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_ge: Union[Unset, datetime.datetime] = UNSET,
    updated_at_le: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[LogsPaginatedResponse]:
    """Get Logs

    Args:
        type_ (Union[Unset, LoggingControllerLogsQueryType]):
        webhook_type (Union[Unset, str]):
        assistant_id (Union[Unset, str]):
        phone_number_id (Union[Unset, str]):
        customer_id (Union[Unset, str]):
        squad_id (Union[Unset, str]):
        call_id (Union[Unset, str]):
        page (Union[Unset, float]):
        sort_order (Union[Unset, LoggingControllerLogsQuerySortOrder]):
        limit (Union[Unset, float]):
        created_at_gt (Union[Unset, datetime.datetime]):
        created_at_lt (Union[Unset, datetime.datetime]):
        created_at_ge (Union[Unset, datetime.datetime]):
        created_at_le (Union[Unset, datetime.datetime]):
        updated_at_gt (Union[Unset, datetime.datetime]):
        updated_at_lt (Union[Unset, datetime.datetime]):
        updated_at_ge (Union[Unset, datetime.datetime]):
        updated_at_le (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogsPaginatedResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            webhook_type=webhook_type,
            assistant_id=assistant_id,
            phone_number_id=phone_number_id,
            customer_id=customer_id,
            squad_id=squad_id,
            call_id=call_id,
            page=page,
            sort_order=sort_order,
            limit=limit,
            created_at_gt=created_at_gt,
            created_at_lt=created_at_lt,
            created_at_ge=created_at_ge,
            created_at_le=created_at_le,
            updated_at_gt=updated_at_gt,
            updated_at_lt=updated_at_lt,
            updated_at_ge=updated_at_ge,
            updated_at_le=updated_at_le,
        )
    ).parsed
