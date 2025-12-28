# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class FefferyFullscreen(Component):
    """A FefferyFullscreen component.
全屏化组件FefferyFullscreen

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- targetId (string; optional):
    设置要全屏化的目标元素id，缺省时会以整个页面作为全屏化目标.

- isFullscreen (boolean; default False):
    设置或监听目标元素的全屏化状态  默认值：`False`.

- pageFullscreen (dict; default False):
    配置是否启用页面全屏，可进一步设置页面全屏根元素对应的css类名及`z-index`值  默认值：`False`.

    `pageFullscreen` is a boolean | dict with keys:

    - className (string; optional):
        设置页面全屏根元素对应的css类名.

    - zIndex (number; optional):
        设置页面全屏根元素对应的`z-index`值."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyFullscreen'
    PageFullscreen = TypedDict(
        "PageFullscreen",
            {
            "className": NotRequired[str],
            "zIndex": NotRequired[NumberType]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        targetId: typing.Optional[str] = None,
        isFullscreen: typing.Optional[bool] = None,
        pageFullscreen: typing.Optional[typing.Union[bool, "PageFullscreen"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'targetId', 'isFullscreen', 'pageFullscreen']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'targetId', 'isFullscreen', 'pageFullscreen']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyFullscreen, self).__init__(**args)

setattr(FefferyFullscreen, "__init__", _explicitize_args(FefferyFullscreen.__init__))
