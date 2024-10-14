# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyBlockColorPicker(Component):
    """A FefferyBlockColorPicker component.
Block风格色彩选择器

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- width (string; default '170px'):
    整体宽度  默认值：`'170px'`.

- color (string; optional):
    监听或设置当前选中色彩对应16进制颜色值.

- colors (list of strings; default ['#D9E3F0', '#F47373', '#697689', '#37D67A', '#2CCCE4', '#555555', '#dce775', '#ff8a65', '#ba68c8']):
    设置可选色彩对应16进制颜色值数组  默认值：`['#D9E3F0', '#F47373', '#697689',
    '#37D67A', '#2CCCE4', '#555555', '#dce775', '#ff8a65',
    '#ba68c8']`.

- triangle (a value equal to: 'hide', 'top'; default 'top'):
    顶部箭头方位，可选项有`'hide'`、`'top'`  默认值：`'top'`.

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
    _type = 'FefferyBlockColorPicker'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, width=Component.UNDEFINED, color=Component.UNDEFINED, colors=Component.UNDEFINED, triangle=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'width', 'color', 'colors', 'triangle', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'width', 'color', 'colors', 'triangle', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyBlockColorPicker, self).__init__(**args)
