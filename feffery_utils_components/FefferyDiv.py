# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyDiv(Component):
    """A FefferyDiv component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- _height (number; optional)

- _width (number; optional)

- className (string | dict; optional)

- clickAwayCount (number; default 0)

- contextMenuEvent (dict; optional)

    `contextMenuEvent` is a dict with keys:

    - pageX (number; optional)

    - pageY (number; optional)

    - timestamp (number; optional)

- debounceWait (number; default 150)

- enableListenContextMenu (boolean; default False)

- isHovering (boolean; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- mouseEnterCount (number; default 0)

- mouseLeaveCount (number; default 0)

- nClicks (number; default 0)

- nDoubleClicks (number; default 0)

- style (dict; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDiv'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, _width=Component.UNDEFINED, _height=Component.UNDEFINED, debounceWait=Component.UNDEFINED, mouseEnterCount=Component.UNDEFINED, mouseLeaveCount=Component.UNDEFINED, nClicks=Component.UNDEFINED, nDoubleClicks=Component.UNDEFINED, enableListenContextMenu=Component.UNDEFINED, contextMenuEvent=Component.UNDEFINED, isHovering=Component.UNDEFINED, clickAwayCount=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', '_height', '_width', 'className', 'clickAwayCount', 'contextMenuEvent', 'debounceWait', 'enableListenContextMenu', 'isHovering', 'loading_state', 'mouseEnterCount', 'mouseLeaveCount', 'nClicks', 'nDoubleClicks', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', '_height', '_width', 'className', 'clickAwayCount', 'contextMenuEvent', 'debounceWait', 'enableListenContextMenu', 'isHovering', 'loading_state', 'mouseEnterCount', 'mouseLeaveCount', 'nClicks', 'nDoubleClicks', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyDiv, self).__init__(children=children, **args)
