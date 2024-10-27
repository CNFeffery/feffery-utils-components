# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCountUp(Component):
    """A FefferyCountUp component.
数字递增组件FefferyCountUp

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- end (number; required):
    必填，数字递增目标值，每次更新此参数后会重新触发递增动画.

- start (number; default 0):
    数字递增起始值，每次更新此参数后会重新触发递增动画  默认值：`0`.

- duration (number; default 2):
    数字递增动画耗时，单位：秒，每次更新此参数后会重新触发递增动画  默认值：`2`.

- decimals (number; default 0):
    小数精度  默认值：`0`.

- enableScrollSpy (boolean; default True):
    是否在当前元素进入视口后才开始执行递增动画  默认值：`True`.

- scrollSpyDelay (number; default 0):
    当`enableScrollSpy=True`时，设置当前元素进入视口后延时多久开始执行递增动画，单位：毫秒  默认值：`0`.

- scrollSpyOnce (boolean; default True):
    是否仅进行一次视口出现后启用动画行为  默认值：`True`.

- separator (string; default ','):
    自定义千分符  默认值：`','`.

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
    _type = 'FefferyCountUp'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, end=Component.REQUIRED, start=Component.UNDEFINED, duration=Component.UNDEFINED, decimals=Component.UNDEFINED, enableScrollSpy=Component.UNDEFINED, scrollSpyDelay=Component.UNDEFINED, scrollSpyOnce=Component.UNDEFINED, separator=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'end', 'start', 'duration', 'decimals', 'enableScrollSpy', 'scrollSpyDelay', 'scrollSpyOnce', 'separator', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'end', 'start', 'duration', 'decimals', 'enableScrollSpy', 'scrollSpyDelay', 'scrollSpyOnce', 'separator', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['end']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyCountUp, self).__init__(**args)
