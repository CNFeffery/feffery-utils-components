# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyScrollbars(Component):
    """A FefferyScrollbars component.


Keyword arguments:

- id (string; optional):
    组件id.

- children (a list of or a singular dash component, string or number; optional):
    组件子元素.

- style (dict; optional):
    设置自定义css样式.

- className (string; optional):
    设置自定义css类名.

- key (string; optional):
    辅助刷新用唯一标识key值.

- autoHide (boolean; default True):
    设置是否在无操作时自动隐藏滚动条，默认为True.

- classNames (dict; optional):
    针对各组成部分单独设置自定义css类名.

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
    设置滑块区域是否强制可见，默认为False.

- timeout (number; default 1000):
    设置滑块自动隐藏的毫秒数，默认为1000.

- scrollbarMinSize (number; default 25):
    设置滚动条最小像素长度，默认为25.

- scrollbarMaxSize (number; optional):
    设置滚动条最大像素长度，默认无限制.

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
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, autoHide=Component.UNDEFINED, classNames=Component.UNDEFINED, forceVisible=Component.UNDEFINED, timeout=Component.UNDEFINED, scrollbarMinSize=Component.UNDEFINED, scrollbarMaxSize=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'children', 'style', 'className', 'key', 'autoHide', 'classNames', 'forceVisible', 'timeout', 'scrollbarMinSize', 'scrollbarMaxSize', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'children', 'style', 'className', 'key', 'autoHide', 'classNames', 'forceVisible', 'timeout', 'scrollbarMinSize', 'scrollbarMaxSize', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyScrollbars, self).__init__(children=children, **args)
