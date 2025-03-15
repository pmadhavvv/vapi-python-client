import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.test_suite_controller_find_all_paginated_sort_order import TestSuiteControllerFindAllPaginatedSortOrder
from ...models.test_suites_paginated_response import TestSuitesPaginatedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, float] = UNSET,
    sort_order: Union[Unset, TestSuiteControllerFindAllPaginatedSortOrder] = UNSET,
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
        "url": "/test-suite",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TestSuitesPaginatedResponse]:
    if response.status_code == 200:
        response_200 = TestSuitesPaginatedResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TestSuitesPaginatedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, float] = UNSET,
    sort_order: Union[Unset, TestSuiteControllerFindAllPaginatedSortOrder] = UNSET,
    limit: Union[Unset, float] = UNSET,
    created_at_gt: Union[Unset, datetime.datetime] = UNSET,
    created_at_lt: Union[Unset, datetime.datetime] = UNSET,
    created_at_ge: Union[Unset, datetime.datetime] = UNSET,
    created_at_le: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_ge: Union[Unset, datetime.datetime] = UNSET,
    updated_at_le: Union[Unset, datetime.datetime] = UNSET,
) -> Response[TestSuitesPaginatedResponse]:
    """List Test Suites

    Args:
        page (Union[Unset, float]):
        sort_order (Union[Unset, TestSuiteControllerFindAllPaginatedSortOrder]):
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
        Response[TestSuitesPaginatedResponse]
    """

    kwargs = _get_kwargs(
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
    page: Union[Unset, float] = UNSET,
    sort_order: Union[Unset, TestSuiteControllerFindAllPaginatedSortOrder] = UNSET,
    limit: Union[Unset, float] = UNSET,
    created_at_gt: Union[Unset, datetime.datetime] = UNSET,
    created_at_lt: Union[Unset, datetime.datetime] = UNSET,
    created_at_ge: Union[Unset, datetime.datetime] = UNSET,
    created_at_le: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_ge: Union[Unset, datetime.datetime] = UNSET,
    updated_at_le: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[TestSuitesPaginatedResponse]:
    """List Test Suites

    Args:
        page (Union[Unset, float]):
        sort_order (Union[Unset, TestSuiteControllerFindAllPaginatedSortOrder]):
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
        TestSuitesPaginatedResponse
    """

    return sync_detailed(
        client=client,
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
    page: Union[Unset, float] = UNSET,
    sort_order: Union[Unset, TestSuiteControllerFindAllPaginatedSortOrder] = UNSET,
    limit: Union[Unset, float] = UNSET,
    created_at_gt: Union[Unset, datetime.datetime] = UNSET,
    created_at_lt: Union[Unset, datetime.datetime] = UNSET,
    created_at_ge: Union[Unset, datetime.datetime] = UNSET,
    created_at_le: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_ge: Union[Unset, datetime.datetime] = UNSET,
    updated_at_le: Union[Unset, datetime.datetime] = UNSET,
) -> Response[TestSuitesPaginatedResponse]:
    """List Test Suites

    Args:
        page (Union[Unset, float]):
        sort_order (Union[Unset, TestSuiteControllerFindAllPaginatedSortOrder]):
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
        Response[TestSuitesPaginatedResponse]
    """

    kwargs = _get_kwargs(
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
    page: Union[Unset, float] = UNSET,
    sort_order: Union[Unset, TestSuiteControllerFindAllPaginatedSortOrder] = UNSET,
    limit: Union[Unset, float] = UNSET,
    created_at_gt: Union[Unset, datetime.datetime] = UNSET,
    created_at_lt: Union[Unset, datetime.datetime] = UNSET,
    created_at_ge: Union[Unset, datetime.datetime] = UNSET,
    created_at_le: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_at_ge: Union[Unset, datetime.datetime] = UNSET,
    updated_at_le: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[TestSuitesPaginatedResponse]:
    """List Test Suites

    Args:
        page (Union[Unset, float]):
        sort_order (Union[Unset, TestSuiteControllerFindAllPaginatedSortOrder]):
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
        TestSuitesPaginatedResponse
    """

    return (
        await asyncio_detailed(
            client=client,
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
