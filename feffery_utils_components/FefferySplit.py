# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferySplit(Component):
    """A FefferySplit component.


Keyword arguments:

- children (optional)

- id (optional)

- className (optional)

- cursor (optional)

- direction (default 'horizontal')

- dragInterval (optional)

- expandToMin (optional)

- gutterSize (optional)

- loading_state (optional)

- maxSize (optional)

- minSize (optional)

- setProps (optional):
    Dash-assigned callback that should be called to report property
    changes  to Dash, to make them available for callbacks.

- sizes (optional)

- style (optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferySplit'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, sizes=Component.UNDEFINED, minSize=Component.UNDEFINED, maxSize=Component.UNDEFINED, expandToMin=Component.UNDEFINED, gutterSize=Component.UNDEFINED, dragInterval=Component.UNDEFINED, direction=Component.UNDEFINED, cursor=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'cursor', 'direction', 'dragInterval', 'expandToMin', 'gutterSize', 'loading_state', 'maxSize', 'minSize', 'setProps', 'sizes', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'cursor', 'direction', 'dragInterval', 'expandToMin', 'gutterSize', 'loading_state', 'maxSize', 'minSize', 'setProps', 'sizes', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferySplit, self).__init__(children=children, **args)
