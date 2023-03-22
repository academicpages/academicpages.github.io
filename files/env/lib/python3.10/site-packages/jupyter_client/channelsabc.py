"""Abstract base classes for kernel client channels"""
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import abc


class ChannelABC(object, metaclass=abc.ABCMeta):
    """A base class for all channel ABCs."""

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def is_alive(self):
        pass


class HBChannelABC(ChannelABC):
    """HBChannel ABC.

    The docstrings for this class can be found in the base implementation:

    `jupyter_client.channels.HBChannel`
    """

    @abc.abstractproperty
    def time_to_dead(self):
        pass

    @abc.abstractmethod
    def pause(self):
        pass

    @abc.abstractmethod
    def unpause(self):
        pass

    @abc.abstractmethod
    def is_beating(self):
        pass
