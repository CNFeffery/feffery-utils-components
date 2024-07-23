# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyListenDrag(Component):
    """A FefferyListenDrag component.
拖拽事件监听组件FefferyListenDrag

Keyword arguments:

- id (string; optional):
    组件id.

- data (boolean | number | string | dict | list; optional):
    当前监听目标所携带的数据，配合**FefferyListenDrop**使用.

- isDragging (boolean; optional):
    监听目标是否处于拖拽中状态.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- targetSelector (string; optional):
    拖拽事件监听目标选择器规则字符串."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyListenDrag'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, targetSelector=Component.UNDEFINED, data=Component.UNDEFINED, isDragging=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data', 'isDragging', 'loading_state', 'targetSelector']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data', 'isDragging', 'loading_state', 'targetSelector']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyListenDrag, self).__init__(**args)
