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


class FefferyLocalStorage(Component):
    """A FefferyLocalStorage component.
localStorage状态管理组件

Keyword arguments:

- id (string; required):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- data (boolean | number | string | dict | list; optional):
    设置或监听当前`id`对应的`localStorage`数据.

- initialSync (boolean; default False):
    设置初始化时是否从`localStorage`中尝试读取id对应的值并更新到`data`中  默认值：`False`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyLocalStorage'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        data: typing.Optional[typing.Any] = None,
        initialSync: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'data', 'initialSync']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'data', 'initialSync']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyLocalStorage, self).__init__(**args)

setattr(FefferyLocalStorage, "__init__", _explicitize_args(FefferyLocalStorage.__init__))
