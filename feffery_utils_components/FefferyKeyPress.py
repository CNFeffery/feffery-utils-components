# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyKeyPress(Component):
    """A FefferyKeyPress component.


Keyword arguments:

- id (string; optional)

- keys (string; required)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- pressedTimes (number; default 0)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyKeyPress'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, keys=Component.REQUIRED, pressedTimes=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'keys', 'loading_state', 'pressedTimes']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'keys', 'loading_state', 'pressedTimes']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['keys']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyKeyPress, self).__init__(**args)
