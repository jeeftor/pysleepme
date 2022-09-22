from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.device_list_item import DeviceListItem
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> dict[str, Any]:
    url = f"{client.base_url}/devices"

    headers: dict[str, str] = client.get_headers()
    cookies: dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, list[DeviceListItem]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_device_list_item_data in _response_200:
            componentsschemas_device_list_item = DeviceListItem.from_dict(componentsschemas_device_list_item_data)

            response_200.append(componentsschemas_device_list_item)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, list[DeviceListItem]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, list[DeviceListItem]]]:
    """Gets a list of the user's claimed devices

     This endpoint will return a list of claimed devices for a given token.

    Returns:
        Response[Union[Any, List[DeviceListItem]]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[Any, list[DeviceListItem]]]:
    """Gets a list of the user's claimed devices

     This endpoint will return a list of claimed devices for a given token.

    Returns:
        Response[Union[Any, List[DeviceListItem]]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, list[DeviceListItem]]]:
    """Gets a list of the user's claimed devices

     This endpoint will return a list of claimed devices for a given token.

    Returns:
        Response[Union[Any, List[DeviceListItem]]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[Any, list[DeviceListItem]]]:
    """Gets a list of the user's claimed devices

     This endpoint will return a list of claimed devices for a given token.

    Returns:
        Response[Union[Any, List[DeviceListItem]]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
