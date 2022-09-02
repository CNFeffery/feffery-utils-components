# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyGithubColorPicker(Component):
    """A FefferyGithubColorPicker component.


Keyword arguments:

- id (string; optional)

- className (string; optional)

- color (string; optional)

- colors (list of strings; default ['#B80000', '#DB3E00', '#FCCB00', '#008B02', '#006B76', '#1273DE', '#004DCF', '#5300EB', '#EB9694', '#FAD0C3', '#FEF3BD', '#C1E1C5', '#BEDADC', '#C4DEF6', '#BED3F3', '#D4C4FB'])

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- style (dict; optional)

- triangle (a value equal to: 'hide', 'top-left', 'top-right'; default 'top-left')

- width (string; default '200px')"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyGithubColorPicker'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, width=Component.UNDEFINED, color=Component.UNDEFINED, colors=Component.UNDEFINED, triangle=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'color', 'colors', 'loading_state', 'style', 'triangle', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'color', 'colors', 'loading_state', 'style', 'triangle', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyGithubColorPicker, self).__init__(**args)
