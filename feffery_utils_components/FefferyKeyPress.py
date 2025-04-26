# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class FefferyKeyPress(Component):
    """A FefferyKeyPress component.
按键事件监听组件FefferyKeyPress

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- keys (string; required):
    必填，用于设置要监听的按键组合.

- pressedCounts (number; default 0):
    记录设置的按键或按键组合事件已被触发的次数  默认值：`0`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyKeyPress'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        keys: typing.Optional[str] = None,
        pressedCounts: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'keys', 'pressedCounts']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'keys', 'pressedCounts']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['keys']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyKeyPress, self).__init__(**args)

setattr(FefferyKeyPress, "__init__", _explicitize_args(FefferyKeyPress.__init__))
