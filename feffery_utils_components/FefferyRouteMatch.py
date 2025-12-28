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


class FefferyRouteMatch(Component):
    """A FefferyRouteMatch component.
路由匹配组件FefferyRouteMatch

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- pattern (string; required):
    必填，目标路由匹配模式规则.

- match (boolean; optional):
    监听当前地址是否匹配目标路由.

- params (dict; optional):
    当前地址匹配目标路由时，监听对应的相关参数信息.

- updateParamsWhenMatch (boolean; default True):
    是否仅在当前地址匹配目标路由时，对`params`进行更新  默认值：`True`."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyRouteMatch'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        pattern: typing.Optional[typing.Union[str]] = None,
        match: typing.Optional[bool] = None,
        params: typing.Optional[dict] = None,
        updateParamsWhenMatch: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'pattern', 'match', 'params', 'updateParamsWhenMatch']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'pattern', 'match', 'params', 'updateParamsWhenMatch']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['pattern']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyRouteMatch, self).__init__(**args)

setattr(FefferyRouteMatch, "__init__", _explicitize_args(FefferyRouteMatch.__init__))
