# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyCountUp(Component):
    """A FefferyCountUp component.
数字递增组件FefferyCountUp

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

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
    自定义千分符  默认值：`','`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCountUp'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        end: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        start: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        duration: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        decimals: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        enableScrollSpy: typing.Optional[bool] = None,
        scrollSpyDelay: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        scrollSpyOnce: typing.Optional[bool] = None,
        separator: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'end', 'start', 'duration', 'decimals', 'enableScrollSpy', 'scrollSpyDelay', 'scrollSpyOnce', 'separator']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'end', 'start', 'duration', 'decimals', 'enableScrollSpy', 'scrollSpyDelay', 'scrollSpyOnce', 'separator']
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
