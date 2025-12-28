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


class FefferyTiltHover(Component):
    """A FefferyTiltHover component.
倾斜悬浮组件FefferyTiltHover

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，要进行倾斜悬浮效果编排的目标元素.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- tiltEnable (boolean; default True):
    设置是否启用倾斜效果  默认为`True`.

- tiltReverse (boolean; default False):
    设置是否反转倾斜方向  默认为`False`.

- tiltAngleXInitial (number; default 0):
    设置x轴上的初始倾斜值（度）  默认为`0`.

- tiltAngleYInitial (number; default 0):
    设置y轴上的初始倾斜值（度）  默认为`0`.

- tiltMaxAngleX (number; default 20):
    设置x轴上的的最大倾斜旋转（度），范围为`0`到`90`  默认为`20`.

- tiltMaxAngleY (number; default 20):
    设置y轴上的最大倾斜旋转（度），范围为`0`到`90`  默认为`20`.

- tiltAxis (a value equal to: 'x', 'y'; default undefined):
    启用单轴倾斜，可选值为`'x'`或`'y'`.

- tiltAngleXManual (number; optional):
    设置在x轴上手动倾斜旋转（度）.

- tiltAngleYManual (number; optional):
    设置在y轴上手动倾斜旋转（度）.

- glareEnable (boolean; default False):
    设置是否启用眩光效果  默认为`False`.

- glareMaxOpacity (number; default 0.7):
    设置最大眩光不透明度，范围`0`到`1`  默认为`0.7`.

- glareColor (string; default '#ffffff'):
    设置眩光效果的颜色  默认为`'#ffffff'`.

- glareBorderRadius (string; default '0'):
    设置眩光效果的边框半径，接受任何标准的`CSS`边框半径。如果眩光颜色与页面颜色不同，则很有用  默认为`'0'`.

- glarePosition (a value equal to: 'top', 'right', 'bottom', 'left', 'all'; default 'bottom'):
    设置眩光效果的位置，可选的值为`'top'`、`'right'`、`'bottom'`、`'left'`、`'all'`
    默认为`'bottom'`.

- glareReverse (boolean; default False):
    设置是否反转眩光方向  默认为`False`.

- scale (number; default 1):
    设置组件的比例（`1.5 = 150%`，`2 = 200%`，等）  默认为`1`.

- perspective (number; default 1000):
    定义对象（包装/子组件）与用户的距离。越低，倾斜度越大  默认为`1000`.

- flipVertically (boolean; default False):
    设置是否启用组件的垂直翻转  默认为`False`.

- flipHorizontally (boolean; default False):
    设置是否启用组件的水平翻转  默认为`False`.

- reset (boolean; default True):
    设置是否必须在事件中重置效果  默认为`True`.

- transitionEasing (string; default 'cubic-bezier(.03,.98,.52,.99)'):
    设置在操作组件时过渡效果  默认为`'cubic-bezier(.03,.98,.52,.99)'`.

- transitionSpeed (number; default 400):
    设置在操作组件时的过渡速度  默认为`400`.

- trackOnWindow (boolean; default False):
    设置是否跟踪整个窗口上的鼠标和触摸事件  默认为`False`.

- gyroscope (boolean; default False):
    设置是否启用设备方向检测  默认为`False`.

- listenMove (dict; optional):
    监听用户在组件上移动时触发的事件数据.

- listenEnter (dict; optional):
    监听用户进入组件时触发的事件数据.

- listenLeave (dict; optional):
    监听用户离开组件时触发的事件数据."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyTiltHover'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        tiltEnable: typing.Optional[bool] = None,
        tiltReverse: typing.Optional[bool] = None,
        tiltAngleXInitial: typing.Optional[NumberType] = None,
        tiltAngleYInitial: typing.Optional[NumberType] = None,
        tiltMaxAngleX: typing.Optional[NumberType] = None,
        tiltMaxAngleY: typing.Optional[NumberType] = None,
        tiltAxis: typing.Optional[Literal["x", "y"]] = None,
        tiltAngleXManual: typing.Optional[NumberType] = None,
        tiltAngleYManual: typing.Optional[NumberType] = None,
        glareEnable: typing.Optional[bool] = None,
        glareMaxOpacity: typing.Optional[NumberType] = None,
        glareColor: typing.Optional[str] = None,
        glareBorderRadius: typing.Optional[str] = None,
        glarePosition: typing.Optional[Literal["top", "right", "bottom", "left", "all"]] = None,
        glareReverse: typing.Optional[bool] = None,
        scale: typing.Optional[NumberType] = None,
        perspective: typing.Optional[NumberType] = None,
        flipVertically: typing.Optional[bool] = None,
        flipHorizontally: typing.Optional[bool] = None,
        reset: typing.Optional[bool] = None,
        transitionEasing: typing.Optional[str] = None,
        transitionSpeed: typing.Optional[NumberType] = None,
        trackOnWindow: typing.Optional[bool] = None,
        gyroscope: typing.Optional[bool] = None,
        listenMove: typing.Optional[dict] = None,
        listenEnter: typing.Optional[dict] = None,
        listenLeave: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'tiltEnable', 'tiltReverse', 'tiltAngleXInitial', 'tiltAngleYInitial', 'tiltMaxAngleX', 'tiltMaxAngleY', 'tiltAxis', 'tiltAngleXManual', 'tiltAngleYManual', 'glareEnable', 'glareMaxOpacity', 'glareColor', 'glareBorderRadius', 'glarePosition', 'glareReverse', 'scale', 'perspective', 'flipVertically', 'flipHorizontally', 'reset', 'transitionEasing', 'transitionSpeed', 'trackOnWindow', 'gyroscope', 'listenMove', 'listenEnter', 'listenLeave']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'tiltEnable', 'tiltReverse', 'tiltAngleXInitial', 'tiltAngleYInitial', 'tiltMaxAngleX', 'tiltMaxAngleY', 'tiltAxis', 'tiltAngleXManual', 'tiltAngleYManual', 'glareEnable', 'glareMaxOpacity', 'glareColor', 'glareBorderRadius', 'glarePosition', 'glareReverse', 'scale', 'perspective', 'flipVertically', 'flipHorizontally', 'reset', 'transitionEasing', 'transitionSpeed', 'trackOnWindow', 'gyroscope', 'listenMove', 'listenEnter', 'listenLeave']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyTiltHover, self).__init__(children=children, **args)

setattr(FefferyTiltHover, "__init__", _explicitize_args(FefferyTiltHover.__init__))
