# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyEventSource(Component):
    """A FefferyEventSource component.
EventSource通信组件FefferyEventSource

Keyword arguments:

- id (string; optional):
    组件id.

- autoReconnect (dict; default False):
    配置连接断开自动重连相关参数，设置为`False`时将不会自动重连  默认：`False`.

    `autoReconnect` is a dict with keys:

    - delay (number; optional):
        重试前的延时时长，单位：毫秒.

    - retries (number; optional):
        重试次数. | boolean

- data (boolean | number | string | dict | list; optional):
    监听最新的返回数据.

- event (string; optional):
    监听最新的事件名称.

- events (list of strings; optional):
    目标事件名称列表.

- immediate (boolean; default True):
    是否立即建立连接  默认：`True`.

- key (string; optional):
    强制刷新用唯一标识key值.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- operation (a value equal to: 'open', 'close'; optional):
    控制要立即执行的操作，可选项有`'open'`、`'close'`，每次新的操作执行完成后都会重置为空值.

- status (string; optional):
    监听最新的连接状态.

- url (string; required):
    必填，目标服务地址."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyEventSource'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, url=Component.REQUIRED, events=Component.UNDEFINED, immediate=Component.UNDEFINED, autoReconnect=Component.UNDEFINED, status=Component.UNDEFINED, data=Component.UNDEFINED, event=Component.UNDEFINED, operation=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'autoReconnect', 'data', 'event', 'events', 'immediate', 'key', 'loading_state', 'operation', 'status', 'url']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'autoReconnect', 'data', 'event', 'events', 'immediate', 'key', 'loading_state', 'operation', 'status', 'url']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['url']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyEventSource, self).__init__(**args)
