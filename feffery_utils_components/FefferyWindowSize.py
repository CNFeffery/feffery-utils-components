# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyWindowSize(Component):
    """A FefferyWindowSize component.


Keyword arguments:

- id (string; optional):
    组件id.

- _height (number; optional):
    监听当前浏览器窗口高度.

- _width (number; optional):
    监听当前浏览器窗口像素宽度.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyWindowSize'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, _width=Component.UNDEFINED, _height=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', '_height', '_width', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', '_height', '_width', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyWindowSize, self).__init__(**args)
