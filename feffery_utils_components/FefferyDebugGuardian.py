# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyDebugGuardian(Component):
    """A FefferyDebugGuardian component.
调试守护组件FefferyDebugGuardian

Keyword arguments:

- id (string; optional):
    组件id.

- detectInterval (number; default 1000):
    设置后台轮询检测的间隔时长，单位：毫秒  默认：1000.

- strategy (a value equal to: 'infinite-debugger', 'debugger-then-auto-close', 'debugger-then-execute-js'; default 'infinite-debugger'):
    设置当检测到开发者工具被打开时的应对策略，可选的有'infinite-debugger'（无限debugger）、'debugger-then-auto-close'（激活debugger后自动关闭）、'debugger-then-execute-js'（激活debugger后执行js）
    默认：'infinite-debugger'.

- jsString (string; optional):
    当strategy为'debugger-then-execute-js'时，设置要执行的js代码.

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
    _type = 'FefferyDebugGuardian'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, detectInterval=Component.UNDEFINED, strategy=Component.UNDEFINED, jsString=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'detectInterval', 'strategy', 'jsString', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'detectInterval', 'strategy', 'jsString', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyDebugGuardian, self).__init__(**args)
