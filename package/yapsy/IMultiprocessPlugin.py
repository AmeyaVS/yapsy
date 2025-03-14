# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t; python-indent: 4 -*-


"""
Role
====

Defines the basic interfaces for multiprocessed plugins.

Extensibility
=============

In your own software, you'll probably want to build derived classes of
the ``IMultiprocessPlugin`` class as it is a mere interface with no specific
functionality.

Your software's plugins should then inherit your very own plugin class
(itself derived from ``IMultiprocessPlugin``).

Override the `run` method to include your code. Use the `self.parent_pipe` to send
and receive data with the parent process or create your own communication
mecanism.

Where and how to code these plugins is explained in the section about
the :doc:`PluginManager`.

API
===
"""

from yapsy.IPlugin import IPlugin


class IMultiprocessPlugin(IPlugin):
    """
    Base class for multiprocessed plugin.
    """

    def __init__(self, parent_pipe):
        IPlugin.__init__(self)
        self.parent_pipe = parent_pipe

    def run(self):
        """
        Override this method in your implementation
        """
        return
