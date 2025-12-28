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


class FefferyTopProgress(Component):
    """A FefferyTopProgress component.
顶端加载进度条组件FefferyTopProgress

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，内嵌元素.

- className (string; optional):
    当前组件css类名.

- spinning (boolean; optional):
    是否处于加载中状态.

- minimum (number; optional):
    顶端进度条初始进度值，取值在`0.33`到`1`之间  默认值：`0.33`.

- easing (string; optional):
    对应设置`css`中的`easing`属性  默认值：`'ease'`.

- speed (number; optional):
    进度条每步递增耗时，单位：毫秒  默认值：`200`.

- showSpinner (boolean; optional):
    是否在右上角渲染圆圈加载动画  默认值：`True`.

- debug (boolean; default False):
    是否开启debug模式，开启后，每次动画加载都会在开发者工具的控制台打印相关`prop`信息  默认值：`False`.

- listenPropsMode (a value equal to: 'default', 'exclude', 'include'; default 'default'):
    监听模式，可选项有`'default'`、`'exclude'`、`'include'`  默认值：`'default'`.

- excludeProps (list of strings; optional):
    `listenPropsMode='exclude'`时，设置需要排除监听的回调目标列表，格式如`['组件id1.组件属性1',
    '组件id2.组件属性2', ...]`.

- includeProps (list of strings; optional):
    `listenPropsMode='include'`时，设置需要包含监听的回调目标列表，格式如`['组件id1.组件属性1',
    '组件id2.组件属性2', ...]`.

- color (string; default '#29d'):
    顶部进度条色彩  默认值：`'#29d'`.

- zIndex (number; default 99999):
    顶部进度条`z-index`值  默认值：`99999`.

- manual (boolean; default False):
    是否开启手动控制模式，开启后是否处于加载状态将由`spinning`参数控制，与内部元素参与的回调状态无关
    默认值：`False`."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyTopProgress'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        spinning: typing.Optional[bool] = None,
        minimum: typing.Optional[NumberType] = None,
        easing: typing.Optional[str] = None,
        speed: typing.Optional[NumberType] = None,
        showSpinner: typing.Optional[bool] = None,
        debug: typing.Optional[bool] = None,
        listenPropsMode: typing.Optional[Literal["default", "exclude", "include"]] = None,
        excludeProps: typing.Optional[typing.Sequence[str]] = None,
        includeProps: typing.Optional[typing.Sequence[str]] = None,
        color: typing.Optional[str] = None,
        zIndex: typing.Optional[NumberType] = None,
        manual: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'spinning', 'minimum', 'easing', 'speed', 'showSpinner', 'debug', 'listenPropsMode', 'excludeProps', 'includeProps', 'color', 'zIndex', 'manual']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'spinning', 'minimum', 'easing', 'speed', 'showSpinner', 'debug', 'listenPropsMode', 'excludeProps', 'includeProps', 'color', 'zIndex', 'manual']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyTopProgress, self).__init__(children=children, **args)

setattr(FefferyTopProgress, "__init__", _explicitize_args(FefferyTopProgress.__init__))
