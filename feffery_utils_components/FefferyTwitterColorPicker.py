# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyTwitterColorPicker(Component):
    """A FefferyTwitterColorPicker component.


Keyword arguments:

- id (string; optional):
    组件id.

- className (string; optional):
    css类名.

- color (string; optional):
    设置或监听当前选中色彩对应16进制颜色值.

- colors (list of strings; default ['#FF6900', '#FCB900', '#7BDCB5', '#00D084', '#8ED1FC', '#0693E3', '#ABB8C3', '#EB144C', '#F78DA7', '#9900EF']):
    设置可选色彩对应16进制颜色值数组  默认：['#FF6900', '#FCB900', '#7BDCB5', '#00D084',
    '#8ED1FC', '#0693E3', '#ABB8C3', '#EB144C', '#F78DA7', '#9900EF'].

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

- triangle (a value equal to: 'hide', 'top-left', 'top-right'; default 'top-left'):
    设置顶部箭头的方位，可选的有'hide'、'top-left'、'top-right'  默认：'top-left'.

- width (string; default '276px'):
    设置组件整体宽度  默认：'276px'."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyTwitterColorPicker'
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

        super(FefferyTwitterColorPicker, self).__init__(**args)
