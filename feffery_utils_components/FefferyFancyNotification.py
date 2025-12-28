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


class FefferyFancyNotification(Component):
    """A FefferyFancyNotification component.
美观通知提示组件FefferyFancyNotification

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，设置内嵌元素内容.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- type (a value equal to: 'info', 'success', 'warning', 'error'; optional):
    设置信息类型，可选的有`'info'`、`'success'`、`'warning'`、`'error'`.

- visible (boolean; default True):
    主动设置是否可见  默认值：`False`.

- position (a value equal to: 'top-right', 'top-center', 'top-left', 'bottom-right', 'bottom-cente', 'bottom-left'; optional):
    设置通知提示弹出方位，可选的有`'top-right'`、`'top-center'`、`'top-left'`、`'bottom-right'`、`'bottom-cente'`、`'bottom-left'`
    默认值：`'top-right'`.

- autoClose (boolean | number; optional):
    配置自动关闭延时（单位：毫秒），当设置为`False`时不会自动关闭  默认值：`5000`.

- closable (boolean; default True):
    设置是否可关闭  默认值：`True`.

- hideProgressBar (boolean; optional):
    设置是否显示关闭倒计时进度条  默认值：`False`.

- pauseOnHover (boolean; optional):
    设置当鼠标悬浮于通知框上时，是否暂停倒计时  默认值：`True`.

- closeOnClick (boolean; optional):
    设置是否允许通知框在被点击后自动关闭  默认值：`True`.

- newestOnTop (boolean; optional):
    设置是否将新的通知框显示在更顶端的位置  默认值：`False`.

- toastClassName (string; optional):
    设置通知框的`css`类.

- bodyClassName (string; optional):
    设置通知框内容区的`css`类.

- progressClassName (string; optional):
    设置通知框进度条的`css`类.

- progressStyle (dict; optional):
    设置通知框进度条的`css`样式.

- draggable (boolean; optional):
    设置通知框是否可拖拽  默认值：`True`.

- draggablePercent (number; optional):
    设置通知框被拖拽距离占自身宽度的百分比阈值，拖拽距离超出此阈值时通知框会被关闭  默认值：`80`.

- containerId (string; optional):
    可选，设置局部目标容器的`id`.

- limit (number; optional):
    设置屏幕中允许同时显示的通知框数量上限，默认无上限.

- theme (a value equal to: 'light', 'dark', 'colored'; optional):
    设置主题，可选的有`'light'`、`'dark'`、`'colored'`  默认值：`'light'`."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyFancyNotification'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        type: typing.Optional[Literal["info", "success", "warning", "error"]] = None,
        visible: typing.Optional[bool] = None,
        position: typing.Optional[Literal["top-right", "top-center", "top-left", "bottom-right", "bottom-cente", "bottom-left"]] = None,
        autoClose: typing.Optional[typing.Union[bool, NumberType]] = None,
        closable: typing.Optional[bool] = None,
        hideProgressBar: typing.Optional[bool] = None,
        pauseOnHover: typing.Optional[bool] = None,
        closeOnClick: typing.Optional[bool] = None,
        newestOnTop: typing.Optional[bool] = None,
        toastClassName: typing.Optional[str] = None,
        bodyClassName: typing.Optional[str] = None,
        progressClassName: typing.Optional[str] = None,
        progressStyle: typing.Optional[dict] = None,
        draggable: typing.Optional[bool] = None,
        draggablePercent: typing.Optional[NumberType] = None,
        containerId: typing.Optional[str] = None,
        limit: typing.Optional[NumberType] = None,
        theme: typing.Optional[Literal["light", "dark", "colored"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'type', 'visible', 'position', 'autoClose', 'closable', 'hideProgressBar', 'pauseOnHover', 'closeOnClick', 'newestOnTop', 'toastClassName', 'bodyClassName', 'progressClassName', 'progressStyle', 'draggable', 'draggablePercent', 'containerId', 'limit', 'theme']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'type', 'visible', 'position', 'autoClose', 'closable', 'hideProgressBar', 'pauseOnHover', 'closeOnClick', 'newestOnTop', 'toastClassName', 'bodyClassName', 'progressClassName', 'progressStyle', 'draggable', 'draggablePercent', 'containerId', 'limit', 'theme']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyFancyNotification, self).__init__(children=children, **args)

setattr(FefferyFancyNotification, "__init__", _explicitize_args(FefferyFancyNotification.__init__))
