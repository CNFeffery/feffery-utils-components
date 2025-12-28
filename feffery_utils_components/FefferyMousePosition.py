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


class FefferyMousePosition(Component):
    """A FefferyMousePosition component.
鼠标位置监听组件FefferyMousePosition

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- position (dict; optional):
    监听当前鼠标位置相关信息."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyMousePosition'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        position: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'position']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'position']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyMousePosition, self).__init__(**args)

setattr(FefferyMousePosition, "__init__", _explicitize_args(FefferyMousePosition.__init__))
