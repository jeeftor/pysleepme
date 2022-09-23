#!/usr/bin/env python
"""Tests for `pysleepme` package."""

import pytest
from respx import MockRouter

from pysleepme.pysleepme import PySleepMe

TOKEN = "FAKE_TOKEN"
DEVICE_ID = "fake_device_id"


@pytest.mark.parametrize('device_id', [DEVICE_ID])
def test_get_device_by_id_sync(mock_get_device_by_id: MockRouter) -> None:
    """Extract device by id check."""
    psm = PySleepMe(api_token=TOKEN)
    psm.get_device_by_id_sync(DEVICE_ID)


@pytest.mark.parametrize('device_id', [DEVICE_ID])
def test_get_device_by_id_sync_error(mock_get_device_by_id_with_error: MockRouter) -> None:
    """Error version of extract device by id check."""
    psm = PySleepMe(api_token=TOKEN)
    with pytest.raises(Exception):
        psm.get_device_by_id_sync(DEVICE_ID)
