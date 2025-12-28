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


class FefferyVirtualList(Component):
    """A FefferyVirtualList component.
虚拟滚动组件FefferyVirtualList

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，设置内嵌元素内容.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- height (number; required):
    虚拟化区域像素高度.

- itemHeight (number; required):
    每个子元素区域的像素高度."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyVirtualList'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        height: typing.Optional[NumberType] = None,
        itemHeight: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'height', 'itemHeight']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'height', 'itemHeight']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['height', 'itemHeight']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyVirtualList, self).__init__(children=children, **args)

setattr(FefferyVirtualList, "__init__", _explicitize_args(FefferyVirtualList.__init__))
