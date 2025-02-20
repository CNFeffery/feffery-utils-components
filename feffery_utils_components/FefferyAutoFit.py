# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyAutoFit(Component):
    """A FefferyAutoFit component.
自适应组件FefferyAutoFit

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- containerId (string; default 'body'):
    要进行自适应的目标元素id  默认值：`'body'`.

- dw (number; default 1920):
    设计稿的宽度，默认是1920.

- dh (number; default 1080):
    设计稿的高度  默认值：`1080`.

- resize (boolean; default True):
    是否监听resize事件  默认值：`True`.

- ignore (list of dicts; optional):
    忽略缩放的元素列表（列表内的元素将反向缩放）.

    `ignore` is a list of dicts with keys:

    - el (string; optional):
        要忽略缩放的元素的选择器名.

- transition (number; default 0):
    过渡时间  默认值：`0`.

- delay (number; default 0):
    延迟时间  默认值：`0`.

- limit (number; default 0.1):
    不缩放的临界值，当缩放阈值不大于此值时不缩放，比如设置为`0.1`时，`0.9-1.1`的范围会被重置为`1`
    默认值：`0.1`.

- close (boolean; default False):
    关闭自适应，设置为`True`执行完相应操作后会自动重置为`False`  默认为`False`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyAutoFit'
    Ignore = TypedDict(
        "Ignore",
            {
            "el": NotRequired[str]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        containerId: typing.Optional[str] = None,
        dw: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        dh: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        resize: typing.Optional[bool] = None,
        ignore: typing.Optional[typing.Sequence["Ignore"]] = None,
        transition: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        delay: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        limit: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        close: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'containerId', 'dw', 'dh', 'resize', 'ignore', 'transition', 'delay', 'limit', 'close']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'containerId', 'dw', 'dh', 'resize', 'ignore', 'transition', 'delay', 'limit', 'close']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyAutoFit, self).__init__(**args)
