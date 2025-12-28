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


class FefferyEventListener(Component):
    """A FefferyEventListener component.
通用事件监听组件FefferyEventListener

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- eventName (string | list of strings; required):
    必填，目标事件名称，也可传入多种事件名构成的数组.

- handler (string; optional):
    必填，自定义事件处理`js`函数字符串，唯一入参为事件对象，返回值将用于更新`result`属性.

- targetSelector (string; optional):
    事件监听目标对应的选择器字符串，默认监听目标为整个页面.

- enable (boolean; default True):
    控制是否开启监听  默认值：`True`.

- result (boolean | number | string | dict | list; optional):
    监听`handler`对应函数的返回值，作为事件监听的结果."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyEventListener'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        eventName: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        handler: typing.Optional[str] = None,
        targetSelector: typing.Optional[str] = None,
        enable: typing.Optional[bool] = None,
        result: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'eventName', 'handler', 'targetSelector', 'enable', 'result']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'eventName', 'handler', 'targetSelector', 'enable', 'result']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['eventName']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyEventListener, self).__init__(**args)

setattr(FefferyEventListener, "__init__", _explicitize_args(FefferyEventListener.__init__))
