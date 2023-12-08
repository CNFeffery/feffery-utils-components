# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCircleColorPicker(Component):
    """A FefferyCircleColorPicker component.


Keyword arguments:

- id (string; optional):
    组件id.

- circleSize (number; default 28):
    设置圆圈的像素尺寸  默认：28.

- circleSpacing (number; default 14):
    设置圆圈之间的像素间隔大小  默认：14.

- className (string; optional):
    css类名.

- color (string; optional):
    设置或监听当前选中色彩对应16进制颜色值.

- colors (list of strings; default ["#f44336", "#e91e63", "#9c27b0", "#673ab7", "#3f51b5", "#2196f3", "#03a9f4", "#00bcd4", "#009688", "#4caf50", "#8bc34a", "#cddc39", "#ffeb3b", "#ffc107", "#ff9800", "#ff5722", "#795548", "#607d8b"]):
    设置可选色彩对应16进制颜色值数组  默认：[\"#f44336\", \"#e91e63\", \"#9c27b0\",
    \"#673ab7\", \"#3f51b5\", \"#2196f3\", \"#03a9f4\", \"#00bcd4\",
    \"#009688\", \"#4caf50\", \"#8bc34a\", \"#cddc39\", \"#ffeb3b\",
    \"#ffc107\", \"#ff9800\", \"#ff5722\", \"#795548\", \"#607d8b\"].

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

- width (string; default '252px'):
    设置组件整体宽度  默认：'252px'."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCircleColorPicker'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, width=Component.UNDEFINED, circleSize=Component.UNDEFINED, circleSpacing=Component.UNDEFINED, color=Component.UNDEFINED, colors=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'circleSize', 'circleSpacing', 'className', 'color', 'colors', 'loading_state', 'style', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'circleSize', 'circleSpacing', 'className', 'color', 'colors', 'loading_state', 'style', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyCircleColorPicker, self).__init__(**args)
