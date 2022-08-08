# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyInViewport(Component):
    """A FefferyInViewport component.


Keyword arguments:

- children (optional)

- id (optional)

- inViewport (optional)

- loading_state (optional)

- setProps (optional):
    Dash-assigned callback that should be called to report property
    changes  to Dash, to make them available for callbacks.

- threshold (optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyInViewport'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, inViewport=Component.UNDEFINED, threshold=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'inViewport', 'loading_state', 'setProps', 'threshold']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'inViewport', 'loading_state', 'setProps', 'threshold']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyInViewport, self).__init__(children=children, **args)
