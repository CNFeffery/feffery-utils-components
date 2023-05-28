# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCookie(Component):
    """A FefferyCookie component.


Keyword arguments:

- id (string; optional)

- cookieKey (string; required)

- defaultValue (string; optional)

- expires (number; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- pathname (string; default '/')

- secure (boolean; default False)

- value (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCookie'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, cookieKey=Component.REQUIRED, defaultValue=Component.UNDEFINED, value=Component.UNDEFINED, expires=Component.UNDEFINED, pathname=Component.UNDEFINED, secure=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'cookieKey', 'defaultValue', 'expires', 'loading_state', 'pathname', 'secure', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'cookieKey', 'defaultValue', 'expires', 'loading_state', 'pathname', 'secure', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['cookieKey']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyCookie, self).__init__(**args)
