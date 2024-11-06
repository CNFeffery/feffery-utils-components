# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyPostEventSource(Component):
    """A FefferyPostEventSource component.
POST请求EventSource通信组件FefferyPostEventSource

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- url (string; required):
    必填，目标服务地址.

- headers (dict; optional):
    设置请求头字典.

- body (string; optional):
    设置请求体信息.

- withCredentials (boolean; optional):
    是否使用凭证.

- immediate (boolean; default True):
    是否立即建立连接  默认：`True`.

- autoReconnect (dict; default False):
    配置连接断开自动重连相关参数，设置为`False`时将不会自动重连  默认：`False`.

    `autoReconnect` is a dict with keys:

    - retries (number; optional):
        重试次数.

    - delay (number; optional):
        重试前的延时时长，单位：毫秒. | boolean

- status (string; optional):
    监听最新的连接状态.

- data (boolean | number | string | dict | list; optional):
    监听最新的返回数据.

- event (string; optional):
    监听最新的事件名称.

- operation (a value equal to: 'open', 'close'; optional):
    控制要立即执行的操作，可选项有`'open'`、`'close'`，每次新的操作执行完成后都会重置为空值.

- errorEvent (dict; optional):
    监听最新的异常错误事件.

    `errorEvent` is a dict with keys:

    - timestamp (number; optional):
        错误事件时间戳.

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
    _type = 'FefferyPostEventSource'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, url=Component.REQUIRED, headers=Component.UNDEFINED, body=Component.UNDEFINED, withCredentials=Component.UNDEFINED, immediate=Component.UNDEFINED, autoReconnect=Component.UNDEFINED, status=Component.UNDEFINED, data=Component.UNDEFINED, event=Component.UNDEFINED, operation=Component.UNDEFINED, errorEvent=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'url', 'headers', 'body', 'withCredentials', 'immediate', 'autoReconnect', 'status', 'data', 'event', 'operation', 'errorEvent', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'url', 'headers', 'body', 'withCredentials', 'immediate', 'autoReconnect', 'status', 'data', 'event', 'operation', 'errorEvent', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['url']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyPostEventSource, self).__init__(**args)