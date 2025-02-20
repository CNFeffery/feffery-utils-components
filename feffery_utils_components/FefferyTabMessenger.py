# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyTabMessenger(Component):
    """A FefferyTabMessenger component.
跨标签页通信组件FefferyTabMessenger

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- role (a value equal to: 'sender', 'receiver'; required):
    必填，声明当前组件所在标签页角色，可选的有`'sender'`和`'receiver'`.

- targetUrl (string; optional):
    当`role='sender'`时，用于定义自动创建打开的目标标签页对应`url`.

- targetWindowFeatures (string; optional):
    当`role='sender'`时，用于定义自动创建打开的目标标签页底层调用`window.open()`对应的额外的windowFeatures字符串.

- toSendMessage (boolean | number | string | dict | list; optional):
    当`role='sender'`时，用于设置将要新发送的信息内容，每次成功发送后都会重置为空.

- recivedMessage (boolean | number | string | dict | list; optional):
    当`role='receiver'`时，用于监听最近一次收到的信息内容."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyTabMessenger'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        role: typing.Optional[Literal["sender", "receiver"]] = None,
        targetUrl: typing.Optional[str] = None,
        targetWindowFeatures: typing.Optional[str] = None,
        toSendMessage: typing.Optional[typing.Any] = None,
        recivedMessage: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'role', 'targetUrl', 'targetWindowFeatures', 'toSendMessage', 'recivedMessage']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'role', 'targetUrl', 'targetWindowFeatures', 'toSendMessage', 'recivedMessage']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['role']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyTabMessenger, self).__init__(**args)
