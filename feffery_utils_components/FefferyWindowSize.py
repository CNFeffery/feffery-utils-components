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


class FefferyWindowSize(Component):
    """A FefferyWindowSize component.
浏览器窗口尺寸监听组件FefferyWindowSize

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- _width (number; optional):
    监听当前浏览器窗口像素宽度.

- _height (number; optional):
    监听当前浏览器窗口像素高度."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyWindowSize'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        _width: typing.Optional[NumberType] = None,
        _height: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', '_width', '_height']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', '_width', '_height']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyWindowSize, self).__init__(**args)

setattr(FefferyWindowSize, "__init__", _explicitize_args(FefferyWindowSize.__init__))
