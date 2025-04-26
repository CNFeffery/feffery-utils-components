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


class FefferyCssVar(Component):
    """A FefferyCssVar component.
CSS变量更新组件FefferyCssVar

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- cssVars (dict; optional):
    定义要更新的`css`变量键值对信息."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCssVar'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        cssVars: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'cssVars']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'cssVars']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyCssVar, self).__init__(**args)

setattr(FefferyCssVar, "__init__", _explicitize_args(FefferyCssVar.__init__))
