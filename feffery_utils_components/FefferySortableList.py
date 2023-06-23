# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferySortableList(Component):
    """A FefferySortableList component.


Keyword arguments:

- id (string; optional)

- className (string | dict; optional)

- currentOrder (list of number | strings; optional)

- direction (a value equal to: 'vertical', 'horizontal'; default 'vertical')

- handleClassName (string | dict; optional)

- handlePosition (a value equal to: 'start', 'end'; default 'end')

- handleStyle (dict; optional)

- handleType (a value equal to: 'holder', 'menu', 'drag'; default 'holder')

- itemDraggingScale (number; default 1)

- items (list of dicts; required)

    `items` is a list of dicts with keys:

    - className (string | dict; optional)

    - content (a list of or a singular dash component, string or number; optional)

    - draggingClassName (string | dict; optional)

    - draggingStyle (dict; optional)

    - key (number | string; required)

    - style (dict; optional)

- key (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- style (dict; optional)"""
    _children_props = ['items[].content']
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferySortableList'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, handleStyle=Component.UNDEFINED, handleClassName=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, items=Component.REQUIRED, direction=Component.UNDEFINED, itemDraggingScale=Component.UNDEFINED, handlePosition=Component.UNDEFINED, handleType=Component.UNDEFINED, currentOrder=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'currentOrder', 'direction', 'handleClassName', 'handlePosition', 'handleStyle', 'handleType', 'itemDraggingScale', 'items', 'key', 'loading_state', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'currentOrder', 'direction', 'handleClassName', 'handlePosition', 'handleStyle', 'handleType', 'itemDraggingScale', 'items', 'key', 'loading_state', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['items']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferySortableList, self).__init__(**args)
