# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyLazyLoad(Component):
    """A FefferyLazyLoad component.
懒加载容器组件FefferyLazyLoad

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，设置内嵌元素内容.

- style (dict; optional):
    当前组件css样式.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- height (number | string; optional):
    设置默认高度.

- width (number | string; optional):
    设置默认宽度.

- offset (number; optional):
    设置元素距离浏览器下边界若干像素距离时开始预加载  默认值：`0`.

- visible (boolean; default False):
    监听容器是否已出现在用户视图中.

- throttle (number; optional):
    设置节流所需的延时加载时长（单位：毫秒）  默认值：`250`.

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
    _type = 'FefferyLazyLoad'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, offset=Component.UNDEFINED, visible=Component.UNDEFINED, throttle=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'height', 'width', 'offset', 'visible', 'throttle', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'height', 'width', 'offset', 'visible', 'throttle', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyLazyLoad, self).__init__(children=children, **args)
