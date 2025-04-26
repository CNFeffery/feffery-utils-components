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


class FefferyHttpRequests(Component):
    """A FefferyHttpRequests component.
http请求组件FefferyHttpRequests

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- requestConfig (dict; optional):
    构造新发起http请求对应的参数，每次更新为有效值后会发起相应的请求，每次请求完成（成功或失败）后会自动重置为空值.

    `requestConfig` is a dict with keys:

    - method (a value equal to: 'get', 'post', 'put', 'patch', 'delete'; optional):
        请求类型，可选项有`'get'`、`'post'`、`'put'`、`'patch'`、`'delete'`
        默认值：`'get'`.

    - url (string; required):
        必填，请求目标url.

    - headers (dict; optional):
        自定义请求头.

    - params (dict; optional):
        自定义请求参数.

    - data (dict; optional):
        自定义请求体发送数据.

    - timeout (number; optional):
        请求超时时长，单位：毫秒，设置为`0`表示永不超时  默认值：`0`.

    - withCredentials (boolean; optional):
        跨域请求时是否需要使用凭证  默认值：`False`.

    - responseType (a value equal to: 'json', 'text', 'document', 'stream', 'arraybuffer', 'blob'; optional):
        响应结果数据类型，可选项有`'json'`、`'text'`、`'document'`、`'stream'`、`'arraybuffer'`、`'blob'`
        默认值：`'json'`.

- responseResult (dict; optional):
    监听最近一次请求任务执行结果相关信息.

    `responseResult` is a dict with keys:

    - status (number; optional):
        请求结果状态.

    - statusText (string; optional):
        请求结果状态描述.

    - data (boolean | number | string | dict | list; optional):
        请求结果数据.

    - requestURL (string; optional):
        请求地址.

    - timestamp (number; optional):
        请求任务完成时间戳.

    - errorCode (string; optional):
        请求错误代码，仅任务失败时附带.

    - message (string; optional):
        请求错误描述，仅任务失败时附带.

- status (a value equal to: 'pending', 'idle'; optional):
    监听当前组件的状态，`'pending'`表示请求中，`'idle'`表示空闲状态."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyHttpRequests'
    RequestConfig = TypedDict(
        "RequestConfig",
            {
            "method": NotRequired[Literal["get", "post", "put", "patch", "delete"]],
            "url": str,
            "headers": NotRequired[dict],
            "params": NotRequired[dict],
            "data": NotRequired[dict],
            "timeout": NotRequired[NumberType],
            "withCredentials": NotRequired[bool],
            "responseType": NotRequired[Literal["json", "text", "document", "stream", "arraybuffer", "blob"]]
        }
    )

    ResponseResult = TypedDict(
        "ResponseResult",
            {
            "status": NotRequired[NumberType],
            "statusText": NotRequired[str],
            "data": NotRequired[typing.Any],
            "requestURL": NotRequired[str],
            "timestamp": NotRequired[NumberType],
            "errorCode": NotRequired[str],
            "message": NotRequired[str]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        requestConfig: typing.Optional["RequestConfig"] = None,
        responseResult: typing.Optional["ResponseResult"] = None,
        status: typing.Optional[Literal["pending", "idle"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'requestConfig', 'responseResult', 'status']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'requestConfig', 'responseResult', 'status']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyHttpRequests, self).__init__(**args)

setattr(FefferyHttpRequests, "__init__", _explicitize_args(FefferyHttpRequests.__init__))
