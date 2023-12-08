# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyRgbColorPicker(Component):
    """A FefferyRgbColorPicker component.


Keyword arguments:

- id (string; optional):
    组件id.

- className (string; optional):
    css类名.

- color (string; default 'rgb(68, 206, 246)'):
    对应当前选中的rgb[a]色彩值字符串  默认：'rgb(68, 206, 246)'.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- showAlpha (boolean; default False):
    设置是否显示透明度选择控件  默认：False.

- style (dict; optional):
    css样式."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyRgbColorPicker'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, color=Component.UNDEFINED, showAlpha=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'color', 'loading_state', 'showAlpha', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'color', 'loading_state', 'showAlpha', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyRgbColorPicker, self).__init__(**args)
