"""A MultiTerminalManager for use in the notebook webserver
- raises HTTPErrors
- creates REST API models
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import warnings

from datetime import timedelta
from notebook._tz import utcnow, isoformat
from terminado import NamedTermManager
from tornado import web
from tornado.ioloop import IOLoop, PeriodicCallback
from traitlets import Integer, validate
from traitlets.config import LoggingConfigurable
from ..prometheus.metrics import TERMINAL_CURRENTLY_RUNNING_TOTAL


class TerminalManager(LoggingConfigurable, NamedTermManager):
    """  """

    _culler_callback = None

    _initialized_culler = False

    cull_inactive_timeout = Integer(0, config=True,
        help="""Timeout (in seconds) in which a terminal has been inactive and ready to be culled.
        Values of 0 or lower disable culling."""
                                    )

    cull_interval_default = 300  # 5 minutes
    cull_interval = Integer(cull_interval_default, config=True,
        help="""The interval (in seconds) on which to check for terminals exceeding the inactive timeout value."""
                            )

    # -------------------------------------------------------------------------
    # Methods for managing terminals
    # -------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create(self):
        """Create a new terminal."""
        name, term = self.new_named_terminal()
        return self._finish_create(name, term)

    def create_with_name(self, name):
        """Create a new terminal."""
        if name in self.terminals:
            raise web.HTTPError(409, f"A terminal with name '{name}' already exists.")
        term = self.get_terminal(name)
        return self._finish_create(name, term)

    def _finish_create(self, name, term):
        # Monkey-patch last-activity, similar to kernels.  Should we need
        # more functionality per terminal, we can look into possible sub-
        # classing or containment then.
        term.last_activity = utcnow()
        model = self.get_terminal_model(name)
        # Increase the metric by one because a new terminal was created
        TERMINAL_CURRENTLY_RUNNING_TOTAL.inc()
        # Ensure culler is initialized
        self._initialize_culler()
        return model

    def get(self, name):
        """Get terminal 'name'."""
        model = self.get_terminal_model(name)
        return model

    def list(self):
        """Get a list of all running terminals."""
        models = [self.get_terminal_model(name) for name in self.terminals]

        # Update the metric below to the length of the list 'terms'
        TERMINAL_CURRENTLY_RUNNING_TOTAL.set(
            len(models)
        )
        return models

    async def terminate(self, name, force=False):
        """Terminate terminal 'name'."""
        self._check_terminal(name)
        await super().terminate(name, force=force)

        # Decrease the metric below by one
        # because a terminal has been shutdown
        TERMINAL_CURRENTLY_RUNNING_TOTAL.dec()

    async def terminate_all(self):
        """Terminate all terminals."""
        terms = [name for name in self.terminals]
        for term in terms:
            await self.terminate(term, force=True)

    def get_terminal_model(self, name):
        """Return a JSON-safe dict representing a terminal.
        For use in representing terminals in the JSON APIs.
        """
        self._check_terminal(name)
        term = self.terminals[name]
        model = {
            "name": name,
            "last_activity": isoformat(term.last_activity),
        }
        return model

    def _check_terminal(self, name):
        """Check a that terminal 'name' exists and raise 404 if not."""
        if name not in self.terminals:
            raise web.HTTPError(404, f'Terminal not found: {name}')

    def _initialize_culler(self):
        """Start culler if 'cull_inactive_timeout' is greater than zero.
        Regardless of that value, set flag that we've been here.
        """
        if not self._initialized_culler and self.cull_inactive_timeout > 0:
            if self._culler_callback is None:
                loop = IOLoop.current()
                if self.cull_interval <= 0:  # handle case where user set invalid value
                    self.log.warning("Invalid value for 'cull_interval' detected (%s) - using default value (%s).",
                                     self.cull_interval, self.cull_interval_default)
                    self.cull_interval = self.cull_interval_default
                self._culler_callback = PeriodicCallback(
                    self._cull_terminals, 1000 * self.cull_interval)
                self.log.info("Culling terminals with inactivity > %s seconds at %s second intervals ...",
                              self.cull_inactive_timeout, self.cull_interval)
                self._culler_callback.start()

        self._initialized_culler = True

    async def _cull_terminals(self):
        self.log.debug("Polling every %s seconds for terminals inactive for > %s seconds...",
                       self.cull_interval, self.cull_inactive_timeout)
        # Create a separate list of terminals to avoid conflicting updates while iterating
        for name in list(self.terminals):
            try:
                await self._cull_inactive_terminal(name)
            except Exception as e:
                self.log.exception(
                    f"The following exception was encountered while checking the activity of terminal {name}: {e}"
                )

    async def _cull_inactive_terminal(self, name):
        try:
            term = self.terminals[name]
        except KeyError:
            return  # KeyErrors are somewhat expected since the terminal can be terminated as the culling check is made.

        self.log.debug("name=%s, last_activity=%s", name, term.last_activity)
        if hasattr(term, 'last_activity'):
            dt_now = utcnow()
            dt_inactive = dt_now - term.last_activity
            # Compute idle properties
            is_time = dt_inactive > timedelta(seconds=self.cull_inactive_timeout)
            # Cull the kernel if all three criteria are met
            if (is_time):
                inactivity = int(dt_inactive.total_seconds())
                self.log.warning("Culling terminal '%s' due to %s seconds of inactivity.", name, inactivity)
                await self.terminate(name, force=True)
