from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_query_dto import AnalyticsQueryDTO
from ...models.analytics_query_result import AnalyticsQueryResult
from ...types import Response


def _get_kwargs(
    *,
    body: AnalyticsQueryDTO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/analytics",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["AnalyticsQueryResult"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AnalyticsQueryResult.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, list["AnalyticsQueryResult"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AnalyticsQueryDTO,
) -> Response[Union[Any, list["AnalyticsQueryResult"]]]:
    """Create Analytics Queries

    Args:
        body (AnalyticsQueryDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['AnalyticsQueryResult']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: AnalyticsQueryDTO,
) -> Optional[Union[Any, list["AnalyticsQueryResult"]]]:
    """Create Analytics Queries

    Args:
        body (AnalyticsQueryDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['AnalyticsQueryResult']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AnalyticsQueryDTO,
) -> Response[Union[Any, list["AnalyticsQueryResult"]]]:
    """Create Analytics Queries

    Args:
        body (AnalyticsQueryDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['AnalyticsQueryResult']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AnalyticsQueryDTO,
) -> Optional[Union[Any, list["AnalyticsQueryResult"]]]:
    """Create Analytics Queries

    Args:
        body (AnalyticsQueryDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['AnalyticsQueryResult']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
