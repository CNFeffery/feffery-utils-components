# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyListenDrop(Component):
    """A FefferyListenDrop component.
放置事件监听组件FefferyListenDrop

Keyword arguments:

- id (string; optional):
    组件id.

- dropEvent (dict; optional):
    监听最近一次基于FefferyListenDrag的元素拖拽放置事件.

    `dropEvent` is a dict with keys:

    - clientX (number; optional):
        以浏览器窗口左上角为原点，记录x坐标.

    - clientY (number; optional):
        以浏览器窗口左上角为原点，记录y坐标.

    - data (boolean | number | string | dict | list; optional):
        事件携带数据.

    - pageX (number; optional):
        以页面整体左上角为原点，记录x坐标.

    - pageY (number; optional):
        以页面整体左上角为原点，记录y坐标.

    - screenX (number; optional):
        以屏幕左上角为原点，记录x坐标.

    - screenY (number; optional):
        以屏幕左上角为原点，记录y坐标.

    - time (number; optional):
        事件对应时间戳.

- hoverEvent (dict; optional):
    监听最近一次正处于待放置鼠标悬停状态时的事件.

    `hoverEvent` is a dict with keys:

    - clientX (number; optional):
        以浏览器窗口左上角为原点，记录x坐标.

    - clientY (number; optional):
        以浏览器窗口左上角为原点，记录y坐标.

    - pageX (number; optional):
        以页面整体左上角为原点，记录x坐标.

    - pageY (number; optional):
        以页面整体左上角为原点，记录y坐标.

    - screenX (number; optional):
        以屏幕左上角为原点，记录x坐标.

    - screenY (number; optional):
        以屏幕左上角为原点，记录y坐标.

    - time (number; optional):
        事件对应时间戳.

- isHovering (boolean; optional):
    监听放置事件监听目标容器是否正处于待放置鼠标悬停状态.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- targetSelector (string; optional):
    放置事件监听目标容器选择器规则字符串."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyListenDrop'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, targetSelector=Component.UNDEFINED, dropEvent=Component.UNDEFINED, isHovering=Component.UNDEFINED, hoverEvent=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'dropEvent', 'hoverEvent', 'isHovering', 'loading_state', 'targetSelector']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'dropEvent', 'hoverEvent', 'isHovering', 'loading_state', 'targetSelector']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyListenDrop, self).__init__(**args)
