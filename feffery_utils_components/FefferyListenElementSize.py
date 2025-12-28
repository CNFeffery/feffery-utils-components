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


class FefferyListenElementSize(Component):
    """A FefferyListenElementSize component.
元素尺寸监听组件FefferyListenElementSize

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- target (string | dict; required):
    必填，设置尺寸监听目标元素`id`.

- width (number; optional):
    监听目标元素像素宽度.

- height (number; optional):
    监听目标元素像素高度."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyListenElementSize'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        target: typing.Optional[typing.Union[str, dict]] = None,
        width: typing.Optional[NumberType] = None,
        height: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'target', 'width', 'height']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'target', 'width', 'height']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['target']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyListenElementSize, self).__init__(**args)

setattr(FefferyListenElementSize, "__init__", _explicitize_args(FefferyListenElementSize.__init__))
