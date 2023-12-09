# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyImagePaste(Component):
    """A FefferyImagePaste component.


Keyword arguments:

- id (string; optional):
    组件id.

- disabled (boolean; default False):
    设置是否禁用当前组件的图片粘贴行为监听功能，默认为False.

- imageInfo (dict; optional):
    监听最近一次图片粘贴事件中载入图片的base64字符串及时间戳信息.

    `imageInfo` is a dict with keys:

    - base64 (string; optional):
        记录最新粘贴图片的base64字符串.

    - timestamp (number; optional):
        时间戳信息.

- key (string; optional):
    辅助刷新用唯一标识key值.

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
    _type = 'FefferyImagePaste'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, imageInfo=Component.UNDEFINED, disabled=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'disabled', 'imageInfo', 'key', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'disabled', 'imageInfo', 'key', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyImagePaste, self).__init__(**args)
