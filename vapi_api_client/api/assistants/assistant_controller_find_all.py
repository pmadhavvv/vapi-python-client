import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assistant import Assistant
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
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
        "url": "/assistant",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["Assistant"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Assistant.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["Assistant"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, float] = UNSET,
    created_at_gt: Union[Unset, datetime.datetime] = UNSET,
    created_at_lt: Union[Unset, datetime.datetime] = UNSET,
    created_at_ge: Union[Unset, datetime.datetime] = UNSET,
    created_at_le: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_ge: Union[Unset, datetime.datetime] = UNSET,
    updated_at_le: Union[Unset, datetime.datetime] = UNSET,
) -> Response[list["Assistant"]]:
    """List Assistants

    Args:
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
        Response[list['Assistant']]
    """

    kwargs = _get_kwargs(
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
    limit: Union[Unset, float] = UNSET,
    created_at_gt: Union[Unset, datetime.datetime] = UNSET,
    created_at_lt: Union[Unset, datetime.datetime] = UNSET,
    created_at_ge: Union[Unset, datetime.datetime] = UNSET,
    created_at_le: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_ge: Union[Unset, datetime.datetime] = UNSET,
    updated_at_le: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[list["Assistant"]]:
    """List Assistants

    Args:
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
        list['Assistant']
    """

    return sync_detailed(
        client=client,
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
    limit: Union[Unset, float] = UNSET,
    created_at_gt: Union[Unset, datetime.datetime] = UNSET,
    created_at_lt: Union[Unset, datetime.datetime] = UNSET,
    created_at_ge: Union[Unset, datetime.datetime] = UNSET,
    created_at_le: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_ge: Union[Unset, datetime.datetime] = UNSET,
    updated_at_le: Union[Unset, datetime.datetime] = UNSET,
) -> Response[list["Assistant"]]:
    """List Assistants

    Args:
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
        Response[list['Assistant']]
    """

    kwargs = _get_kwargs(
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
    limit: Union[Unset, float] = UNSET,
    created_at_gt: Union[Unset, datetime.datetime] = UNSET,
    created_at_lt: Union[Unset, datetime.datetime] = UNSET,
    created_at_ge: Union[Unset, datetime.datetime] = UNSET,
    created_at_le: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_ge: Union[Unset, datetime.datetime] = UNSET,
    updated_at_le: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[list["Assistant"]]:
    """List Assistants

    Args:
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
        list['Assistant']
    """

    return (
        await asyncio_detailed(
            client=client,
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
