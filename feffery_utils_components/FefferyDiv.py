# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyDiv(Component):
    """A FefferyDiv component.


Keyword arguments:

- children (optional)

- id (optional)

- _height (optional)

- _width (optional)

- className (optional)

- contextMenuEvent (optional)

- debounceWait (default 150)

- enableListenContextMenu (default False)

- loading_state (optional)

- mouseEnterCounts (default 0)

- mouseLeaveCounts (default 0)

- nClicks (default 0)

- nDoubleClicks (default 0)

- setProps (optional):
    Dash-assigned callback that should be called to report property
    changes  to Dash, to make them available for callbacks.

- style (optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDiv'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, _width=Component.UNDEFINED, _height=Component.UNDEFINED, debounceWait=Component.UNDEFINED, mouseEnterCounts=Component.UNDEFINED, mouseLeaveCounts=Component.UNDEFINED, nClicks=Component.UNDEFINED, nDoubleClicks=Component.UNDEFINED, enableListenContextMenu=Component.UNDEFINED, contextMenuEvent=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', '_height', '_width', 'className', 'contextMenuEvent', 'debounceWait', 'enableListenContextMenu', 'loading_state', 'mouseEnterCounts', 'mouseLeaveCounts', 'nClicks', 'nDoubleClicks', 'setProps', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', '_height', '_width', 'className', 'contextMenuEvent', 'debounceWait', 'enableListenContextMenu', 'loading_state', 'mouseEnterCounts', 'mouseLeaveCounts', 'nClicks', 'nDoubleClicks', 'setProps', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyDiv, self).__init__(children=children, **args)
