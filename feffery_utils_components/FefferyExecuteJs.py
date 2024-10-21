# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyExecuteJs(Component):
    """A FefferyExecuteJs component.
js执行组件FefferyExecuteJs

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- jsString (string; optional):
    设置要执行的`javascript`代码字符串.

- mode (a value equal to: 'default', 'delay', 'interval', 'wait-until-element-rendered'; default 'default'):
    设置执行模式，可选项有`'default'`（立即执行）、`'delay'`（延迟执行）、`'interval'`（定时轮询执行）、`'wait-until-element-rendered'`（等待目标元素渲染后执行）
    默认值：`'default'`.

- delay (number; optional):
    `delay`模式下，设置延时执行时长，单位：毫秒.

- interval (number; optional):
    `interval`模式下，设置轮询执行间隔时长，单位：毫秒.

- targetSelector (string; optional):
    `wait-until-element-rendered`模式下，设置需要等待渲染完成的目标元素`css`选择器.

- targetWaitTimeout (number; optional):
    `wait-until-element-rendered`模式下，设置目标元素渲染检测最大等待时长，单位：毫秒，默认无限制.

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
    _type = 'FefferyExecuteJs'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, jsString=Component.UNDEFINED, mode=Component.UNDEFINED, delay=Component.UNDEFINED, interval=Component.UNDEFINED, targetSelector=Component.UNDEFINED, targetWaitTimeout=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'jsString', 'mode', 'delay', 'interval', 'targetSelector', 'targetWaitTimeout', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'jsString', 'mode', 'delay', 'interval', 'targetSelector', 'targetWaitTimeout', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyExecuteJs, self).__init__(**args)
