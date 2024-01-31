# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyIframeMessenger(Component):
    """A FefferyIframeMessenger component.


Keyword arguments:

- id (string; optional):
    组件id.

- key (string; optional):
    强制刷新组件状态用.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- mode (a value equal to: 'to-parent', 'to-child'; required):
    必填，声明当前组件对应传递信息的模式，可选的有'to-parent'和'to-child'.

- recivedMessage (boolean | number | string | dict | list; optional):
    当role为'receiver'时，用于监听最近一次收到的信息内容.

- role (a value equal to: 'sender', 'receiver'; required):
    必填，声明当前组件所在标签页角色，可选的有'sender'和'receiver'.

- targetIframeId (string; optional):
    当role为'sender'且mode为'to-child'时，用于定义需要发送消息的目标iframe组件的id.

- toSendMessage (boolean | number | string | dict | list; optional):
    当role为'sender'时，用于设置将要新发送的信息内容，每次成功发送后都会重置为空."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyIframeMessenger'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.REQUIRED, mode=Component.REQUIRED, targetIframeId=Component.UNDEFINED, toSendMessage=Component.UNDEFINED, recivedMessage=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'loading_state', 'mode', 'recivedMessage', 'role', 'targetIframeId', 'toSendMessage']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'loading_state', 'mode', 'recivedMessage', 'role', 'targetIframeId', 'toSendMessage']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['mode', 'role']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyIframeMessenger, self).__init__(**args)
