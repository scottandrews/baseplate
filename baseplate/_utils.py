"""Internal library helpers."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


import functools
import warnings


def warn_deprecated(message):
    """Emit a deprecation warning from the caller.

    The stacktrace for the warning will point to the place where the function
    calling this was called, rather than in baseplate. This allows the user to
    most easily see where in _their_ code the deprecation is coming from.

    """
    warnings.warn(message, DeprecationWarning, stacklevel=3)


class cached_property(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped
        functools.update_wrapper(self, wrapped)

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        ret = self.wrapped(obj)
        setattr(obj, self.wrapped.__name__, ret)
        return ret
