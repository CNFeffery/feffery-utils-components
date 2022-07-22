# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyExtraSpinner(Component):
    """A FefferyExtraSpinner component.


Keyword arguments:

- id (optional)

- backColor (default '#1890ff')

- className (optional)

- color (default '#1890ff')

- frontColor (default '#def6ff')

- loading_state (optional)

- size (optional)

- sizeUnit (default 'px')

- style (optional)

- type (default 'ball')"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyExtraSpinner'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, type=Component.UNDEFINED, size=Component.UNDEFINED, sizeUnit=Component.UNDEFINED, color=Component.UNDEFINED, frontColor=Component.UNDEFINED, backColor=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'backColor', 'className', 'color', 'frontColor', 'loading_state', 'size', 'sizeUnit', 'style', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'backColor', 'className', 'color', 'frontColor', 'loading_state', 'size', 'sizeUnit', 'style', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyExtraSpinner, self).__init__(**args)
