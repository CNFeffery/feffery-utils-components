# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyEventListener(Component):
    """A FefferyEventListener component.
通用事件监听组件FefferyEventListener

Keyword arguments:

- id (string; optional):
    组件id.

- enable (boolean; default True):
    控制是否开启监听  默认值：`True`.

- eventName (string; required):
    必填，目标事件名称.

- handler (string; optional):
    必填，自定义事件处理js函数字符串，唯一入参为事件对象，返回值将用于更新`result`属性.

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

- result (boolean | number | string | dict | list; optional):
    监听`handler`对应函数的返回值，作为事件监听的结果.

- targetSelector (string; optional):
    事件监听目标对应的选择器字符串，默认监听目标为整个页面."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyEventListener'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, eventName=Component.REQUIRED, handler=Component.UNDEFINED, targetSelector=Component.UNDEFINED, enable=Component.UNDEFINED, result=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'enable', 'eventName', 'handler', 'key', 'loading_state', 'result', 'targetSelector']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'enable', 'eventName', 'handler', 'key', 'loading_state', 'result', 'targetSelector']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['eventName']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyEventListener, self).__init__(**args)
