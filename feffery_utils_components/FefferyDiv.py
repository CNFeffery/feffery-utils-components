# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyDiv(Component):
    """A FefferyDiv component.
进阶div容器组件FefferyDiv

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，内嵌元素.

- style (dict; optional):
    当前组件css样式.

- className (string | dict; optional):
    当前组件css类名.

- enableEvents (list of a value equal to: 'click', 'dbclick', 'size', 'mouseenter', 'mouseleave', 'contextmenu', 'hover', 'touch', 'clickaway', 'position', 'focus', 'paste's; default ['click', 'dbclick']):
    控制要开启的事件监听类型数组，可选项有`'click'`（单击事件）、`'dbclick'`（双击事件）、`'size'`（尺寸变化事件）、
    `'mouseenter'`（鼠标移入事件），`'mouseleave'`（鼠标移出事件）、`'contextmenu'`（鼠标右键点击事件）、
    `'hover'`（鼠标悬停事件）、`'touch'`（移动端触碰事件）、`'clickaway'`（元素外点击事件）、`'position'`（左上角坐标位置变化事件）、
    `'focus'`（聚焦状态切换事件）、`'paste'`（文本粘贴事件）  默认值：`['click', 'dbclick']`.

- _width (number; optional):
    监听容器当前像素宽度值.

- _height (number; optional):
    监听容器当前像素高度值.

- debounceWait (number; default 150):
    尺寸变化事件监听属性的防抖等待时间，单位：毫秒  默认值：`150`.

- mouseEnterCount (number; default 0):
    监听鼠标移入事件累计次数  默认值：`0`.

- mouseLeaveCount (number; default 0):
    监听鼠标移出事件累计次数  默认值：`0`.

- nClicks (number; default 0):
    监听单击事件累计次数  默认值：`0`.

- clickEvent (dict; optional):
    监听单击事件对应详细参数.

    `clickEvent` is a dict with keys:

    - pageX (number; optional):
        以页面整体左上角为原点，记录x坐标.

    - pageY (number; optional):
        以页面整体左上角为原点，记录y坐标.

    - clientX (number; optional):
        以浏览器窗口左上角为原点，记录x坐标.

    - clientY (number; optional):
        以浏览器窗口左上角为原点，记录y坐标.

    - screenX (number; optional):
        以屏幕左上角为原点，记录x坐标.

    - screenY (number; optional):
        以屏幕左上角为原点，记录y坐标.

    - timestamp (number; optional):
        点击事件对应的时间戳.

- nDoubleClicks (number; default 0):
    监听双击事件累计次数  默认值：`0`.

- doubleClickEvent (dict; optional):
    监听双击事件对应详细参数.

    `doubleClickEvent` is a dict with keys:

    - pageX (number; optional):
        以页面整体左上角为原点，记录x坐标.

    - pageY (number; optional):
        以页面整体左上角为原点，记录y坐标.

    - clientX (number; optional):
        以浏览器窗口左上角为原点，记录x坐标.

    - clientY (number; optional):
        以浏览器窗口左上角为原点，记录y坐标.

    - screenX (number; optional):
        以屏幕左上角为原点，记录x坐标.

    - screenY (number; optional):
        以屏幕左上角为原点，记录y坐标.

    - timestamp (number; optional):
        点击事件对应的时间戳.

- enableListenContextMenu (boolean; default False):
    是否针对当前组件监听右键点击事件，开启后会强制阻止当前组件内的默认右键菜单弹出行为  默认值：`False`.

- contextMenuEvent (dict; optional):
    监听鼠标右键点击事件对应详细参数.

    `contextMenuEvent` is a dict with keys:

    - pageX (number; optional):
        以页面整体左上角为原点，记录x坐标.

    - pageY (number; optional):
        以页面整体左上角为原点，记录y坐标.

    - clientX (number; optional):
        以浏览器窗口左上角为原点，记录x坐标.

    - clientY (number; optional):
        以浏览器窗口左上角为原点，记录y坐标.

    - screenX (number; optional):
        以屏幕左上角为原点，记录x坐标.

    - screenY (number; optional):
        以屏幕左上角为原点，记录y坐标.

    - timestamp (number; optional):
        点击事件对应的时间戳.

- isHovering (boolean; optional):
    监听当前元素是否正处于鼠标悬停状态.

- isTouching (boolean; optional):
    针对移动端场景，监听当前元素是否处于触摸状态.

- enableClickAway (boolean; default False):
    是否启用元素外点击事件监听  默认值：`False`.

- clickAwayCount (number; default 0):
    监听当前元素外部点击事件累计次数  默认值：`0`.

- position (dict; optional):
    监听当前元素左上角在视口中的坐标位置.

    `position` is a dict with keys:

    - x (number; optional):
        以页面整体左上角为原点，记录x坐标.

    - y (number; optional):
        以页面整体左上角为原点，记录y坐标.

- enableFocus (boolean; default False):
    是否启用聚焦状态监听功能  默认值：`False`.

- isFocused (boolean; optional):
    监听或设置当前元素是否聚焦中.

- pasteEvent (dict; optional):
    监听文本粘贴事件.

    `pasteEvent` is a dict with keys:

    - text (string; optional):
        已粘贴文本内容.

    - timestamp (number; optional):
        粘贴事件对应的时间戳.

- wheelEventStrategy (a value equal to: 'default', 'internally-only'; default 'default'):
    设置当前组件内部处理鼠标滑轮事件的策略，可选项有`'default'`、`'internally-only'`（不向外传递）
    默认值：`'default'.

- shadow (a value equal to: 'no-shadow', 'hover-shadow', 'always-shadow', 'hover-shadow-light', 'always-shadow-light'; default 'no-shadow'):
    为当前组件快捷设置内置阴影效果，可选项有`'no-shadow'`、`'hover-shadow'`、`'always-shadow'`、`'hover-shadow-light'`、`'always-shadow-light'`
    默认值：`'no-shadow'`.

- scrollbar (a value equal to: 'default', 'simple', 'hidden'; default 'default'):
    为当前组件快捷设置内置滚动条效果，可选项有`'default'`、`'simple'`、`'hidden'`
    默认值：`'default'.

- textAlign (a value equal to: 'left', 'center', 'right'; optional):
    当前组件`css`对应`text-align`属性快捷设置.

- justify (string; optional):
    针对flex布局的`justify-content`属性快捷设置，传入有效值后会自动开启flex布局.

- align (string; optional):
    针对flex布局的`align-items`快捷设置，传入有效值后会自动开启flex布局.

- padding (string | number; optional):
    `css`对应`padding`属性快捷设置.

- margin (string | number; optional):
    `css`对应`margin`属性快捷设置.

- border (string; optional):
    `css`对应`border`属性快捷设置.

- borderRadius (string | number; optional):
    `css`对应`border-radius`属性快捷设置.

- printNow (boolean; optional):
    是否立即执行打印功能调用，每次设置为`True`触发打印后都会重置为`False`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDiv'
    ClickEvent = TypedDict(
        "ClickEvent",
            {
            "pageX": NotRequired[typing.Union[int, float, numbers.Number]],
            "pageY": NotRequired[typing.Union[int, float, numbers.Number]],
            "clientX": NotRequired[typing.Union[int, float, numbers.Number]],
            "clientY": NotRequired[typing.Union[int, float, numbers.Number]],
            "screenX": NotRequired[typing.Union[int, float, numbers.Number]],
            "screenY": NotRequired[typing.Union[int, float, numbers.Number]],
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    DoubleClickEvent = TypedDict(
        "DoubleClickEvent",
            {
            "pageX": NotRequired[typing.Union[int, float, numbers.Number]],
            "pageY": NotRequired[typing.Union[int, float, numbers.Number]],
            "clientX": NotRequired[typing.Union[int, float, numbers.Number]],
            "clientY": NotRequired[typing.Union[int, float, numbers.Number]],
            "screenX": NotRequired[typing.Union[int, float, numbers.Number]],
            "screenY": NotRequired[typing.Union[int, float, numbers.Number]],
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    ContextMenuEvent = TypedDict(
        "ContextMenuEvent",
            {
            "pageX": NotRequired[typing.Union[int, float, numbers.Number]],
            "pageY": NotRequired[typing.Union[int, float, numbers.Number]],
            "clientX": NotRequired[typing.Union[int, float, numbers.Number]],
            "clientY": NotRequired[typing.Union[int, float, numbers.Number]],
            "screenX": NotRequired[typing.Union[int, float, numbers.Number]],
            "screenY": NotRequired[typing.Union[int, float, numbers.Number]],
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    Position = TypedDict(
        "Position",
            {
            "x": NotRequired[typing.Union[int, float, numbers.Number]],
            "y": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    PasteEvent = TypedDict(
        "PasteEvent",
            {
            "text": NotRequired[str],
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        enableEvents: typing.Optional[typing.Sequence[Literal["click", "dbclick", "size", "mouseenter", "mouseleave", "contextmenu", "hover", "touch", "clickaway", "position", "focus", "paste"]]] = None,
        _width: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        _height: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        debounceWait: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        mouseEnterCount: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        mouseLeaveCount: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        nClicks: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        clickEvent: typing.Optional["ClickEvent"] = None,
        nDoubleClicks: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        doubleClickEvent: typing.Optional["DoubleClickEvent"] = None,
        enableListenContextMenu: typing.Optional[bool] = None,
        contextMenuEvent: typing.Optional["ContextMenuEvent"] = None,
        isHovering: typing.Optional[bool] = None,
        isTouching: typing.Optional[bool] = None,
        enableClickAway: typing.Optional[bool] = None,
        clickAwayCount: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        position: typing.Optional["Position"] = None,
        enableFocus: typing.Optional[bool] = None,
        isFocused: typing.Optional[bool] = None,
        pasteEvent: typing.Optional["PasteEvent"] = None,
        wheelEventStrategy: typing.Optional[Literal["default", "internally-only"]] = None,
        shadow: typing.Optional[Literal["no-shadow", "hover-shadow", "always-shadow", "hover-shadow-light", "always-shadow-light"]] = None,
        scrollbar: typing.Optional[Literal["default", "simple", "hidden"]] = None,
        textAlign: typing.Optional[Literal["left", "center", "right"]] = None,
        justify: typing.Optional[str] = None,
        align: typing.Optional[str] = None,
        padding: typing.Optional[typing.Union[str, typing.Union[int, float, numbers.Number]]] = None,
        margin: typing.Optional[typing.Union[str, typing.Union[int, float, numbers.Number]]] = None,
        border: typing.Optional[str] = None,
        borderRadius: typing.Optional[typing.Union[str, typing.Union[int, float, numbers.Number]]] = None,
        printNow: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'enableEvents', '_width', '_height', 'debounceWait', 'mouseEnterCount', 'mouseLeaveCount', 'nClicks', 'clickEvent', 'nDoubleClicks', 'doubleClickEvent', 'enableListenContextMenu', 'contextMenuEvent', 'isHovering', 'isTouching', 'enableClickAway', 'clickAwayCount', 'position', 'enableFocus', 'isFocused', 'pasteEvent', 'wheelEventStrategy', 'shadow', 'scrollbar', 'textAlign', 'justify', 'align', 'padding', 'margin', 'border', 'borderRadius', 'printNow']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'enableEvents', '_width', '_height', 'debounceWait', 'mouseEnterCount', 'mouseLeaveCount', 'nClicks', 'clickEvent', 'nDoubleClicks', 'doubleClickEvent', 'enableListenContextMenu', 'contextMenuEvent', 'isHovering', 'isTouching', 'enableClickAway', 'clickAwayCount', 'position', 'enableFocus', 'isFocused', 'pasteEvent', 'wheelEventStrategy', 'shadow', 'scrollbar', 'textAlign', 'justify', 'align', 'padding', 'margin', 'border', 'borderRadius', 'printNow']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyDiv, self).__init__(children=children, **args)
