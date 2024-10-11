# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyFormatBytes(Component):
    """A FefferyFormatBytes component.
字节格式化组件FefferyFormatBytes

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- value (number; default 0):
    待格式化的原始字节数值  默认值：`0`.

- unit (a value equal to: 'byte', 'bit'; default 'byte'):
    展示单位，可选项有`'byte'`、`'bit'`  默认值：`'byte'`.

- display (a value equal to: 'long', 'short', 'narrow'; default 'short'):
    展示类型，可选项有`'long'`、`'short'`、`'narrow'`  默认值：`'short'`.

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
    _type = 'FefferyFormatBytes'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, value=Component.UNDEFINED, unit=Component.UNDEFINED, display=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'value', 'unit', 'display', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'value', 'unit', 'display', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyFormatBytes, self).__init__(**args)
