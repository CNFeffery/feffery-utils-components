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


class FefferyResponsive(Component):
    """A FefferyResponsive component.
页面响应式监听组件FefferyResponsive

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- responsive (dict; optional):
    监听当前页面尺寸下对应各断点像素宽度的满足情况."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyResponsive'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        responsive: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'responsive']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'responsive']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyResponsive, self).__init__(**args)

setattr(FefferyResponsive, "__init__", _explicitize_args(FefferyResponsive.__init__))
