from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.byo_phone_number import ByoPhoneNumber
from ...models.telnyx_phone_number import TelnyxPhoneNumber
from ...models.twilio_phone_number import TwilioPhoneNumber
from ...models.vapi_phone_number import VapiPhoneNumber
from ...models.vonage_phone_number import VonagePhoneNumber
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/phone-number/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union["ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"]
]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union["ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ByoPhoneNumber.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = TwilioPhoneNumber.from_dict(data)

                return response_200_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = VonagePhoneNumber.from_dict(data)

                return response_200_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3 = VapiPhoneNumber.from_dict(data)

                return response_200_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_4 = TelnyxPhoneNumber.from_dict(data)

            return response_200_type_4

        response_200 = _parse_response_200(response.json())

        return response_200
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
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union["ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"]
]:
    """Delete Phone Number

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ByoPhoneNumber', 'TelnyxPhoneNumber', 'TwilioPhoneNumber', 'VapiPhoneNumber', 'VonagePhoneNumber']]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union["ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"]
]:
    """Delete Phone Number

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ByoPhoneNumber', 'TelnyxPhoneNumber', 'TwilioPhoneNumber', 'VapiPhoneNumber', 'VonagePhoneNumber']
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union["ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"]
]:
    """Delete Phone Number

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ByoPhoneNumber', 'TelnyxPhoneNumber', 'TwilioPhoneNumber', 'VapiPhoneNumber', 'VonagePhoneNumber']]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union["ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"]
]:
    """Delete Phone Number

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ByoPhoneNumber', 'TelnyxPhoneNumber', 'TwilioPhoneNumber', 'VapiPhoneNumber', 'VonagePhoneNumber']
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
