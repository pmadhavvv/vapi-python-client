from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.test_suite_test_voice import TestSuiteTestVoice
from ...models.update_test_suite_test_voice_dto import UpdateTestSuiteTestVoiceDto
from ...types import Response


def _get_kwargs(
    test_suite_id: str,
    id: str,
    *,
    body: UpdateTestSuiteTestVoiceDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/test-suite/{test_suite_id}/test/{id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TestSuiteTestVoice]:
    if response.status_code == 200:
        response_200 = TestSuiteTestVoice.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TestSuiteTestVoice]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    test_suite_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTestSuiteTestVoiceDto,
) -> Response[TestSuiteTestVoice]:
    """Update Test

    Args:
        test_suite_id (str):
        id (str):
        body (UpdateTestSuiteTestVoiceDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestSuiteTestVoice]
    """

    kwargs = _get_kwargs(
        test_suite_id=test_suite_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    test_suite_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTestSuiteTestVoiceDto,
) -> Optional[TestSuiteTestVoice]:
    """Update Test

    Args:
        test_suite_id (str):
        id (str):
        body (UpdateTestSuiteTestVoiceDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestSuiteTestVoice
    """

    return sync_detailed(
        test_suite_id=test_suite_id,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    test_suite_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTestSuiteTestVoiceDto,
) -> Response[TestSuiteTestVoice]:
    """Update Test

    Args:
        test_suite_id (str):
        id (str):
        body (UpdateTestSuiteTestVoiceDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestSuiteTestVoice]
    """

    kwargs = _get_kwargs(
        test_suite_id=test_suite_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    test_suite_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTestSuiteTestVoiceDto,
) -> Optional[TestSuiteTestVoice]:
    """Update Test

    Args:
        test_suite_id (str):
        id (str):
        body (UpdateTestSuiteTestVoiceDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestSuiteTestVoice
    """

    return (
        await asyncio_detailed(
            test_suite_id=test_suite_id,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
