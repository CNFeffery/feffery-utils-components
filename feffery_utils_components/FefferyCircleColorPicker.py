# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCircleColorPicker(Component):
    """A FefferyCircleColorPicker component.
Circle风格色彩选择器

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- width (string; default '252px'):
    整体宽度  默认值：`'252px'`.

- circleSize (number; default 28):
    圆圈像素大小  默认值：`28`.

- circleSpacing (number; default 14):
    圆圈之间的像素间隔大小  默认值：`14`.

- color (string; optional):
    监听或设置当前选中色彩对应16进制颜色值.

- colors (list of strings; default ["#f44336", "#e91e63", "#9c27b0", "#673ab7", "#3f51b5", "#2196f3", "#03a9f4", "#00bcd4", "#009688", "#4caf50", "#8bc34a", "#cddc39", "#ffeb3b", "#ffc107", "#ff9800", "#ff5722", "#795548", "#607d8b"]):
    设置可选色彩对应16进制颜色值数组  默认值：`[\"#f44336\", \"#e91e63\", \"#9c27b0\",
    \"#673ab7\", \"#3f51b5\", \"#2196f3\", \"#03a9f4\", \"#00bcd4\",
    \"#009688\", \"#4caf50\", \"#8bc34a\", \"#cddc39\", \"#ffeb3b\",
    \"#ffc107\", \"#ff9800\", \"#ff5722\", \"#795548\", \"#607d8b\"]`.

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
    _type = 'FefferyCircleColorPicker'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, width=Component.UNDEFINED, circleSize=Component.UNDEFINED, circleSpacing=Component.UNDEFINED, color=Component.UNDEFINED, colors=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'width', 'circleSize', 'circleSpacing', 'color', 'colors', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'width', 'circleSize', 'circleSpacing', 'color', 'colors', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyCircleColorPicker, self).__init__(**args)
