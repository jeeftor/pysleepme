"""List of exceptions."""


class __DocDefaultException(Exception):
    """Subclass exceptions use docstring as default message."""

    def __init__(self, msg=None, *args, **kwargs):  # type: ignore
        super().__init__(msg or self.__doc__, *args, **kwargs)


class BadRequestException(__DocDefaultException):
    """Status Code 400: Bad Request."""


class UnauthorizedException(__DocDefaultException):
    """Status Code 401: Unauthorized, you are missing / have invalid credential."""


class ForbiddenException(__DocDefaultException):
    """Status Code 403: Forbidden, you are not allowed to read this device status."""


class DeviceNotFoundException(__DocDefaultException):
    """Status Code 404: Device not found."""


class ServerErrorException(__DocDefaultException):
    """Status Code 500: Server error."""


def get_exception_by_status(status_code: int) -> __DocDefaultException:
    """Return correct exception by status code."""
    if status_code == 400:
        return BadRequestException()
    elif status_code == 401:
        return UnauthorizedException()
    elif status_code == 403:
        return ForbiddenException()
    elif status_code == 404:
        return DeviceNotFoundException()
    elif status_code == 500:
        return ServerErrorException()
    else:
        raise Exception()
