# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyTextSelection(Component):
    """A FefferyTextSelection component.
文字选中监听组件FefferyTextSelection

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- targetId (string; optional):
    设置目标监听容器`id`.

- targetSelector (string; optional):
    设置目标监听容器对应的`css`选择器.

- targetType (a value equal to: 'id', 'selector'; default 'id'):
    设置目标监听规则类型，可选项有`'id'`、`'selector'`  默认值：`'id'`.

- selectedTextInfo (dict; optional):
    监听最近一次目标容器内文本选中事件相关信息.

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
    _type = 'FefferyTextSelection'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, targetId=Component.UNDEFINED, targetSelector=Component.UNDEFINED, targetType=Component.UNDEFINED, selectedTextInfo=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'targetId', 'targetSelector', 'targetType', 'selectedTextInfo', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'targetId', 'targetSelector', 'targetType', 'selectedTextInfo', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyTextSelection, self).__init__(**args)
