# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyListenDrop(Component):
    """A FefferyListenDrop component.
放置事件监听组件FefferyListenDrop

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- targetSelector (string; optional):
    放置事件监听目标容器选择器规则字符串.

- dropEvent (dict; optional):
    监听最近一次基于`FefferyListenDrag`的元素拖拽放置事件.

    `dropEvent` is a dict with keys:

    - time (number; optional):
        事件对应时间戳.

    - data (boolean | number | string | dict | list; optional):
        事件携带数据.

    - pageX (number; optional):
        以页面整体左上角为原点，记录`x`坐标.

    - pageY (number; optional):
        以页面整体左上角为原点，记录`y`坐标.

    - clientX (number; optional):
        以浏览器窗口左上角为原点，记录`x`坐标.

    - clientY (number; optional):
        以浏览器窗口左上角为原点，记录`y`坐标.

    - screenX (number; optional):
        以屏幕左上角为原点，记录`x`坐标.

    - screenY (number; optional):
        以屏幕左上角为原点，记录`y`坐标.

- isHovering (boolean; optional):
    监听放置事件监听目标容器是否正处于待放置鼠标悬停状态.

- hoverEvent (dict; optional):
    监听最近一次正处于待放置鼠标悬停状态时的事件.

    `hoverEvent` is a dict with keys:

    - time (number; optional):
        事件对应时间戳.

    - pageX (number; optional):
        以页面整体左上角为原点，记录`x`坐标.

    - pageY (number; optional):
        以页面整体左上角为原点，记录`y`坐标.

    - clientX (number; optional):
        以浏览器窗口左上角为原点，记录`x`坐标.

    - clientY (number; optional):
        以浏览器窗口左上角为原点，记录`y`坐标.

    - screenX (number; optional):
        以屏幕左上角为原点，记录`x`坐标.

    - screenY (number; optional):
        以屏幕左上角为原点，记录`y`坐标."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyListenDrop'
    DropEvent = TypedDict(
        "DropEvent",
            {
            "time": NotRequired[typing.Union[int, float, numbers.Number]],
            "data": NotRequired[typing.Any],
            "pageX": NotRequired[typing.Union[int, float, numbers.Number]],
            "pageY": NotRequired[typing.Union[int, float, numbers.Number]],
            "clientX": NotRequired[typing.Union[int, float, numbers.Number]],
            "clientY": NotRequired[typing.Union[int, float, numbers.Number]],
            "screenX": NotRequired[typing.Union[int, float, numbers.Number]],
            "screenY": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    HoverEvent = TypedDict(
        "HoverEvent",
            {
            "time": NotRequired[typing.Union[int, float, numbers.Number]],
            "pageX": NotRequired[typing.Union[int, float, numbers.Number]],
            "pageY": NotRequired[typing.Union[int, float, numbers.Number]],
            "clientX": NotRequired[typing.Union[int, float, numbers.Number]],
            "clientY": NotRequired[typing.Union[int, float, numbers.Number]],
            "screenX": NotRequired[typing.Union[int, float, numbers.Number]],
            "screenY": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        targetSelector: typing.Optional[str] = None,
        dropEvent: typing.Optional["DropEvent"] = None,
        isHovering: typing.Optional[bool] = None,
        hoverEvent: typing.Optional["HoverEvent"] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'targetSelector', 'dropEvent', 'isHovering', 'hoverEvent']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'targetSelector', 'dropEvent', 'isHovering', 'hoverEvent']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyListenDrop, self).__init__(**args)
