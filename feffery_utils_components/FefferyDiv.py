# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyDiv(Component):
    """A FefferyDiv component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    组件子元素.

- id (string; optional):
    组件id.

- _height (number; optional):
    监听容器像素高度变化.

- _width (number; optional):
    监听容器像素宽度变化.

- align (string; optional):
    针对flex布局的align-items快捷设置  传入有效值后会自动开启flex布局.

- border (string; optional):
    border快捷设置.

- borderRadius (string | number; optional):
    border-radius快捷设置.

- className (string | dict; optional):
    css类名.

- clickAwayCount (number; default 0):
    监听元素外点击事件发生次数，默认为0.

- contextMenuEvent (dict; optional):
    监听右键事件.

    `contextMenuEvent` is a dict with keys:

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

    - timestamp (number; optional):
        点击事件对应的时间戳.

- debounceWait (number; default 150):
    设置针对尺寸变化事件的防抖等待时间（单位：毫秒），默认为150.

- enableClickAway (boolean; default False):
    设置是否启用元素外点击事件监听，当页面中有大量FefferyDiv元素时，建议不要开启此特性，会导致明显的性能问题
    默认为False.

- enableFocus (boolean; default False):
    是否启用聚焦状态监听功能  默认：False.

- enableListenContextMenu (boolean; default False):
    设置是否针对当前div监听右键点击事件，开启后会强制关闭当前div内的默认右键菜单弹出  默认为False.

- isFocused (boolean; optional):
    监听或设置当前元素是否聚焦.

- isHovering (boolean; optional):
    监听当前元素是否被鼠标悬浮.

- justify (string; optional):
    针对flex布局的justify-content快捷设置  传入有效值后会自动开启flex布局.

- key (string; optional):
    强制刷新用.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- margin (string | number; optional):
    margin快捷设置.

- mouseEnterCount (number; default 0):
    监听鼠标移入事件次数，初始化为0.

- mouseLeaveCount (number; default 0):
    监听鼠标移出事件次数，初始化为0.

- nClicks (number; default 0):
    监听单击事件次数，初始化为0.

- nDoubleClicks (number; default 0):
    监听双击事件次数，初始化为0.

- padding (string | number; optional):
    padding快捷设置.

- position (dict; optional):
    监听当前元素左上角在视口中的坐标位置.

    `position` is a dict with keys:

    - x (number; optional):
        以页面整体左上角为原点，记录x坐标.

    - y (number; optional):
        以页面整体左上角为原点，记录y坐标.

- scrollbar (a value equal to: 'default', 'simple', 'hidden'; default 'default'):
    设置当前容器的快捷滚动条美化效果，可选的有'default'、'simple'、'hidden'.

- shadow (a value equal to: 'no-shadow', 'hover-shadow', 'always-shadow', 'hover-shadow-light', 'always-shadow-light'; default 'no-shadow'):
    设置当前容器的快捷阴影效果，可选的有'no-shadow'、'hover-shadow'、'always-shadow'
    默认为'no-shadow'.

- style (dict; optional):
    自定义css字典.

- textAlign (a value equal to: 'left', 'center', 'right'; optional):
    text-align快捷设置.

- wheelEventStrategy (a value equal to: 'default', 'internally-only'; default 'default'):
    设置当前div内部处理鼠标滑轮事件的策略  可选的有'default'、'internally-only'（不向外传递）
    默认：'default'."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDiv'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, _width=Component.UNDEFINED, _height=Component.UNDEFINED, debounceWait=Component.UNDEFINED, mouseEnterCount=Component.UNDEFINED, mouseLeaveCount=Component.UNDEFINED, nClicks=Component.UNDEFINED, nDoubleClicks=Component.UNDEFINED, enableListenContextMenu=Component.UNDEFINED, contextMenuEvent=Component.UNDEFINED, isHovering=Component.UNDEFINED, enableClickAway=Component.UNDEFINED, clickAwayCount=Component.UNDEFINED, position=Component.UNDEFINED, enableFocus=Component.UNDEFINED, isFocused=Component.UNDEFINED, wheelEventStrategy=Component.UNDEFINED, shadow=Component.UNDEFINED, scrollbar=Component.UNDEFINED, textAlign=Component.UNDEFINED, justify=Component.UNDEFINED, align=Component.UNDEFINED, padding=Component.UNDEFINED, margin=Component.UNDEFINED, border=Component.UNDEFINED, borderRadius=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', '_height', '_width', 'align', 'border', 'borderRadius', 'className', 'clickAwayCount', 'contextMenuEvent', 'debounceWait', 'enableClickAway', 'enableFocus', 'enableListenContextMenu', 'isFocused', 'isHovering', 'justify', 'key', 'loading_state', 'margin', 'mouseEnterCount', 'mouseLeaveCount', 'nClicks', 'nDoubleClicks', 'padding', 'position', 'scrollbar', 'shadow', 'style', 'textAlign', 'wheelEventStrategy']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', '_height', '_width', 'align', 'border', 'borderRadius', 'className', 'clickAwayCount', 'contextMenuEvent', 'debounceWait', 'enableClickAway', 'enableFocus', 'enableListenContextMenu', 'isFocused', 'isHovering', 'justify', 'key', 'loading_state', 'margin', 'mouseEnterCount', 'mouseLeaveCount', 'nClicks', 'nDoubleClicks', 'padding', 'position', 'scrollbar', 'shadow', 'style', 'textAlign', 'wheelEventStrategy']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyDiv, self).__init__(children=children, **args)
