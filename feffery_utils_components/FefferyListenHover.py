# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyListenHover(Component):
    """A FefferyListenHover component.
鼠标悬停监听组件FefferyListenHover

Keyword arguments:

- id (string; optional):
    组件id.

- isHovering (boolean; optional):
    监听目标元素是否处于鼠标悬停状态.

- key (string; optional):
    强制刷新用key值.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- targetSelector (string; required):
    必填，监听目标选择器字符串."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyListenHover'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, targetSelector=Component.REQUIRED, isHovering=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'isHovering', 'key', 'loading_state', 'targetSelector']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'isHovering', 'key', 'loading_state', 'targetSelector']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['targetSelector']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyListenHover, self).__init__(**args)
