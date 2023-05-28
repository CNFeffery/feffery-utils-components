# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyResizable(Component):
    """A FefferyResizable component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- bounds (a value equal to: 'window', 'parent'; default 'window')

- className (string; optional)

- defaultSize (dict; optional)

    `defaultSize` is a dict with keys:

    - height (number | string; optional)

    - width (number | string; optional)

- direction (list of a value equal to: 'top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft's; default ['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft'])

- grid (list of numbers; default [1, 1])

- handleClassNames (dict; optional)

    `handleClassNames` is a dict with keys:

    - bottom (string; optional)

    - bottomLeft (string; optional)

    - bottomRight (string; optional)

    - left (string; optional)

    - right (string; optional)

    - top (string; optional)

    - topLeft (string; optional)

    - topRight (string; optional)

- handleStyles (dict; optional)

    `handleStyles` is a dict with keys:

    - bottom (dict; optional)

    - bottomLeft (dict; optional)

    - bottomRight (dict; optional)

    - left (dict; optional)

    - right (dict; optional)

    - top (dict; optional)

    - topLeft (dict; optional)

    - topRight (dict; optional)

- key (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- maxHeight (number | string; optional)

- maxWidth (number | string; optional)

- minHeight (number | string; default 10)

- minWidth (number | string; default 10)

- style (dict; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyResizable'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, defaultSize=Component.UNDEFINED, minWidth=Component.UNDEFINED, minHeight=Component.UNDEFINED, maxWidth=Component.UNDEFINED, maxHeight=Component.UNDEFINED, direction=Component.UNDEFINED, grid=Component.UNDEFINED, bounds=Component.UNDEFINED, handleStyles=Component.UNDEFINED, handleClassNames=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bounds', 'className', 'defaultSize', 'direction', 'grid', 'handleClassNames', 'handleStyles', 'key', 'loading_state', 'maxHeight', 'maxWidth', 'minHeight', 'minWidth', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bounds', 'className', 'defaultSize', 'direction', 'grid', 'handleClassNames', 'handleStyles', 'key', 'loading_state', 'maxHeight', 'maxWidth', 'minHeight', 'minWidth', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyResizable, self).__init__(children=children, **args)
