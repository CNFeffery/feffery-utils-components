# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyHttpRequests(Component):
    """A FefferyHttpRequests component.
http请求组件FefferyHttpRequests

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- requestConfig (dict; optional):
    构造新发起http请求对应的参数，每次更新为有效值后会发起相应的请求，每次请求完成（成功或失败）后会自动重置为空值.

    `requestConfig` is a dict with keys:

    - data (dict; optional):
        自定义请求体发送数据.

    - headers (dict; optional):
        自定义请求头.

    - method (a value equal to: 'get', 'post', 'put', 'patch', 'delete'; optional):
        请求类型，可选项有`'get'`、`'post'`、`'put'`、`'patch'`、`'delete'`
        默认值：`'get'`.

    - params (dict; optional):
        自定义请求参数.

    - responseType (a value equal to: 'json', 'text', 'document', 'stream', 'arraybuffer', 'blob'; optional):
        响应结果数据类型，可选项有`'json'`、`'text'`、`'document'`、`'stream'`、`'arraybuffer'`、`'blob'`
        默认值：`'json'`.

    - timeout (number; optional):
        请求超时时长，单位：毫秒，设置为`0`表示永不超时  默认值：`0`.

    - url (string; required):
        必填，请求目标url.

    - withCredentials (boolean; optional):
        跨域请求时是否需要使用凭证  默认值：`False`.

- responseResult (dict; optional):
    监听最近一次请求任务执行结果相关信息.

    `responseResult` is a dict with keys:

    - data (boolean | number | string | dict | list; optional):
        请求结果数据.

    - errorCode (string; optional):
        请求错误代码，仅任务失败时附带.

    - message (string; optional):
        请求错误描述，仅任务失败时附带.

    - requestURL (string; optional):
        请求地址.

    - status (number; optional):
        请求结果状态.

    - statusText (string; optional):
        请求结果状态描述.

    - timestamp (number; optional):
        请求任务完成时间戳.

- status (a value equal to: 'pending', 'idle'; optional):
    监听当前组件的状态，`'pending'`表示请求中，`'idle'`表示空闲状态."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyHttpRequests'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, requestConfig=Component.UNDEFINED, responseResult=Component.UNDEFINED, status=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'loading_state', 'requestConfig', 'responseResult', 'status']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'loading_state', 'requestConfig', 'responseResult', 'status']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyHttpRequests, self).__init__(**args)
