# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyUnmount(Component):
    """A FefferyUnmount component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- isUnmount (boolean; optional)

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
    _type = 'FefferyUnmount'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, isUnmount=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'isUnmount', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'isUnmount', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyUnmount, self).__init__(children=children, **args)
