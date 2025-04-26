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


class FefferyInViewport(Component):
    """A FefferyInViewport component.
元素可见性检查组件FefferyInViewport

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，需要进行可见性监听的目标元素.

- inViewport (boolean; optional):
    监听当前元素是否出现在可视范围内.

- threshold (number; optional):
    触发元素可见性状态切换的比例阈值."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyInViewport'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        inViewport: typing.Optional[bool] = None,
        threshold: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'inViewport', 'threshold']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'inViewport', 'threshold']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyInViewport, self).__init__(children=children, **args)

setattr(FefferyInViewport, "__init__", _explicitize_args(FefferyInViewport.__init__))
