# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferySticky(Component):
    """A FefferySticky component.
粘性布局组件FefferySticky

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，内嵌元素.

- enabled (boolean; default True):
    是否启用粘性布局效果  默认值：`True`.

- top (number | string; default 0):
    用于设置触发粘性布局效果对应的顶部距离阈值，当当前元素距离窗口顶部达到此阈值时会触发粘性布局状态，
    当传入数值型时，用于设置窗口顶端到当前元素顶部的像素距离阈值，
    当传入字符型时，用于定义`css`选择器规则，被此选择器规则匹配到的元素的高度会被作为阈值所使用.

- bottomBoundary (number | string; optional):
    用于设置解除粘性布局效果对应的底部距离阈值，  当传入数值型时，用于设置页面顶端到当前元素顶部的像素距离阈值，
    当传入字符型时，用于定义`css`选择器规则，当该规则匹配到的目标元素底部到达粘性布局元素底部时，粘性状态会被解除.

- zIndex (number; optional):
    粘性布局元素对应`z-index`属性.

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
    _type = 'FefferySticky'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, enabled=Component.UNDEFINED, top=Component.UNDEFINED, bottomBoundary=Component.UNDEFINED, zIndex=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'children', 'enabled', 'top', 'bottomBoundary', 'zIndex', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'enabled', 'top', 'bottomBoundary', 'zIndex', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferySticky, self).__init__(children=children, **args)
