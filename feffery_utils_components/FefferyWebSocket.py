# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyWebSocket(Component):
    """A FefferyWebSocket component.


Keyword arguments:

- id (string; optional):
    组件id.

- socketUrl (string; required):
    设置要建立连接的WebSocket服务url.

- reconnectLimit (number; optional):
    设置连接重试次数，默认为3.

- reconnectInterval (number; optional):
    设置连接重试间隔，默认为3000，单位：毫秒.

- operation (a value equal to: 'connect', 'disconnect', 'send'; optional):
    用于执行连接/断开连接/发送信息操作，可选项有'connect'、'disconnect'、'send'，
    每次新操作执行后，operation参数都会被重置为None.

- message (string; optional):
    当operation更新为'send'时，用于设置要通过WebSocket服务向服务器发送的数据.

- latestMessage (string; optional):
    监听从服务器传来的最新信息.

- state (a value equal to: 'connecting', 'open', 'closing', 'closed'; optional):
    用于监听当前此连接的状态，有'connecting'、'open'、'closing'、'closed'四种状态.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyWebSocket'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, socketUrl=Component.REQUIRED, reconnectLimit=Component.UNDEFINED, reconnectInterval=Component.UNDEFINED, operation=Component.UNDEFINED, message=Component.UNDEFINED, latestMessage=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'socketUrl', 'reconnectLimit', 'reconnectInterval', 'operation', 'message', 'latestMessage', 'state', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'socketUrl', 'reconnectLimit', 'reconnectInterval', 'operation', 'message', 'latestMessage', 'state', 'loading_state']
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
