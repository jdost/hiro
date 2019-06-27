"""
patched builtin time classes for use by :class:`hiro.Timeline`
"""
from __future__ import absolute_import
import abc
from datetime import date as realdate
from datetime import datetime as realdatetime
import time
import six


class DatetimeMeta(abc.ABCMeta):
    """
    meta class to allow interaction between :class:`datetime.datetime`
    objects create inside the :class:`hiro.Timeline` with those created
    outside it.
    """
    def __instancecheck__(cls, instance):
        return isinstance(instance, realdatetime)

class DateMeta(type):
    """
    meta class to allow interaction between :class:`datetime.date`
    objects create inside the :class:`hiro.Timeline` with those created
    outside it.
    """
    def __instancecheck__(cls, instance):
        return isinstance(instance, realdate)

@six.add_metaclass(DatetimeMeta)
class Datetime(realdatetime):
    """
    used to patch :class:`datetime.datetime` to follow the rules of the
    parent :class:`hiro.Timeline`
    """

    @classmethod
    def now(cls, tz=None):
        return cls.fromtimestamp(time.time(), tz)

    @classmethod
    def utcnow(cls):
        return cls.utcfromtimestamp(time.time())

@six.add_metaclass(DateMeta)
class Date(six.with_metaclass(DateMeta, realdate)):
    """
    used to patch :class:`datetime.date` to follow the rules of the
    parent :class:`hiro.Timeline`
    """

    @classmethod
    def today(cls):
        return cls.fromtimestamp(time.time())
