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


class FefferyIframeMessenger(Component):
    """A FefferyIframeMessenger component.
跨iframe通信组件FefferyIframeMessenger

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- role (a value equal to: 'sender', 'receiver'; required):
    必填，声明当前组件所在标签页角色，可选的有`'sender'`和`'receiver'`.

- mode (a value equal to: 'to-parent', 'to-child'; required):
    必填，声明当前组件对应传递信息的模式，可选的有`'to-parent'`和`'to-child'`.

- targetIframeId (string; optional):
    当`role='sender'`且`mode='to-child'`时，用于定义需要发送消息的目标iframe组件的`id`.

- toSendMessage (boolean | number | string | dict | list; optional):
    当`role='sender'`时，用于设置将要新发送的信息内容，每次成功发送后都会重置为空.

- recivedMessage (boolean | number | string | dict | list; optional):
    当`role='receiver'`时，用于监听最近一次收到的信息内容."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyIframeMessenger'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        role: typing.Optional[Literal["sender", "receiver"]] = None,
        mode: typing.Optional[Literal["to-parent", "to-child"]] = None,
        targetIframeId: typing.Optional[str] = None,
        toSendMessage: typing.Optional[typing.Any] = None,
        recivedMessage: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'role', 'mode', 'targetIframeId', 'toSendMessage', 'recivedMessage']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'role', 'mode', 'targetIframeId', 'toSendMessage', 'recivedMessage']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['role', 'mode']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyIframeMessenger, self).__init__(**args)

setattr(FefferyIframeMessenger, "__init__", _explicitize_args(FefferyIframeMessenger.__init__))
