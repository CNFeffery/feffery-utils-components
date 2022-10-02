# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferySplit(Component):
    """A FefferySplit component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- cursor (string; optional)

- direction (a value equal to: 'horizontal', 'vertical'; default 'horizontal')

- dragInterval (number; optional)

- expandToMin (boolean; optional)

- gutterSize (number; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- maxSize (number | list of numbers; optional)

- minSize (number | list of numbers; optional)

- sizes (list of numbers; optional)

- style (dict; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferySplit'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, sizes=Component.UNDEFINED, minSize=Component.UNDEFINED, maxSize=Component.UNDEFINED, expandToMin=Component.UNDEFINED, gutterSize=Component.UNDEFINED, dragInterval=Component.UNDEFINED, direction=Component.UNDEFINED, cursor=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'cursor', 'direction', 'dragInterval', 'expandToMin', 'gutterSize', 'loading_state', 'maxSize', 'minSize', 'sizes', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'cursor', 'direction', 'dragInterval', 'expandToMin', 'gutterSize', 'loading_state', 'maxSize', 'minSize', 'sizes', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferySplit, self).__init__(children=children, **args)
