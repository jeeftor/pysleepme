#!/usr/bin/env python
"""Tests for `pysleepme` package."""
import json
from collections.abc import Generator

import pytest
import respx
from httpx import Response
from respx import MockRouter

from pysleepme.const import BASE_URL, ENDPOINT_DEVICES
from pysleepme.exceptions import (
    BadRequestException,
    DeviceNotFoundException,
    ForbiddenException,
    ServerErrorException,
    UnauthorizedException,
)
from pysleepme.pysleepme import PySleepMe

DEVICES_RESPONSE = '''[
    {
        "id": "zx-cagh25ahjfawkfawhg",
        "name": "My Dock Pro",
        "attachments": [
            "CHILIPAD_PRO"
        ]
    },
    {
        "id": "zx-wagagj21qk222j25525",
        "name": "Another Dock Pro",
        "attachments": [
            "CHILIPAD_PRO"
        ]
    }
]'''
SINGLE_DEVICE_RESPONSE = '''{
    "about": {
        "firmware_version": "5.15",
        "ip_address": "25.26.873.23",
        "lan_address": "192.168.0.131",
        "mac_address": "b5:56:12:67:jg:w2",
        "model": "DP999NA",
        "serial_number": "6236265923682376276"
    },
    "control": {
        "brightness_level": 100,
        "display_temperature_unit": "f",
        "set_temperature_c": 23.5,
        "set_temperature_f": 74,
        "thermal_control_status": "active",
        "time_zone": "America/New_York"
    },
    "status": {
        "is_connected": true,
        "is_water_low": false,
        "water_level": 100,
        "water_temperature_f": 74,
        "water_temperature_c": 23.5
    }
}'''


@pytest.fixture()
def mock_get_devices_with_error(status_code: int) -> Generator:
    """Parameterizable fixture."""
    with respx.mock(base_url=BASE_URL, assert_all_called=False) as respx_mock:
        devices_route = respx_mock.get(f"/{ENDPOINT_DEVICES}")
        devices_route.return_value = Response(status_code)
        yield respx_mock


@pytest.fixture()
def mock_get_devices() -> Generator:
    """Test fixture for devices endpoint."""
    with respx.mock(base_url=BASE_URL, assert_all_called=False) as respx_mock:
        devices_route = respx_mock.get(f"/{ENDPOINT_DEVICES}")
        devices_route.return_value = Response(200, json=json.loads(DEVICES_RESPONSE))
        yield respx_mock


@pytest.mark.parametrize('status_code', [400])
def test_error_400(mock_get_devices_with_error: MockRouter) -> None:
    """Test for error code 400."""
    TOKEN = "FAKE_TOKEN"
    psm = PySleepMe(api_token=TOKEN)
    with pytest.raises(BadRequestException) as exc_info:
        psm.get_devices_sync()
    assert BadRequestException == exc_info.type
    assert True


@pytest.mark.parametrize('status_code', [401])
def test_error_401(mock_get_devices_with_error: MockRouter) -> None:
    """Test for error code 401."""
    TOKEN = "FAKE_TOKEN"
    psm = PySleepMe(api_token=TOKEN)
    with pytest.raises(UnauthorizedException) as exc_info:
        psm.get_devices_sync()
    assert UnauthorizedException == exc_info.type
    assert True


@pytest.mark.parametrize('status_code', [403])
def test_error_403(mock_get_devices_with_error: MockRouter) -> None:
    """Test for error code 403."""
    TOKEN = "FAKE_TOKEN"
    psm = PySleepMe(api_token=TOKEN)
    with pytest.raises(ForbiddenException) as exc_info:
        psm.get_devices_sync()
    assert ForbiddenException == exc_info.type
    assert True


@pytest.mark.parametrize('status_code', [404])
def test_error_404(mock_get_devices_with_error: MockRouter) -> None:
    """Test for error code 404."""
    TOKEN = "FAKE_TOKEN"
    psm = PySleepMe(api_token=TOKEN)
    with pytest.raises(DeviceNotFoundException) as exc_info:
        psm.get_devices_sync()
    assert DeviceNotFoundException == exc_info.type


@pytest.mark.parametrize('status_code', [500])
def test_error_500(mock_get_devices_with_error: MockRouter) -> None:
    """Test for error code 500."""
    TOKEN = "FAKE_TOKEN"
    psm = PySleepMe(api_token=TOKEN)
    with pytest.raises(ServerErrorException) as exc_info:
        psm.get_devices_sync()
    assert ServerErrorException == exc_info.type


# @pytest.mark.parametrize('status_code', [500])
#
# def test_error_404(mock_get_devices_with_error: MockRouter) -> None:
# """Test for error code 404."""
#     TOKEN = "FAKE_TOKEN"
#     psm = PySleepMe(api_token=TOKEN)
#     assertRaises(ServerErrorException, psm.get_devices_sync())
#     assert True
#
#     with pytest.raises(ServerErrorException) as exc_info:
#         psm.get_devices_sync()
#     assert ServerErrorException == exc_info.type
#     assert True


def test_devices_fixture(mock_get_devices: MockRouter) -> None:
    """Perform test using fixture."""
    TOKEN = "FAKE_TOKEN"
    psm = PySleepMe(api_token=TOKEN)
    devices = psm.get_devices_sync()
    assert len(devices) == 2
    assert devices[1].id == 'zx-wagagj21qk222j25525'


def test_devices_sync(respx_mock) -> None:  # type: ignore
    """Test the sync get devices call."""
    respx_mock.get(f"{BASE_URL}/{ENDPOINT_DEVICES}").mock(return_value=Response(200, json=json.loads(DEVICES_RESPONSE)))
    TOKEN = "FAKE_TOKEN"
    psm = PySleepMe(api_token=TOKEN)
    devices = psm.get_devices_sync()
    assert len(devices) == 2
    assert devices[1].id == 'zx-wagagj21qk222j25525'
