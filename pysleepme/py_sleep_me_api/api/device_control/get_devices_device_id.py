from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.status import Status
from ...types import Response


def _get_kwargs(
    device_id: str,
    *,
    client: Client,
) -> dict[str, Any]:
    url = f"{client.base_url}/devices/{device_id}"

    headers: dict[str, str] = client.get_headers()
    cookies: dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Status]]:
    if response.status_code == 200:
        response_200 = Status.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Status]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    device_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Status]]:
    """Gets the current status for a given device

     This will give a device's metadata and control state

    Args:
        device_id (str):

    Returns:
        Response[Union[Any, Status]]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    device_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Status]]:
    """Gets the current status for a given device

     This will give a device's metadata and control state

    Args:
        device_id (str):

    Returns:
        Response[Union[Any, Status]]
    """

    return sync_detailed(
        device_id=device_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    device_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Status]]:
    """Gets the current status for a given device

     This will give a device's metadata and control state

    Args:
        device_id (str):

    Returns:
        Response[Union[Any, Status]]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    device_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Status]]:
    """Gets the current status for a given device

     This will give a device's metadata and control state

    Args:
        device_id (str):

    Returns:
        Response[Union[Any, Status]]
    """

    return (
        await asyncio_detailed(
            device_id=device_id,
            client=client,
        )
    ).parsed
