from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bash_tool import BashTool
from ...models.computer_tool import ComputerTool
from ...models.create_bash_tool_dto import CreateBashToolDTO
from ...models.create_computer_tool_dto import CreateComputerToolDTO
from ...models.create_dtmf_tool_dto import CreateDtmfToolDTO
from ...models.create_end_call_tool_dto import CreateEndCallToolDTO
from ...models.create_function_tool_dto import CreateFunctionToolDTO
from ...models.create_ghl_tool_dto import CreateGhlToolDTO
from ...models.create_make_tool_dto import CreateMakeToolDTO
from ...models.create_output_tool_dto import CreateOutputToolDTO
from ...models.create_query_tool_dto import CreateQueryToolDTO
from ...models.create_text_editor_tool_dto import CreateTextEditorToolDTO
from ...models.create_transfer_call_tool_dto import CreateTransferCallToolDTO
from ...models.dtmf_tool import DtmfTool
from ...models.end_call_tool import EndCallTool
from ...models.function_tool import FunctionTool
from ...models.ghl_tool import GhlTool
from ...models.make_tool import MakeTool
from ...models.output_tool import OutputTool
from ...models.query_tool import QueryTool
from ...models.text_editor_tool import TextEditorTool
from ...models.transfer_call_tool import TransferCallTool
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        "CreateBashToolDTO",
        "CreateComputerToolDTO",
        "CreateDtmfToolDTO",
        "CreateEndCallToolDTO",
        "CreateFunctionToolDTO",
        "CreateGhlToolDTO",
        "CreateMakeToolDTO",
        "CreateOutputToolDTO",
        "CreateQueryToolDTO",
        "CreateTextEditorToolDTO",
        "CreateTransferCallToolDTO",
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tool",
    }

    _body: dict[str, Any]
    if isinstance(body, CreateDtmfToolDTO):
        _body = body.to_dict()
    elif isinstance(body, CreateEndCallToolDTO):
        _body = body.to_dict()
    elif isinstance(body, CreateFunctionToolDTO):
        _body = body.to_dict()
    elif isinstance(body, CreateGhlToolDTO):
        _body = body.to_dict()
    elif isinstance(body, CreateMakeToolDTO):
        _body = body.to_dict()
    elif isinstance(body, CreateTransferCallToolDTO):
        _body = body.to_dict()
    elif isinstance(body, CreateOutputToolDTO):
        _body = body.to_dict()
    elif isinstance(body, CreateBashToolDTO):
        _body = body.to_dict()
    elif isinstance(body, CreateComputerToolDTO):
        _body = body.to_dict()
    elif isinstance(body, CreateTextEditorToolDTO):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        "BashTool",
        "ComputerTool",
        "DtmfTool",
        "EndCallTool",
        "FunctionTool",
        "GhlTool",
        "MakeTool",
        "OutputTool",
        "QueryTool",
        "TextEditorTool",
        "TransferCallTool",
    ]
]:
    if response.status_code == 201:

        def _parse_response_201(
            data: object,
        ) -> Union[
            "BashTool",
            "ComputerTool",
            "DtmfTool",
            "EndCallTool",
            "FunctionTool",
            "GhlTool",
            "MakeTool",
            "OutputTool",
            "QueryTool",
            "TextEditorTool",
            "TransferCallTool",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0 = DtmfTool.from_dict(data)

                return response_201_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_1 = EndCallTool.from_dict(data)

                return response_201_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_2 = FunctionTool.from_dict(data)

                return response_201_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_3 = GhlTool.from_dict(data)

                return response_201_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_4 = MakeTool.from_dict(data)

                return response_201_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_5 = TransferCallTool.from_dict(data)

                return response_201_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_6 = OutputTool.from_dict(data)

                return response_201_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_7 = BashTool.from_dict(data)

                return response_201_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_8 = ComputerTool.from_dict(data)

                return response_201_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_9 = TextEditorTool.from_dict(data)

                return response_201_type_9
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_201_type_10 = QueryTool.from_dict(data)

            return response_201_type_10

        response_201 = _parse_response_201(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        "BashTool",
        "ComputerTool",
        "DtmfTool",
        "EndCallTool",
        "FunctionTool",
        "GhlTool",
        "MakeTool",
        "OutputTool",
        "QueryTool",
        "TextEditorTool",
        "TransferCallTool",
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        "CreateBashToolDTO",
        "CreateComputerToolDTO",
        "CreateDtmfToolDTO",
        "CreateEndCallToolDTO",
        "CreateFunctionToolDTO",
        "CreateGhlToolDTO",
        "CreateMakeToolDTO",
        "CreateOutputToolDTO",
        "CreateQueryToolDTO",
        "CreateTextEditorToolDTO",
        "CreateTransferCallToolDTO",
    ],
) -> Response[
    Union[
        "BashTool",
        "ComputerTool",
        "DtmfTool",
        "EndCallTool",
        "FunctionTool",
        "GhlTool",
        "MakeTool",
        "OutputTool",
        "QueryTool",
        "TextEditorTool",
        "TransferCallTool",
    ]
]:
    """Create Tool

    Args:
        body (Union['CreateBashToolDTO', 'CreateComputerToolDTO', 'CreateDtmfToolDTO',
            'CreateEndCallToolDTO', 'CreateFunctionToolDTO', 'CreateGhlToolDTO', 'CreateMakeToolDTO',
            'CreateOutputToolDTO', 'CreateQueryToolDTO', 'CreateTextEditorToolDTO',
            'CreateTransferCallToolDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['BashTool', 'ComputerTool', 'DtmfTool', 'EndCallTool', 'FunctionTool', 'GhlTool', 'MakeTool', 'OutputTool', 'QueryTool', 'TextEditorTool', 'TransferCallTool']]
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
    body: Union[
        "CreateBashToolDTO",
        "CreateComputerToolDTO",
        "CreateDtmfToolDTO",
        "CreateEndCallToolDTO",
        "CreateFunctionToolDTO",
        "CreateGhlToolDTO",
        "CreateMakeToolDTO",
        "CreateOutputToolDTO",
        "CreateQueryToolDTO",
        "CreateTextEditorToolDTO",
        "CreateTransferCallToolDTO",
    ],
) -> Optional[
    Union[
        "BashTool",
        "ComputerTool",
        "DtmfTool",
        "EndCallTool",
        "FunctionTool",
        "GhlTool",
        "MakeTool",
        "OutputTool",
        "QueryTool",
        "TextEditorTool",
        "TransferCallTool",
    ]
]:
    """Create Tool

    Args:
        body (Union['CreateBashToolDTO', 'CreateComputerToolDTO', 'CreateDtmfToolDTO',
            'CreateEndCallToolDTO', 'CreateFunctionToolDTO', 'CreateGhlToolDTO', 'CreateMakeToolDTO',
            'CreateOutputToolDTO', 'CreateQueryToolDTO', 'CreateTextEditorToolDTO',
            'CreateTransferCallToolDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['BashTool', 'ComputerTool', 'DtmfTool', 'EndCallTool', 'FunctionTool', 'GhlTool', 'MakeTool', 'OutputTool', 'QueryTool', 'TextEditorTool', 'TransferCallTool']
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        "CreateBashToolDTO",
        "CreateComputerToolDTO",
        "CreateDtmfToolDTO",
        "CreateEndCallToolDTO",
        "CreateFunctionToolDTO",
        "CreateGhlToolDTO",
        "CreateMakeToolDTO",
        "CreateOutputToolDTO",
        "CreateQueryToolDTO",
        "CreateTextEditorToolDTO",
        "CreateTransferCallToolDTO",
    ],
) -> Response[
    Union[
        "BashTool",
        "ComputerTool",
        "DtmfTool",
        "EndCallTool",
        "FunctionTool",
        "GhlTool",
        "MakeTool",
        "OutputTool",
        "QueryTool",
        "TextEditorTool",
        "TransferCallTool",
    ]
]:
    """Create Tool

    Args:
        body (Union['CreateBashToolDTO', 'CreateComputerToolDTO', 'CreateDtmfToolDTO',
            'CreateEndCallToolDTO', 'CreateFunctionToolDTO', 'CreateGhlToolDTO', 'CreateMakeToolDTO',
            'CreateOutputToolDTO', 'CreateQueryToolDTO', 'CreateTextEditorToolDTO',
            'CreateTransferCallToolDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['BashTool', 'ComputerTool', 'DtmfTool', 'EndCallTool', 'FunctionTool', 'GhlTool', 'MakeTool', 'OutputTool', 'QueryTool', 'TextEditorTool', 'TransferCallTool']]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        "CreateBashToolDTO",
        "CreateComputerToolDTO",
        "CreateDtmfToolDTO",
        "CreateEndCallToolDTO",
        "CreateFunctionToolDTO",
        "CreateGhlToolDTO",
        "CreateMakeToolDTO",
        "CreateOutputToolDTO",
        "CreateQueryToolDTO",
        "CreateTextEditorToolDTO",
        "CreateTransferCallToolDTO",
    ],
) -> Optional[
    Union[
        "BashTool",
        "ComputerTool",
        "DtmfTool",
        "EndCallTool",
        "FunctionTool",
        "GhlTool",
        "MakeTool",
        "OutputTool",
        "QueryTool",
        "TextEditorTool",
        "TransferCallTool",
    ]
]:
    """Create Tool

    Args:
        body (Union['CreateBashToolDTO', 'CreateComputerToolDTO', 'CreateDtmfToolDTO',
            'CreateEndCallToolDTO', 'CreateFunctionToolDTO', 'CreateGhlToolDTO', 'CreateMakeToolDTO',
            'CreateOutputToolDTO', 'CreateQueryToolDTO', 'CreateTextEditorToolDTO',
            'CreateTransferCallToolDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['BashTool', 'ComputerTool', 'DtmfTool', 'EndCallTool', 'FunctionTool', 'GhlTool', 'MakeTool', 'OutputTool', 'QueryTool', 'TextEditorTool', 'TransferCallTool']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
