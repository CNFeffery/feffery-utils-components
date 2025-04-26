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


class FefferyFormatBytes(Component):
    """A FefferyFormatBytes component.
字节格式化组件FefferyFormatBytes

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- value (number; default 0):
    待格式化的原始字节数值  默认值：`0`.

- unit (a value equal to: 'byte', 'bit'; default 'byte'):
    展示单位，可选项有`'byte'`、`'bit'`  默认值：`'byte'`.

- display (a value equal to: 'long', 'short', 'narrow'; default 'short'):
    展示类型，可选项有`'long'`、`'short'`、`'narrow'`  默认值：`'short'`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyFormatBytes'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        value: typing.Optional[NumberType] = None,
        unit: typing.Optional[Literal["byte", "bit"]] = None,
        display: typing.Optional[Literal["long", "short", "narrow"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'value', 'unit', 'display']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'value', 'unit', 'display']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyFormatBytes, self).__init__(**args)

setattr(FefferyFormatBytes, "__init__", _explicitize_args(FefferyFormatBytes.__init__))
