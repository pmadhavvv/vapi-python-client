from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_knowledge_base import CustomKnowledgeBase
from ...models.trieve_knowledge_base import TrieveKnowledgeBase
from ...models.update_custom_knowledge_base_dto import UpdateCustomKnowledgeBaseDTO
from ...models.update_trieve_knowledge_base_dto import UpdateTrieveKnowledgeBaseDTO
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: Union["UpdateCustomKnowledgeBaseDTO", "UpdateTrieveKnowledgeBaseDTO"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/knowledge-base/{id}",
    }

    _body: dict[str, Any]
    if isinstance(body, UpdateTrieveKnowledgeBaseDTO):
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
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["CustomKnowledgeBase", "TrieveKnowledgeBase"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = TrieveKnowledgeBase.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = CustomKnowledgeBase.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
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
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union["UpdateCustomKnowledgeBaseDTO", "UpdateTrieveKnowledgeBaseDTO"],
) -> Response[Union["CustomKnowledgeBase", "TrieveKnowledgeBase"]]:
    """Update Knowledge Base

    Args:
        id (str):
        body (Union['UpdateCustomKnowledgeBaseDTO', 'UpdateTrieveKnowledgeBaseDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['CustomKnowledgeBase', 'TrieveKnowledgeBase']]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union["UpdateCustomKnowledgeBaseDTO", "UpdateTrieveKnowledgeBaseDTO"],
) -> Optional[Union["CustomKnowledgeBase", "TrieveKnowledgeBase"]]:
    """Update Knowledge Base

    Args:
        id (str):
        body (Union['UpdateCustomKnowledgeBaseDTO', 'UpdateTrieveKnowledgeBaseDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['CustomKnowledgeBase', 'TrieveKnowledgeBase']
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union["UpdateCustomKnowledgeBaseDTO", "UpdateTrieveKnowledgeBaseDTO"],
) -> Response[Union["CustomKnowledgeBase", "TrieveKnowledgeBase"]]:
    """Update Knowledge Base

    Args:
        id (str):
        body (Union['UpdateCustomKnowledgeBaseDTO', 'UpdateTrieveKnowledgeBaseDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['CustomKnowledgeBase', 'TrieveKnowledgeBase']]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union["UpdateCustomKnowledgeBaseDTO", "UpdateTrieveKnowledgeBaseDTO"],
) -> Optional[Union["CustomKnowledgeBase", "TrieveKnowledgeBase"]]:
    """Update Knowledge Base

    Args:
        id (str):
        body (Union['UpdateCustomKnowledgeBaseDTO', 'UpdateTrieveKnowledgeBaseDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['CustomKnowledgeBase', 'TrieveKnowledgeBase']
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
