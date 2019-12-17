#!/usr/bin/env python
from functools import wraps

class Borg:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state
        if 'hooks' not in self.__dict__:
            self.__dict__['hooks'] = {}
        if 'direct' not in self.__dict__:
            self.__dict__['direct'] = {}


def on_start(*args, **kwargs):
    def _command_hook(func):
        return func

    # if len(args) == 1 and callable(args[0]):  # this decorator is being used directly
    return lambda func: _command_hook(func)

def legacy_command(*args, **kwargs):
    """External command decorator. Can be used directly as a decorator, or with args to return a decorator.
    :type param: str | list[str] | function
    """

    def _command_hook(func, alias_param=None):
        hooks = Borg()
        for alias in alias_param:
            hooks.__dict__['hooks'][alias] = func
        return func

    if len(args) == 1 and callable(args[0]):  # this decorator is being used directly
        return _command_hook(args[0])
    else:  # this decorator is being used indirectly, so return a decorator function
        return lambda func: _command_hook(func, alias_param=args)

def command(*args, **kwargs):
    """External command decorator. Can be used directly as a decorator, or with args to return a decorator.
    :type param: str | list[str] | function
    """

    def _command_hook(func, alias_param=None):
        hooks = Borg()
        for alias in alias_param:
            hooks.__dict__['direct'][alias] = func
        return func

    if len(args) == 1 and callable(args[0]):  # this decorator is being used directly
        return _command_hook(args[0])
    else:  # this decorator is being used indirectly, so return a decorator function
        return lambda func: _command_hook(func, alias_param=args)

def wrapper(func):
    return lambda bot, update: update.message.reply_text(func(update.message.text[update.message.text.find(" ")+1:]))
