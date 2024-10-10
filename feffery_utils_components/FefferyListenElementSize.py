# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyListenElementSize(Component):
    """A FefferyListenElementSize component.
元素尺寸监听组件FefferyListenElementSize

Keyword arguments:

- id (string; optional):
    组件id.

- key (string; optional):
    强制刷新用key值.

- target (string; required):
    必填，设置尺寸监听目标元素id.

- width (number; optional):
    监听目标元素像素宽度.

- height (number; optional):
    监听目标元素像素高度.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyListenElementSize'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, target=Component.REQUIRED, width=Component.UNDEFINED, height=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'target', 'width', 'height', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'target', 'width', 'height', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['target']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyListenElementSize, self).__init__(**args)
