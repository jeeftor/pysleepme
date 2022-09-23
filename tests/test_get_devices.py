#!/usr/bin/env python
"""Tests for `pysleepme` package."""

import pytest
from respx import MockRouter

from pysleepme.exceptions import (
    BadRequestException,
    DeviceNotFoundException,
    ForbiddenException,
    ServerErrorException,
    UnauthorizedException,
)
from pysleepme.pysleepme import PySleepMe

TOKEN = "FAKE_TOKEN"


@pytest.mark.parametrize('status_code', [400])
def test_error_400(mock_get_devices_with_error: MockRouter) -> None:
    """Test for error code 400."""
    psm = PySleepMe(api_token=TOKEN)
    with pytest.raises(BadRequestException) as exc_info:
        psm.get_devices_sync()
    assert BadRequestException == exc_info.type
    assert True


@pytest.mark.parametrize('status_code', [401])
def test_error_401(mock_get_devices_with_error: MockRouter) -> None:
    """Test for error code 401."""
    psm = PySleepMe(api_token=TOKEN)
    with pytest.raises(UnauthorizedException) as exc_info:
        psm.get_devices_sync()
    assert UnauthorizedException == exc_info.type
    assert True


@pytest.mark.parametrize('status_code', [403])
def test_error_403(mock_get_devices_with_error: MockRouter) -> None:
    """Test for error code 403."""
    psm = PySleepMe(api_token=TOKEN)
    with pytest.raises(ForbiddenException) as exc_info:
        psm.get_devices_sync()
    assert ForbiddenException == exc_info.type
    assert True


@pytest.mark.parametrize('status_code', [404])
def test_error_404(mock_get_devices_with_error: MockRouter) -> None:
    """Test for error code 404."""
    psm = PySleepMe(api_token=TOKEN)
    with pytest.raises(DeviceNotFoundException) as exc_info:
        psm.get_devices_sync()
    assert DeviceNotFoundException == exc_info.type


@pytest.mark.parametrize('status_code', [500])
def test_error_500(mock_get_devices_with_error: MockRouter) -> None:
    """Test for error code 500."""
    psm = PySleepMe(api_token=TOKEN)
    with pytest.raises(ServerErrorException) as exc_info:
        psm.get_devices_sync()
    assert ServerErrorException == exc_info.type


@pytest.mark.parametrize('status_code', [501])
def test_error_501(mock_get_devices_with_error: MockRouter) -> None:
    """Test for error code 500."""
    psm = PySleepMe(api_token=TOKEN)
    with pytest.raises(Exception) as exc_info:
        psm.get_devices_sync()
    assert Exception == exc_info.type


def test_devices_fixture(mock_get_devices: MockRouter) -> None:
    """Perform test using fixture."""
    psm = PySleepMe(api_token=TOKEN)
    devices = psm.get_devices_sync()
    assert len(devices) == 2
    assert devices[1].id == 'zx-wagagj21qk222j25525'
