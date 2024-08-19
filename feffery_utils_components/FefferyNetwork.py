# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyNetwork(Component):
    """A FefferyNetwork component.
网络状态信息监听组件FefferyNetwork

Keyword arguments:

- id (string; optional):
    组件id.

- downlink (number; optional):
    有效带宽估算（单位：兆比特/秒）.

- downlinkMax (number; optional):
    最大下行速度（单位：兆比特/秒）.

- effectiveType (a value equal to: 'slow-2g', '2g', '3g', '4g'; optional):
    网络连接的类型，可选的值有'slow-2g'、'2g'、'3g'、'4g'.

- key (string; optional):
    强制刷新用key值.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- online (boolean; optional):
    网络是否为在线.

- rtt (number; optional):
    当前连接下评估的往返时延.

- saveData (boolean; optional):
    用户代理是否设置了减少数据使用的选项.

- since (string; optional):
    `online`最后改变时间.

- type (a value equal to: 'bluetooth', 'cellular', 'ethernet', 'none', 'wifi', 'wimax', 'other', 'unknown'; optional):
    设备使用与所述网络进行通信的连接的类型，可选项有'bluetooth'、'cellular'、'ethernet'、'none'、'wifi'、'wimax'、'other'、'unknown'."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyNetwork'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, online=Component.UNDEFINED, since=Component.UNDEFINED, rtt=Component.UNDEFINED, type=Component.UNDEFINED, downlink=Component.UNDEFINED, downlinkMax=Component.UNDEFINED, saveData=Component.UNDEFINED, effectiveType=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'downlink', 'downlinkMax', 'effectiveType', 'key', 'loading_state', 'online', 'rtt', 'saveData', 'since', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'downlink', 'downlinkMax', 'effectiveType', 'key', 'loading_state', 'online', 'rtt', 'saveData', 'since', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyNetwork, self).__init__(**args)
