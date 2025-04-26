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


class FefferyWebSocket(Component):
    """A FefferyWebSocket component.
WebSocket通信组件FefferyWebSocket

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- socketUrl (string; required):
    设置要建立连接的WebSocket服务`url`.

- reconnectLimit (number; optional):
    设置连接重试次数  默认为`3`.

- reconnectInterval (number; optional):
    设置连接重试间隔，单位：毫秒  默认为`3000`.

- operation (a value equal to: 'connect', 'disconnect', 'send'; optional):
    用于执行连接/断开连接/发送信息操作，可选项有`'connect'`、`'disconnect'`、`'send'`，每次新操作执行后，operation参数都会被重置为None.

- message (string; optional):
    当operation更新为`'send'`时，用于设置要通过WebSocket服务向服务器发送的数据.

- latestMessage (string; optional):
    监听从服务器传来的最新信息.

- state (a value equal to: 'connecting', 'open', 'closing', 'closed'; optional):
    用于监听当前此连接的状态，有`'connecting'`、`'open'`、`'closing'`、`'closed'`四种状态."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyWebSocket'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        socketUrl: typing.Optional[str] = None,
        reconnectLimit: typing.Optional[NumberType] = None,
        reconnectInterval: typing.Optional[NumberType] = None,
        operation: typing.Optional[Literal["connect", "disconnect", "send"]] = None,
        message: typing.Optional[str] = None,
        latestMessage: typing.Optional[str] = None,
        state: typing.Optional[Literal["connecting", "open", "closing", "closed"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'socketUrl', 'reconnectLimit', 'reconnectInterval', 'operation', 'message', 'latestMessage', 'state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'socketUrl', 'reconnectLimit', 'reconnectInterval', 'operation', 'message', 'latestMessage', 'state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['socketUrl']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyWebSocket, self).__init__(**args)

setattr(FefferyWebSocket, "__init__", _explicitize_args(FefferyWebSocket.__init__))
