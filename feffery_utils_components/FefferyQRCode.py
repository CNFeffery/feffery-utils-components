# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyQRCode(Component):
    """A FefferyQRCode component.


Keyword arguments:

- id (string; optional)

- bgColor (string; default '#FFFFFF')

- fgColor (string; default '#000000')

- imageSettings (dict; optional)

    `imageSettings` is a dict with keys:

    - excavate (boolean; optional)

    - height (number; optional)

    - src (string; optional)

    - width (number; optional)

- includeMargin (boolean; default False)

- level (a value equal to: 'L', 'M', 'Q', 'H'; default 'L')

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- renderer (a value equal to: 'svg', 'canvas'; default 'svg')

- size (number; default 128)

- value (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyQRCode'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, value=Component.REQUIRED, size=Component.UNDEFINED, bgColor=Component.UNDEFINED, fgColor=Component.UNDEFINED, level=Component.UNDEFINED, includeMargin=Component.UNDEFINED, imageSettings=Component.UNDEFINED, renderer=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'bgColor', 'fgColor', 'imageSettings', 'includeMargin', 'level', 'loading_state', 'renderer', 'size', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'bgColor', 'fgColor', 'imageSettings', 'includeMargin', 'level', 'loading_state', 'renderer', 'size', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['value']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyQRCode, self).__init__(**args)
