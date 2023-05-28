# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyLocation(Component):
    """A FefferyLocation component.


Keyword arguments:

- id (string; optional)

- hash (string; optional)

- host (string; optional)

- hostname (string; optional)

- href (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- pathname (string; optional)

- port (string; optional)

- protocol (string; optional)

- search (string; optional)

- trigger (a value equal to: 'load', 'pushstate', 'popstate'; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyLocation'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, href=Component.UNDEFINED, pathname=Component.UNDEFINED, search=Component.UNDEFINED, hash=Component.UNDEFINED, host=Component.UNDEFINED, hostname=Component.UNDEFINED, port=Component.UNDEFINED, protocol=Component.UNDEFINED, trigger=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'hash', 'host', 'hostname', 'href', 'loading_state', 'pathname', 'port', 'protocol', 'search', 'trigger']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'hash', 'host', 'hostname', 'href', 'loading_state', 'pathname', 'port', 'protocol', 'search', 'trigger']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyLocation, self).__init__(**args)
