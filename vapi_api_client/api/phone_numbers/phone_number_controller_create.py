from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.byo_phone_number import ByoPhoneNumber
from ...models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
from ...models.create_telnyx_phone_number_dto import CreateTelnyxPhoneNumberDTO
from ...models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
from ...models.create_vapi_phone_number_dto import CreateVapiPhoneNumberDTO
from ...models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO
from ...models.telnyx_phone_number import TelnyxPhoneNumber
from ...models.twilio_phone_number import TwilioPhoneNumber
from ...models.vapi_phone_number import VapiPhoneNumber
from ...models.vonage_phone_number import VonagePhoneNumber
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        "CreateByoPhoneNumberDTO",
        "CreateTelnyxPhoneNumberDTO",
        "CreateTwilioPhoneNumberDTO",
        "CreateVapiPhoneNumberDTO",
        "CreateVonagePhoneNumberDTO",
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/phone-number",
    }

    _body: dict[str, Any]
    if isinstance(body, CreateByoPhoneNumberDTO):
        _body = body.to_dict()
    elif isinstance(body, CreateTwilioPhoneNumberDTO):
        _body = body.to_dict()
    elif isinstance(body, CreateVonagePhoneNumberDTO):
        _body = body.to_dict()
    elif isinstance(body, CreateVapiPhoneNumberDTO):
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
    Union["ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"]
]:
    if response.status_code == 201:

        def _parse_response_201(
            data: object,
        ) -> Union["ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0 = ByoPhoneNumber.from_dict(data)

                return response_201_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_1 = TwilioPhoneNumber.from_dict(data)

                return response_201_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_2 = VonagePhoneNumber.from_dict(data)

                return response_201_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_3 = VapiPhoneNumber.from_dict(data)

                return response_201_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_201_type_4 = TelnyxPhoneNumber.from_dict(data)

            return response_201_type_4

        response_201 = _parse_response_201(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union["ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"]
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
        "CreateByoPhoneNumberDTO",
        "CreateTelnyxPhoneNumberDTO",
        "CreateTwilioPhoneNumberDTO",
        "CreateVapiPhoneNumberDTO",
        "CreateVonagePhoneNumberDTO",
    ],
) -> Response[
    Union["ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"]
]:
    """Create Phone Number

    Args:
        body (Union['CreateByoPhoneNumberDTO', 'CreateTelnyxPhoneNumberDTO',
            'CreateTwilioPhoneNumberDTO', 'CreateVapiPhoneNumberDTO', 'CreateVonagePhoneNumberDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ByoPhoneNumber', 'TelnyxPhoneNumber', 'TwilioPhoneNumber', 'VapiPhoneNumber', 'VonagePhoneNumber']]
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
        "CreateByoPhoneNumberDTO",
        "CreateTelnyxPhoneNumberDTO",
        "CreateTwilioPhoneNumberDTO",
        "CreateVapiPhoneNumberDTO",
        "CreateVonagePhoneNumberDTO",
    ],
) -> Optional[
    Union["ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"]
]:
    """Create Phone Number

    Args:
        body (Union['CreateByoPhoneNumberDTO', 'CreateTelnyxPhoneNumberDTO',
            'CreateTwilioPhoneNumberDTO', 'CreateVapiPhoneNumberDTO', 'CreateVonagePhoneNumberDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ByoPhoneNumber', 'TelnyxPhoneNumber', 'TwilioPhoneNumber', 'VapiPhoneNumber', 'VonagePhoneNumber']
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        "CreateByoPhoneNumberDTO",
        "CreateTelnyxPhoneNumberDTO",
        "CreateTwilioPhoneNumberDTO",
        "CreateVapiPhoneNumberDTO",
        "CreateVonagePhoneNumberDTO",
    ],
) -> Response[
    Union["ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"]
]:
    """Create Phone Number

    Args:
        body (Union['CreateByoPhoneNumberDTO', 'CreateTelnyxPhoneNumberDTO',
            'CreateTwilioPhoneNumberDTO', 'CreateVapiPhoneNumberDTO', 'CreateVonagePhoneNumberDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ByoPhoneNumber', 'TelnyxPhoneNumber', 'TwilioPhoneNumber', 'VapiPhoneNumber', 'VonagePhoneNumber']]
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
        "CreateByoPhoneNumberDTO",
        "CreateTelnyxPhoneNumberDTO",
        "CreateTwilioPhoneNumberDTO",
        "CreateVapiPhoneNumberDTO",
        "CreateVonagePhoneNumberDTO",
    ],
) -> Optional[
    Union["ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"]
]:
    """Create Phone Number

    Args:
        body (Union['CreateByoPhoneNumberDTO', 'CreateTelnyxPhoneNumberDTO',
            'CreateTwilioPhoneNumberDTO', 'CreateVapiPhoneNumberDTO', 'CreateVonagePhoneNumberDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ByoPhoneNumber', 'TelnyxPhoneNumber', 'TwilioPhoneNumber', 'VapiPhoneNumber', 'VonagePhoneNumber']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
