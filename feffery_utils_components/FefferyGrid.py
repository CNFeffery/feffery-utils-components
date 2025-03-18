# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyGrid(Component):
    """A FefferyGrid component.
可拖拽网格组件FefferyGrid

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    传入内部的各`FefferyGridItem`组件.

- className (string; optional):
    当前组件css类名.

- placeholder (a list of or a singular dash component, string or number; optional):
    组件型，占位元素，用于在`children`为空时呈现相关提示信息.

- height (number; optional):
    网格容器固定像素高度.

- autoSize (boolean; default True):
    当前网格容器是否受内部元素影响调整高度  默认值：`True`.

- compactType (a value equal to: 'vertical', 'horizontal'; default 'vertical'):
    网格项自动调整约束方向，可选项有`'vertical'`、`'horizontal'`  默认值：`'vertical'`.

- margin (list of numbers | dict with strings as keys and values of type list of numbers; default [10, 10]):
    网格容器内子元素之间的像素间距，格式：`[水平间距, 竖直间距]`，也可以传入以断点为键的字典从而实现响应式  默认值：`[10,
    10]`.

- containerPadding (list of numbers | dict with strings as keys and values of type list of numbers; optional):
    用于设置当前网格容器内部像素padding，格式：[x, y]，支持响应式.

- rowHeight (number; default 150):
    网格中每行像素高度  默认值：`150`.

- closable (boolean; default False):
    内部网格项是否可关闭  默认值：`False`.

- closeEvent (dict; optional):
    监听最近一次内部网格项关闭事件.

    `closeEvent` is a dict with keys:

    - key (string; optional):
        对应网格项`key`值.

    - timestamp (number; optional):
        事件时间戳.

- autoClose (boolean; default False):
    是否在内部网格项关闭触发时进行自动关闭  默认值：`False`.

- isDraggable (boolean; default True):
    内部网格项是否可拖拽  默认值：`True`.

- draggerStyle (dict; optional):
    网格项拖拽控件额外css样式.

- draggerClassName (string; optional):
    网格项拖拽控件额外css类名.

- isResizable (boolean; default True):
    内部网格项尺寸是否可调整  默认值：`True`.

- isBounded (boolean; default False):
    是否允许内部网格项拖拽出界  默认值：`False`.

- allowOverlap (boolean; default False):
    是否允许内部网格项重叠  默认值：`False`.

- breakpoints (dict with strings as keys and values of type number; default { lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0 }):
    自定义断点键及对应断点像素宽度值  默认值：`{lg: 1200, md: 996, sm: 768, xs: 480, xxs:
    0}`.

- cols (dict with strings as keys and values of type number | number; default 12):
    与`breakpoints`对应，设置不同断点下网格系统的列数  默认值：`12`.

- layouts (dict; optional):
    配置各网格项.

    `layouts` is a dict with strings as keys and values of type list
    of dicts with keys:

    - i (string; optional):
        对应当前网格项的`key`值.

    - x (number; optional):
        对应当前网格项的锚点`x`单位坐标.

    - y (number; optional):
        对应当前网格项的锚点`y`单位坐标.

    - w (number; optional):
        对应当前网格项的网格单位宽度.

    - h (number; optional):
        对应当前网格项的网格单位高度.

    - minW (number; optional):
        对应当前网格项的最小网格单位宽度  默认值：`0`.

    - maxW (number; optional):
        对应当前网格项的最大网格单位宽度，默认无限制.

    - minH (number; optional):
        对应当前网格项的最小网格单位高度  默认值：`0`.

    - maxH (number; optional):
        对应当前网格项的最大网格单位高度，默认无限制.

    - static (boolean; optional):
        设置当前网格项是否静态  默认值：`False`.

    - isDraggable (boolean; optional):
        设置当前网格项是否允许被拖拽  默认值：`True`.

    - isResizable (boolean; optional):
        设置当前网格项是否允许被调整尺寸  默认值：`True`.

    - isBounded (boolean; optional):
        设置是否为当前网格项施加边界约束  默认值：`False`. | list of dicts with keys:

    - i (string; optional):
        对应当前网格项的`key`值.

    - x (number; optional):
        对应当前网格项的锚点`x`单位坐标.

    - y (number; optional):
        对应当前网格项的锚点`y`单位坐标.

    - w (number; optional):
        对应当前网格项的网格单位宽度.

    - h (number; optional):
        对应当前网格项的网格单位高度.

    - minW (number; optional):
        对应当前网格项的最小网格单位宽度  默认值：`0`.

    - maxW (number; optional):
        对应当前网格项的最大网格单位宽度，默认无限制.

    - minH (number; optional):
        对应当前网格项的最小网格单位高度  默认值：`0`.

    - maxH (number; optional):
        对应当前网格项的最大网格单位高度，默认无限制.

    - static (boolean; optional):
        设置当前网格项是否静态  默认值：`False`.

    - isDraggable (boolean; optional):
        设置当前网格项是否允许被拖拽  默认值：`True`.

    - isResizable (boolean; optional):
        设置当前网格项是否允许被调整尺寸  默认值：`True`.

    - isBounded (boolean; optional):
        设置是否为当前网格项施加边界约束  默认值：`False`. | boolean | number | string | dict | list

- placeholderBackground (string; default '#3b3a39'):
    拖拽预览占位对应`css`的`background`属性  默认值：`'#3b3a39'`.

- placeholderOpacity (number; default 0.2):
    拖拽预览占位对应`css`的`opacity`属性  默认值：`0.2`.

- placeholderBorder (string; default 'none'):
    拖拽预览占位对应`css`的`border`属性  默认值：`'none'`.

- placeholderBorderRadius (string; default '0px'):
    拖拽预览占位对应`css`的`border-radius`属性  默认值：`'0px'`.

- debug (boolean; default False):
    是否开启调试模式，开启后，每次布局参数更新，都会在浏览器开发者工具控制台打印相关参数  默认值：`False`."""
    _children_props = ['placeholder']
    _base_nodes = ['placeholder', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyGrid'
    CloseEvent = TypedDict(
        "CloseEvent",
            {
            "key": NotRequired[str],
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    Layouts = TypedDict(
        "Layouts",
            {
            "i": NotRequired[str],
            "x": NotRequired[typing.Union[int, float, numbers.Number]],
            "y": NotRequired[typing.Union[int, float, numbers.Number]],
            "w": NotRequired[typing.Union[int, float, numbers.Number]],
            "h": NotRequired[typing.Union[int, float, numbers.Number]],
            "minW": NotRequired[typing.Union[int, float, numbers.Number]],
            "maxW": NotRequired[typing.Union[int, float, numbers.Number]],
            "minH": NotRequired[typing.Union[int, float, numbers.Number]],
            "maxH": NotRequired[typing.Union[int, float, numbers.Number]],
            "static": NotRequired[bool],
            "isDraggable": NotRequired[bool],
            "isResizable": NotRequired[bool],
            "isBounded": NotRequired[bool]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        placeholder: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        height: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        autoSize: typing.Optional[bool] = None,
        compactType: typing.Optional[Literal["vertical", "horizontal"]] = None,
        margin: typing.Optional[typing.Union[typing.Sequence[typing.Union[int, float, numbers.Number]], typing.Dict[typing.Union[str, float, int], typing.Sequence[typing.Union[int, float, numbers.Number]]]]] = None,
        containerPadding: typing.Optional[typing.Union[typing.Sequence[typing.Union[int, float, numbers.Number]], typing.Dict[typing.Union[str, float, int], typing.Sequence[typing.Union[int, float, numbers.Number]]]]] = None,
        rowHeight: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        closable: typing.Optional[bool] = None,
        closeEvent: typing.Optional["CloseEvent"] = None,
        autoClose: typing.Optional[bool] = None,
        isDraggable: typing.Optional[bool] = None,
        draggerStyle: typing.Optional[dict] = None,
        draggerClassName: typing.Optional[str] = None,
        isResizable: typing.Optional[bool] = None,
        isBounded: typing.Optional[bool] = None,
        allowOverlap: typing.Optional[bool] = None,
        breakpoints: typing.Optional[typing.Dict[typing.Union[str, float, int], typing.Union[int, float, numbers.Number]]] = None,
        cols: typing.Optional[typing.Union[typing.Dict[typing.Union[str, float, int], typing.Union[int, float, numbers.Number]], typing.Union[int, float, numbers.Number]]] = None,
        layouts: typing.Optional[typing.Union[typing.Dict[typing.Union[str, float, int], typing.Sequence["Layouts"]], typing.Sequence["Layouts"], typing.Any]] = None,
        placeholderBackground: typing.Optional[str] = None,
        placeholderOpacity: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        placeholderBorder: typing.Optional[str] = None,
        placeholderBorderRadius: typing.Optional[str] = None,
        debug: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'placeholder', 'height', 'autoSize', 'compactType', 'margin', 'containerPadding', 'rowHeight', 'closable', 'closeEvent', 'autoClose', 'isDraggable', 'draggerStyle', 'draggerClassName', 'isResizable', 'isBounded', 'allowOverlap', 'breakpoints', 'cols', 'layouts', 'placeholderBackground', 'placeholderOpacity', 'placeholderBorder', 'placeholderBorderRadius', 'debug']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'placeholder', 'height', 'autoSize', 'compactType', 'margin', 'containerPadding', 'rowHeight', 'closable', 'closeEvent', 'autoClose', 'isDraggable', 'draggerStyle', 'draggerClassName', 'isResizable', 'isBounded', 'allowOverlap', 'breakpoints', 'cols', 'layouts', 'placeholderBackground', 'placeholderOpacity', 'placeholderBorder', 'placeholderBorderRadius', 'debug']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyGrid, self).__init__(children=children, **args)
