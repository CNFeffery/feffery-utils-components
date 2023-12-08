# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyBlockColorPicker(Component):
    """A FefferyBlockColorPicker component.


Keyword arguments:

- id (string; optional):
    组件id.

- className (string; optional):
    css类名.

- color (string; optional):
    设置或监听当前选中色彩对应16进制颜色值.

- colors (list of strings; default ['#D9E3F0', '#F47373', '#697689', '#37D67A', '#2CCCE4', '#555555', '#dce775', '#ff8a65', '#ba68c8']):
    设置可选色彩对应16进制颜色值数组  默认：['#D9E3F0', '#F47373', '#697689', '#37D67A',
    '#2CCCE4', '#555555', '#dce775', '#ff8a65', '#ba68c8'].

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- style (dict; optional):
    css样式.

- triangle (a value equal to: 'hide', 'top'; default 'top'):
    设置顶部箭头方位，可选的有'hide'、'top'  默认：'top'.

- width (string; default '170px'):
    设置组件整体宽度  默认：'170px'."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyBlockColorPicker'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, width=Component.UNDEFINED, color=Component.UNDEFINED, colors=Component.UNDEFINED, triangle=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'color', 'colors', 'loading_state', 'style', 'triangle', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'color', 'colors', 'loading_state', 'style', 'triangle', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyBlockColorPicker, self).__init__(**args)
