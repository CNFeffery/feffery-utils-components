# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyLocalLargeStorage(Component):
    """A FefferyLocalLargeStorage component.
客户端大容量存储器FefferyLocalLargeStorage

Keyword arguments:

- id (string; required):
    用于定义当前存储器的唯一识别id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- data (boolean | number | string | dict | list; optional):
    定义当前存储器对应存储在浏览器本地的数据.

- initialSync (boolean; default False):
    设置初始化时是否从浏览器本地存储中尝试读取`id`对应的值并更新到`data`中  默认值：`False`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyLocalLargeStorage'

    @_explicitize_args
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

        super(FefferyLocalLargeStorage, self).__init__(**args)
