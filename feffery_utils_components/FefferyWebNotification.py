# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyWebNotification(Component):
    """A FefferyWebNotification component.
web通知组件FefferyWebNotification

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- message (string; optional):
    设置要发送的信息内容，每次成功发送后都会重置为空.

- isSupported (boolean; optional):
    监听用户浏览器中是否支持web通知."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyWebNotification'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        isSupported: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'message', 'isSupported']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'message', 'isSupported']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyWebNotification, self).__init__(**args)
