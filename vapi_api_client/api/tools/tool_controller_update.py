from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bash_tool import BashTool
from ...models.computer_tool import ComputerTool
from ...models.dtmf_tool import DtmfTool
from ...models.end_call_tool import EndCallTool
from ...models.function_tool import FunctionTool
from ...models.ghl_tool import GhlTool
from ...models.make_tool import MakeTool
from ...models.output_tool import OutputTool
from ...models.query_tool import QueryTool
from ...models.text_editor_tool import TextEditorTool
from ...models.transfer_call_tool import TransferCallTool
from ...models.update_bash_tool_dto import UpdateBashToolDTO
from ...models.update_computer_tool_dto import UpdateComputerToolDTO
from ...models.update_dtmf_tool_dto import UpdateDtmfToolDTO
from ...models.update_end_call_tool_dto import UpdateEndCallToolDTO
from ...models.update_function_tool_dto import UpdateFunctionToolDTO
from ...models.update_ghl_tool_dto import UpdateGhlToolDTO
from ...models.update_make_tool_dto import UpdateMakeToolDTO
from ...models.update_output_tool_dto import UpdateOutputToolDTO
from ...models.update_query_tool_dto import UpdateQueryToolDTO
from ...models.update_text_editor_tool_dto import UpdateTextEditorToolDTO
from ...models.update_transfer_call_tool_dto import UpdateTransferCallToolDTO
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: Union[
        "UpdateBashToolDTO",
        "UpdateComputerToolDTO",
        "UpdateDtmfToolDTO",
        "UpdateEndCallToolDTO",
        "UpdateFunctionToolDTO",
        "UpdateGhlToolDTO",
        "UpdateMakeToolDTO",
        "UpdateOutputToolDTO",
        "UpdateQueryToolDTO",
        "UpdateTextEditorToolDTO",
        "UpdateTransferCallToolDTO",
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/tool/{id}",
    }

    _body: dict[str, Any]
    if isinstance(body, UpdateDtmfToolDTO):
        _body = body.to_dict()
    elif isinstance(body, UpdateEndCallToolDTO):
        _body = body.to_dict()
    elif isinstance(body, UpdateFunctionToolDTO):
        _body = body.to_dict()
    elif isinstance(body, UpdateGhlToolDTO):
        _body = body.to_dict()
    elif isinstance(body, UpdateMakeToolDTO):
        _body = body.to_dict()
    elif isinstance(body, UpdateTransferCallToolDTO):
        _body = body.to_dict()
    elif isinstance(body, UpdateOutputToolDTO):
        _body = body.to_dict()
    elif isinstance(body, UpdateBashToolDTO):
        _body = body.to_dict()
    elif isinstance(body, UpdateComputerToolDTO):
        _body = body.to_dict()
    elif isinstance(body, UpdateTextEditorToolDTO):
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
    if response.status_code == 200:

        def _parse_response_200(
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
                response_200_type_0 = DtmfTool.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = EndCallTool.from_dict(data)

                return response_200_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = FunctionTool.from_dict(data)

                return response_200_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3 = GhlTool.from_dict(data)

                return response_200_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_4 = MakeTool.from_dict(data)

                return response_200_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_5 = TransferCallTool.from_dict(data)

                return response_200_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_6 = OutputTool.from_dict(data)

                return response_200_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_7 = BashTool.from_dict(data)

                return response_200_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_8 = ComputerTool.from_dict(data)

                return response_200_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_9 = TextEditorTool.from_dict(data)

                return response_200_type_9
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_10 = QueryTool.from_dict(data)

            return response_200_type_10

        response_200 = _parse_response_200(response.json())

        return response_200
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
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        "UpdateBashToolDTO",
        "UpdateComputerToolDTO",
        "UpdateDtmfToolDTO",
        "UpdateEndCallToolDTO",
        "UpdateFunctionToolDTO",
        "UpdateGhlToolDTO",
        "UpdateMakeToolDTO",
        "UpdateOutputToolDTO",
        "UpdateQueryToolDTO",
        "UpdateTextEditorToolDTO",
        "UpdateTransferCallToolDTO",
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
    """Update Tool

    Args:
        id (str):
        body (Union['UpdateBashToolDTO', 'UpdateComputerToolDTO', 'UpdateDtmfToolDTO',
            'UpdateEndCallToolDTO', 'UpdateFunctionToolDTO', 'UpdateGhlToolDTO', 'UpdateMakeToolDTO',
            'UpdateOutputToolDTO', 'UpdateQueryToolDTO', 'UpdateTextEditorToolDTO',
            'UpdateTransferCallToolDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['BashTool', 'ComputerTool', 'DtmfTool', 'EndCallTool', 'FunctionTool', 'GhlTool', 'MakeTool', 'OutputTool', 'QueryTool', 'TextEditorTool', 'TransferCallTool']]
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
    body: Union[
        "UpdateBashToolDTO",
        "UpdateComputerToolDTO",
        "UpdateDtmfToolDTO",
        "UpdateEndCallToolDTO",
        "UpdateFunctionToolDTO",
        "UpdateGhlToolDTO",
        "UpdateMakeToolDTO",
        "UpdateOutputToolDTO",
        "UpdateQueryToolDTO",
        "UpdateTextEditorToolDTO",
        "UpdateTransferCallToolDTO",
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
    """Update Tool

    Args:
        id (str):
        body (Union['UpdateBashToolDTO', 'UpdateComputerToolDTO', 'UpdateDtmfToolDTO',
            'UpdateEndCallToolDTO', 'UpdateFunctionToolDTO', 'UpdateGhlToolDTO', 'UpdateMakeToolDTO',
            'UpdateOutputToolDTO', 'UpdateQueryToolDTO', 'UpdateTextEditorToolDTO',
            'UpdateTransferCallToolDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['BashTool', 'ComputerTool', 'DtmfTool', 'EndCallTool', 'FunctionTool', 'GhlTool', 'MakeTool', 'OutputTool', 'QueryTool', 'TextEditorTool', 'TransferCallTool']
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
    body: Union[
        "UpdateBashToolDTO",
        "UpdateComputerToolDTO",
        "UpdateDtmfToolDTO",
        "UpdateEndCallToolDTO",
        "UpdateFunctionToolDTO",
        "UpdateGhlToolDTO",
        "UpdateMakeToolDTO",
        "UpdateOutputToolDTO",
        "UpdateQueryToolDTO",
        "UpdateTextEditorToolDTO",
        "UpdateTransferCallToolDTO",
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
    """Update Tool

    Args:
        id (str):
        body (Union['UpdateBashToolDTO', 'UpdateComputerToolDTO', 'UpdateDtmfToolDTO',
            'UpdateEndCallToolDTO', 'UpdateFunctionToolDTO', 'UpdateGhlToolDTO', 'UpdateMakeToolDTO',
            'UpdateOutputToolDTO', 'UpdateQueryToolDTO', 'UpdateTextEditorToolDTO',
            'UpdateTransferCallToolDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['BashTool', 'ComputerTool', 'DtmfTool', 'EndCallTool', 'FunctionTool', 'GhlTool', 'MakeTool', 'OutputTool', 'QueryTool', 'TextEditorTool', 'TransferCallTool']]
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
    body: Union[
        "UpdateBashToolDTO",
        "UpdateComputerToolDTO",
        "UpdateDtmfToolDTO",
        "UpdateEndCallToolDTO",
        "UpdateFunctionToolDTO",
        "UpdateGhlToolDTO",
        "UpdateMakeToolDTO",
        "UpdateOutputToolDTO",
        "UpdateQueryToolDTO",
        "UpdateTextEditorToolDTO",
        "UpdateTransferCallToolDTO",
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
    """Update Tool

    Args:
        id (str):
        body (Union['UpdateBashToolDTO', 'UpdateComputerToolDTO', 'UpdateDtmfToolDTO',
            'UpdateEndCallToolDTO', 'UpdateFunctionToolDTO', 'UpdateGhlToolDTO', 'UpdateMakeToolDTO',
            'UpdateOutputToolDTO', 'UpdateQueryToolDTO', 'UpdateTextEditorToolDTO',
            'UpdateTransferCallToolDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['BashTool', 'ComputerTool', 'DtmfTool', 'EndCallTool', 'FunctionTool', 'GhlTool', 'MakeTool', 'OutputTool', 'QueryTool', 'TextEditorTool', 'TransferCallTool']
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
