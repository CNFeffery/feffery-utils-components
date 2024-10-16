# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyScrollbars(Component):
    """A FefferyScrollbars component.
滚动条容器组件FefferyScrollbars

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，内嵌元素.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- autoHide (boolean; default True):
    是否在无操作时自动隐藏滚动条  默认值：`True`.

- classNames (dict; optional):
    各组成部分css类名.

    `classNames` is a dict with keys:

    - content (string; optional):
        内容区域容器.

    - scrollContent (string; optional):
        正在滚动的内容容器.

    - scrollbar (string; optional):
        滚动条.

    - track (string; optional):
        滚动条滑块.

- forceVisible (boolean | a value equal to: 'x', 'y'; default False):
    滑块区域是否强制可见，可传入由`'x'`、`'y'`组成的列表进行水平、竖直方向的单独设置  默认值：`False`.

- timeout (number; default 1000):
    滑块自动隐藏延时，单位：毫秒  默认值：`1000`.

- scrollbarMinSize (number; default 25):
    滚动条最小像素长度  默认值：`25`.

- scrollbarMaxSize (number; optional):
    滚动条最大像素长度.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyScrollbars'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, autoHide=Component.UNDEFINED, classNames=Component.UNDEFINED, forceVisible=Component.UNDEFINED, timeout=Component.UNDEFINED, scrollbarMinSize=Component.UNDEFINED, scrollbarMaxSize=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'autoHide', 'classNames', 'forceVisible', 'timeout', 'scrollbarMinSize', 'scrollbarMaxSize', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'autoHide', 'classNames', 'forceVisible', 'timeout', 'scrollbarMinSize', 'scrollbarMaxSize', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyScrollbars, self).__init__(children=children, **args)
