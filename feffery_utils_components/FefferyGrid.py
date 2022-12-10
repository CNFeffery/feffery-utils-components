# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyGrid(Component):
    """A FefferyGrid component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- allowOverlap (boolean; default False)

- autoSize (boolean; default True)

- breakpoints (dict with strings as keys and values of type number; default { lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0 })

- className (string; optional)

- cols (dict with strings as keys and values of type number | number; default 12)

- compactType (a value equal to: 'vertical', 'horizontal'; default 'vertical')

- containerPadding (list of numbers | dict with strings as keys and values of type list of numbers; optional)

- height (number; optional)

- isBounded (boolean; default False)

- isDraggable (boolean; default True)

- isResizable (boolean; default True)

- key (string; optional)

- layouts (dict; optional)

    `layouts` is a dict with strings as keys and values of type list
    of dicts with keys:

    - h (number; optional)

    - i (string; optional)

    - isBounded (boolean; optional)

    - isDraggable (boolean; optional)

    - isResizable (boolean; optional)

    - maxH (number; optional)

    - maxW (number; optional)

    - minH (number; optional)

    - minW (number; optional)

    - moved (boolean | number | string | dict | list; optional)

    - static (boolean; optional)

    - w (number; optional)

    - x (number; optional)

    - y (number; optional) | list of dicts with keys:

    - h (number; optional)

    - i (string; optional)

    - isBounded (boolean; optional)

    - isDraggable (boolean; optional)

    - isResizable (boolean; optional)

    - maxH (number; optional)

    - maxW (number; optional)

    - minH (number; optional)

    - minW (number; optional)

    - moved (boolean | number | string | dict | list; optional)

    - static (boolean; optional)

    - w (number; optional)

    - x (number; optional)

    - y (number; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- margin (list of numbers | dict with strings as keys and values of type list of numbers; default [10, 10])

- placeholderBackground (string; default '#3b3a39')

- placeholderBorder (string; default 'none')

- placeholderBorderRadius (string; default '0px')

- placeholderOpacity (number; default 0.2)

- rowHeight (number; default 150)

- style (dict; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyGrid'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, height=Component.UNDEFINED, autoSize=Component.UNDEFINED, compactType=Component.UNDEFINED, margin=Component.UNDEFINED, containerPadding=Component.UNDEFINED, rowHeight=Component.UNDEFINED, isDraggable=Component.UNDEFINED, isResizable=Component.UNDEFINED, isBounded=Component.UNDEFINED, allowOverlap=Component.UNDEFINED, breakpoints=Component.UNDEFINED, cols=Component.UNDEFINED, layouts=Component.UNDEFINED, placeholderBackground=Component.UNDEFINED, placeholderOpacity=Component.UNDEFINED, placeholderBorder=Component.UNDEFINED, placeholderBorderRadius=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'allowOverlap', 'autoSize', 'breakpoints', 'className', 'cols', 'compactType', 'containerPadding', 'height', 'isBounded', 'isDraggable', 'isResizable', 'key', 'layouts', 'loading_state', 'margin', 'placeholderBackground', 'placeholderBorder', 'placeholderBorderRadius', 'placeholderOpacity', 'rowHeight', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'allowOverlap', 'autoSize', 'breakpoints', 'className', 'cols', 'compactType', 'containerPadding', 'height', 'isBounded', 'isDraggable', 'isResizable', 'key', 'layouts', 'loading_state', 'margin', 'placeholderBackground', 'placeholderBorder', 'placeholderBorderRadius', 'placeholderOpacity', 'rowHeight', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyGrid, self).__init__(children=children, **args)
