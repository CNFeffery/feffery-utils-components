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


class FefferyNetwork(Component):
    """A FefferyNetwork component.
网络状态信息监听组件FefferyNetwork

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- online (boolean; optional):
    网络是否为在线.

- since (string; optional):
    `online`最后改变时间.

- rtt (number; optional):
    当前连接下评估的往返时延.

- type (a value equal to: 'bluetooth', 'cellular', 'ethernet', 'none', 'wifi', 'wimax', 'other', 'unknown'; optional):
    设备使用与所述网络进行通信的连接的类型，可选项有`'bluetooth'`、`'cellular'`、`'ethernet'`、`'none'`、`'wifi'`、`'wimax'`、`'other'`、`'unknown'`.

- downlink (number; optional):
    有效带宽估算（单位：兆比特/秒）.

- downlinkMax (number; optional):
    最大下行速度（单位：兆比特/秒）.

- saveData (boolean; optional):
    用户代理是否设置了减少数据使用的选项.

- effectiveType (a value equal to: 'slow-2g', '2g', '3g', '4g'; optional):
    网络连接的类型，可选项有`'slow-2g'`、`'2g'`、`'3g'`、`'4g'`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyNetwork'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        online: typing.Optional[bool] = None,
        since: typing.Optional[str] = None,
        rtt: typing.Optional[NumberType] = None,
        type: typing.Optional[Literal["bluetooth", "cellular", "ethernet", "none", "wifi", "wimax", "other", "unknown"]] = None,
        downlink: typing.Optional[NumberType] = None,
        downlinkMax: typing.Optional[NumberType] = None,
        saveData: typing.Optional[bool] = None,
        effectiveType: typing.Optional[Literal["slow-2g", "2g", "3g", "4g"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'online', 'since', 'rtt', 'type', 'downlink', 'downlinkMax', 'saveData', 'effectiveType']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'online', 'since', 'rtt', 'type', 'downlink', 'downlinkMax', 'saveData', 'effectiveType']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyNetwork, self).__init__(**args)

setattr(FefferyNetwork, "__init__", _explicitize_args(FefferyNetwork.__init__))
