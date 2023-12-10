# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyTextSelection(Component):
    """A FefferyTextSelection component.


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

- selectedTextInfo (dict; optional):
    监听最近一次目标容器内文本选中事件相关信息.

- targetId (string; optional):
    设置目标监听容器id.

- targetSelector (string; optional):
    设置目标监听容器对应的css选择器.

- targetType (a value equal to: 'id', 'selector'; default 'id'):
    设置目标监听规则类型，可选的有'id'、'selector'  默认：'id'."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyTextSelection'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, targetId=Component.UNDEFINED, targetSelector=Component.UNDEFINED, targetType=Component.UNDEFINED, selectedTextInfo=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'loading_state', 'selectedTextInfo', 'targetId', 'targetSelector', 'targetType']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'loading_state', 'selectedTextInfo', 'targetId', 'targetSelector', 'targetType']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyTextSelection, self).__init__(**args)
