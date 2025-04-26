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


class FefferyMediaQuery(Component):
    """A FefferyMediaQuery component.
媒体查询监听组件FefferyMediaQuery

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- query (string; required):
    必填，定义媒体查询条件.

- isMatch (boolean; optional):
    监听当前媒体查询是否满足."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyMediaQuery'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        isMatch: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'query', 'isMatch']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'query', 'isMatch']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['query']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyMediaQuery, self).__init__(**args)

setattr(FefferyMediaQuery, "__init__", _explicitize_args(FefferyMediaQuery.__init__))
