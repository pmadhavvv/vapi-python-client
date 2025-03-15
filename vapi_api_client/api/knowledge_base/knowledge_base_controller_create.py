from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_custom_knowledge_base_dto import CreateCustomKnowledgeBaseDTO
from ...models.create_trieve_knowledge_base_dto import CreateTrieveKnowledgeBaseDTO
from ...models.custom_knowledge_base import CustomKnowledgeBase
from ...models.trieve_knowledge_base import TrieveKnowledgeBase
from ...types import Response


def _get_kwargs(
    *,
    body: Union["CreateCustomKnowledgeBaseDTO", "CreateTrieveKnowledgeBaseDTO"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/knowledge-base",
    }

    _body: dict[str, Any]
    if isinstance(body, CreateTrieveKnowledgeBaseDTO):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["CustomKnowledgeBase", "TrieveKnowledgeBase"]]:
    if response.status_code == 201:

        def _parse_response_201(data: object) -> Union["CustomKnowledgeBase", "TrieveKnowledgeBase"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0 = TrieveKnowledgeBase.from_dict(data)

                return response_201_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_201_type_1 = CustomKnowledgeBase.from_dict(data)

            return response_201_type_1

        response_201 = _parse_response_201(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union["CustomKnowledgeBase", "TrieveKnowledgeBase"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union["CreateCustomKnowledgeBaseDTO", "CreateTrieveKnowledgeBaseDTO"],
) -> Response[Union["CustomKnowledgeBase", "TrieveKnowledgeBase"]]:
    """Create Knowledge Base

    Args:
        body (Union['CreateCustomKnowledgeBaseDTO', 'CreateTrieveKnowledgeBaseDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['CustomKnowledgeBase', 'TrieveKnowledgeBase']]
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
    body: Union["CreateCustomKnowledgeBaseDTO", "CreateTrieveKnowledgeBaseDTO"],
) -> Optional[Union["CustomKnowledgeBase", "TrieveKnowledgeBase"]]:
    """Create Knowledge Base

    Args:
        body (Union['CreateCustomKnowledgeBaseDTO', 'CreateTrieveKnowledgeBaseDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['CustomKnowledgeBase', 'TrieveKnowledgeBase']
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union["CreateCustomKnowledgeBaseDTO", "CreateTrieveKnowledgeBaseDTO"],
) -> Response[Union["CustomKnowledgeBase", "TrieveKnowledgeBase"]]:
    """Create Knowledge Base

    Args:
        body (Union['CreateCustomKnowledgeBaseDTO', 'CreateTrieveKnowledgeBaseDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['CustomKnowledgeBase', 'TrieveKnowledgeBase']]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union["CreateCustomKnowledgeBaseDTO", "CreateTrieveKnowledgeBaseDTO"],
) -> Optional[Union["CustomKnowledgeBase", "TrieveKnowledgeBase"]]:
    """Create Knowledge Base

    Args:
        body (Union['CreateCustomKnowledgeBaseDTO', 'CreateTrieveKnowledgeBaseDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['CustomKnowledgeBase', 'TrieveKnowledgeBase']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
