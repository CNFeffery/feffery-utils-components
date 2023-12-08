# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyEyeDropper(Component):
    """A FefferyEyeDropper component.


Keyword arguments:

- id (string; optional):
    组件id.

- color (string; optional):
    用于监听最近一次取色完成后对应的16进制色彩值.

- enable (boolean; default False):
    设置是否启用色彩拾取模式，每次取色完成后都会被重置为False  默认：False.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyEyeDropper'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, enable=Component.UNDEFINED, color=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'color', 'enable', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'color', 'enable', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyEyeDropper, self).__init__(**args)
