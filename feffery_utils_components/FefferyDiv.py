# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyDiv(Component):
    """A FefferyDiv component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- _height (number; optional)

- _width (number; optional)

- align (string; optional)

- border (string; optional)

- borderRadius (string | number; optional)

- className (string | dict; optional)

- clickAwayCount (number; default 0)

- contextMenuEvent (dict; optional)

    `contextMenuEvent` is a dict with keys:

    - clientX (number; optional)

    - clientY (number; optional)

    - pageX (number; optional)

    - pageY (number; optional)

    - screenX (number; optional)

    - screenY (number; optional)

    - timestamp (number; optional)

- debounceWait (number; default 150)

- enableClickAway (boolean; default False)

- enableListenContextMenu (boolean; default False)

- isHovering (boolean; optional)

- justify (string; optional)

- key (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- margin (string | number; optional)

- mouseEnterCount (number; default 0)

- mouseLeaveCount (number; default 0)

- nClicks (number; default 0)

- nDoubleClicks (number; default 0)

- padding (string | number; optional)

- scrollbar (a value equal to: 'default', 'simple', 'hidden'; default 'default')

- shadow (a value equal to: 'no-shadow', 'hover-shadow', 'always-shadow', 'hover-shadow-light', 'always-shadow-light'; default 'no-shadow')

- style (dict; optional)

- textAlign (a value equal to: 'left', 'center', 'right'; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDiv'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, _width=Component.UNDEFINED, _height=Component.UNDEFINED, debounceWait=Component.UNDEFINED, mouseEnterCount=Component.UNDEFINED, mouseLeaveCount=Component.UNDEFINED, nClicks=Component.UNDEFINED, nDoubleClicks=Component.UNDEFINED, enableListenContextMenu=Component.UNDEFINED, contextMenuEvent=Component.UNDEFINED, isHovering=Component.UNDEFINED, enableClickAway=Component.UNDEFINED, clickAwayCount=Component.UNDEFINED, shadow=Component.UNDEFINED, scrollbar=Component.UNDEFINED, textAlign=Component.UNDEFINED, justify=Component.UNDEFINED, align=Component.UNDEFINED, padding=Component.UNDEFINED, margin=Component.UNDEFINED, border=Component.UNDEFINED, borderRadius=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', '_height', '_width', 'align', 'border', 'borderRadius', 'className', 'clickAwayCount', 'contextMenuEvent', 'debounceWait', 'enableClickAway', 'enableListenContextMenu', 'isHovering', 'justify', 'key', 'loading_state', 'margin', 'mouseEnterCount', 'mouseLeaveCount', 'nClicks', 'nDoubleClicks', 'padding', 'scrollbar', 'shadow', 'style', 'textAlign']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', '_height', '_width', 'align', 'border', 'borderRadius', 'className', 'clickAwayCount', 'contextMenuEvent', 'debounceWait', 'enableClickAway', 'enableListenContextMenu', 'isHovering', 'justify', 'key', 'loading_state', 'margin', 'mouseEnterCount', 'mouseLeaveCount', 'nClicks', 'nDoubleClicks', 'padding', 'scrollbar', 'shadow', 'style', 'textAlign']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyDiv, self).__init__(children=children, **args)
