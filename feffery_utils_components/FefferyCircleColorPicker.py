# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCircleColorPicker(Component):
    """A FefferyCircleColorPicker component.


Keyword arguments:

- id (optional)

- circleSize (optional)

- circleSpacing (optional)

- className (optional)

- color (optional)

- colors (optional)

- loading_state (optional)

- style (optional)

- width (optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCircleColorPicker'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, width=Component.UNDEFINED, colors=Component.UNDEFINED, circleSize=Component.UNDEFINED, circleSpacing=Component.UNDEFINED, color=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'circleSize', 'circleSpacing', 'className', 'color', 'colors', 'loading_state', 'style', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'circleSize', 'circleSpacing', 'className', 'color', 'colors', 'loading_state', 'style', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyCircleColorPicker, self).__init__(**args)
