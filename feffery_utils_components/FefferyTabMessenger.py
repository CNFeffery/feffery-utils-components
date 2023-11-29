# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyTabMessenger(Component):
    """A FefferyTabMessenger component.


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

- recivedMessage (string; optional):
    当role为'receiver'时，用于监听最近一次收到的信息内容.

- role (a value equal to: 'sender', 'receiver'; required):
    必填，声明当前组件所在标签页角色，可选的有'sender'和'receiver'.

- targetUrl (string; optional):
    当role为'sender'时，用于定义自动创建打开的目标标签页对应url.

- toSendMessage (string; optional):
    当role为'sender'时，用于设置将要新发送的信息内容，每次成功发送后都会重置为空."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyTabMessenger'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, role=Component.REQUIRED, targetUrl=Component.UNDEFINED, toSendMessage=Component.UNDEFINED, recivedMessage=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'loading_state', 'recivedMessage', 'role', 'targetUrl', 'toSendMessage']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'loading_state', 'recivedMessage', 'role', 'targetUrl', 'toSendMessage']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['role']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyTabMessenger, self).__init__(**args)
