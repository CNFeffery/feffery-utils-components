# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCssVar(Component):
    """A FefferyCssVar component.


Keyword arguments:

- id (string; optional):
    组件id.

- cssVars (dict; optional):
    定义要更新的css变量键值对信息.

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
    _type = 'FefferyCssVar'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, cssVars=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'cssVars', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'cssVars', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyCssVar, self).__init__(**args)
