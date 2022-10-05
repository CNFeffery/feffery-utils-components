# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyFancyNotification(Component):
    """A FefferyFancyNotification component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- autoClose (boolean | number; optional)

- bodyClassName (string; optional)

- className (string; optional)

- closable (boolean; default True)

- closeOnClick (boolean; optional)

- containerId (string; optional)

- draggable (boolean; optional)

- draggablePercent (number; optional)

- hideProgressBar (boolean; optional)

- key (string; optional)

- limit (number; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- newestOnTop (boolean; optional)

- pauseOnHover (boolean; optional)

- position (a value equal to: 'top-right', 'top-center', 'top-left', 'bottom-right', 'bottom-cente', 'bottom-left'; optional)

- progressClassName (string; optional)

- progressStyle (dict; optional)

- style (dict; optional)

- theme (a value equal to: 'light', 'dark', 'colored'; optional)

- toastClassName (string; optional)

- type (a value equal to: 'info', 'success', 'warning', 'error'; optional)

- visible (boolean; default True)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyFancyNotification'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, type=Component.UNDEFINED, visible=Component.UNDEFINED, position=Component.UNDEFINED, autoClose=Component.UNDEFINED, closable=Component.UNDEFINED, hideProgressBar=Component.UNDEFINED, pauseOnHover=Component.UNDEFINED, closeOnClick=Component.UNDEFINED, newestOnTop=Component.UNDEFINED, toastClassName=Component.UNDEFINED, bodyClassName=Component.UNDEFINED, progressClassName=Component.UNDEFINED, progressStyle=Component.UNDEFINED, draggable=Component.UNDEFINED, draggablePercent=Component.UNDEFINED, containerId=Component.UNDEFINED, limit=Component.UNDEFINED, theme=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'autoClose', 'bodyClassName', 'className', 'closable', 'closeOnClick', 'containerId', 'draggable', 'draggablePercent', 'hideProgressBar', 'key', 'limit', 'loading_state', 'newestOnTop', 'pauseOnHover', 'position', 'progressClassName', 'progressStyle', 'style', 'theme', 'toastClassName', 'type', 'visible']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'autoClose', 'bodyClassName', 'className', 'closable', 'closeOnClick', 'containerId', 'draggable', 'draggablePercent', 'hideProgressBar', 'key', 'limit', 'loading_state', 'newestOnTop', 'pauseOnHover', 'position', 'progressClassName', 'progressStyle', 'style', 'theme', 'toastClassName', 'type', 'visible']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyFancyNotification, self).__init__(children=children, **args)
