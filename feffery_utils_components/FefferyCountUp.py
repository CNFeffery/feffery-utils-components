# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCountUp(Component):
    """A FefferyCountUp component.


Keyword arguments:

- id (string; optional):
    部件id.

- className (string; optional):
    css类名.

- decimals (number; default 0):
    设置小数精度，默认为0.

- duration (number; default 2):
    设置数字递增动画耗时，单位：秒，默认为2  对此参数的更新会重新触发递增动画.

- enableScrollSpy (boolean; default True):
    设置是否在当前元素进入视口后才开始执行递增动画，默认为True.

- end (number; required):
    设置数字递增目标，必填  对此参数的更新会重新触发递增动画.

- key (string; optional):
    强制刷新用.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- scrollSpyDelay (number; default 0):
    当enableScrollSpy为True时，设置当前元素进入视口后延时多久开始执行递增动画，单位：毫秒，默认为0.

- scrollSpyOnce (boolean; default True):
    设置是否仅进行一次视口出现后启用动画行为，默认为True.

- separator (string; default ','):
    设置自定义千分符，默认为','.

- start (number; default 0):
    设置数字递增起点，默认为0  对此参数的更新会重新触发递增动画.

- style (dict; optional):
    自定义css字典."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCountUp'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, end=Component.REQUIRED, start=Component.UNDEFINED, duration=Component.UNDEFINED, decimals=Component.UNDEFINED, enableScrollSpy=Component.UNDEFINED, scrollSpyDelay=Component.UNDEFINED, scrollSpyOnce=Component.UNDEFINED, separator=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'decimals', 'duration', 'enableScrollSpy', 'end', 'key', 'loading_state', 'scrollSpyDelay', 'scrollSpyOnce', 'separator', 'start', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'decimals', 'duration', 'enableScrollSpy', 'end', 'key', 'loading_state', 'scrollSpyDelay', 'scrollSpyOnce', 'separator', 'start', 'style']
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
