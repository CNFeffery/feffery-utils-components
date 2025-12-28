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


class FefferyGridItem(Component):
    """A FefferyGridItem component.
可拖拽网格项组件FefferyGridItem

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    用于为当前可拖拽网格项设置唯一标识`key`值.

- children (a list of or a singular dash component, string or number; optional):
    组件型，内嵌元素.

- className (string; optional):
    当前组件css类名."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyGridItem'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyGridItem, self).__init__(children=children, **args)

setattr(FefferyGridItem, "__init__", _explicitize_args(FefferyGridItem.__init__))
