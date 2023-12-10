# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyListenScroll(Component):
    """A FefferyListenScroll component.


Keyword arguments:

- id (string; optional):
    组件id.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- position (dict; optional):
    监听目标滚动条的水平及竖直方向上的像素偏移量.

- target (string; optional):
    设置滚动条监听目标元素id，默认为整个页面."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyListenScroll'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, target=Component.UNDEFINED, position=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'loading_state', 'position', 'target']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'loading_state', 'position', 'target']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyListenScroll, self).__init__(**args)
