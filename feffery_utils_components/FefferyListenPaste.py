# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyListenPaste(Component):
    """A FefferyListenPaste component.


Keyword arguments:

- id (string; optional):
    组件id.

- enableListenPaste (boolean; default False):
    用于设置是否为当前组件启用粘贴事件监听  默认：False.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- pasteCount (number; default 0):
    监听累计监听到的粘贴事件发生次数  默认：0.

- pasteText (string; optional):
    监听最近一次文本粘贴事件对应的粘贴内容.

- targetContainerId (string; optional):
    用于设置要监听绑定的目标容器id，设置此参数后，粘贴事件监听仅在目标容器被鼠标悬停时生效."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyListenPaste'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, pasteText=Component.UNDEFINED, pasteCount=Component.UNDEFINED, enableListenPaste=Component.UNDEFINED, targetContainerId=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'enableListenPaste', 'loading_state', 'pasteCount', 'pasteText', 'targetContainerId']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'enableListenPaste', 'loading_state', 'pasteCount', 'pasteText', 'targetContainerId']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyListenPaste, self).__init__(**args)
