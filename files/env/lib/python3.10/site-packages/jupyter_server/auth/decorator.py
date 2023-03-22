"""Decorator for layering authorization into JupyterHandlers.
"""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
from functools import wraps
from typing import Callable, Optional, Union

from tornado.log import app_log
from tornado.web import HTTPError

from .utils import HTTP_METHOD_TO_AUTH_ACTION


def authorized(
    action: Optional[Union[str, Callable]] = None,
    resource: Optional[str] = None,
    message: Optional[str] = None,
) -> Callable:
    """A decorator for tornado.web.RequestHandler methods
    that verifies whether the current user is authorized
    to make the following request.

    Helpful for adding an 'authorization' layer to
    a REST API.

    .. versionadded:: 2.0

    Parameters
    ----------
    action : str
        the type of permission or action to check.

    resource: str or None
        the name of the resource the action is being authorized
        to access.

    message : str or none
        a message for the unauthorized action.
    """

    def wrapper(method):
        @wraps(method)
        def inner(self, *args, **kwargs):
            # default values for action, resource
            nonlocal action
            nonlocal resource
            nonlocal message
            if action is None:
                http_method = self.request.method.upper()
                action = HTTP_METHOD_TO_AUTH_ACTION[http_method]
            if resource is None:
                resource = self.auth_resource
            if message is None:
                message = f"User is not authorized to {action} on resource: {resource}."

            user = self.current_user
            if not user:
                app_log.warning("Attempting to authorize request without authentication!")
                raise HTTPError(status_code=403, log_message=message)
            # If the user is allowed to do this action,
            # call the method.
            if self.authorizer.is_authorized(self, user, action, resource):
                return method(self, *args, **kwargs)
            # else raise an exception.
            else:
                raise HTTPError(status_code=403, log_message=message)

        return inner

    if callable(action):
        method = action
        action = None
        # no-arguments `@authorized` decorator called
        return wrapper(method)

    return wrapper
