# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyGithubColorPicker(Component):
    """A FefferyGithubColorPicker component.


Keyword arguments:

- id (string; optional):
    组件id.

- style (dict; optional):
    css样式.

- className (string; optional):
    css类名.

- color (string; optional):
    设置或监听当前选中色彩对应16进制颜色值.

- colors (list of strings; default ['#B80000', '#DB3E00', '#FCCB00', '#008B02', '#006B76', '#1273DE', '#004DCF', '#5300EB', '#EB9694', '#FAD0C3', '#FEF3BD', '#C1E1C5', '#BEDADC', '#C4DEF6', '#BED3F3', '#D4C4FB']):
    设置可选色彩对应16进制颜色值数组  默认：['#B80000', '#DB3E00', '#FCCB00', '#008B02',
    '#006B76', '#1273DE', '#004DCF', '#5300EB', '#EB9694', '#FAD0C3',
    '#FEF3BD', '#C1E1C5', '#BEDADC', '#C4DEF6', '#BED3F3', '#D4C4FB'].

- triangle (a value equal to: 'hide', 'top-left', 'top-right'; default 'top-left'):
    设置顶部箭头的方位，可选的有'hide'、'top-left'、'top-right'  默认：'top-left'.

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
    _type = 'FefferyGithubColorPicker'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, color=Component.UNDEFINED, colors=Component.UNDEFINED, triangle=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'style', 'className', 'color', 'colors', 'triangle', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'style', 'className', 'color', 'colors', 'triangle', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyGithubColorPicker, self).__init__(**args)
