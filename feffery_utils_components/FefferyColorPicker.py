# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyColorPicker(Component):
    """A FefferyColorPicker component.


Keyword arguments:

- id (optional)

- className (optional)

- loading_state (optional)

- style (optional)

- type (default 'sketch')"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, type=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'loading_state', 'style', 'type']
        self._type = 'FefferyColorPicker'
        self._namespace = 'feffery_utils_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'loading_state', 'style', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyColorPicker, self).__init__(**args)
