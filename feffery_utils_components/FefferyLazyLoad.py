# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyLazyLoad(Component):
    """A FefferyLazyLoad component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    组件子元素.

- id (string; optional):
    组件id.

- className (string; optional):
    设置css类名.

- height (number | string; optional):
    设置默认高度.

- key (string; optional):
    辅助刷新用唯一标识key值.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- offset (number; optional):
    设置元素距离浏览器下边界若干像素距离时开始预加载，默认为0.

- style (dict; optional):
    自定义css字典.

- throttle (number; optional):
    设置节流所需的延时加载时长（单位：毫秒），默认为250.

- visible (boolean; default False):
    监听容器是否已出现在用户视图中.

- width (number | string; optional):
    设置默认宽度."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyLazyLoad'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, offset=Component.UNDEFINED, visible=Component.UNDEFINED, throttle=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'height', 'key', 'loading_state', 'offset', 'style', 'throttle', 'visible', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'height', 'key', 'loading_state', 'offset', 'style', 'throttle', 'visible', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyLazyLoad, self).__init__(children=children, **args)
