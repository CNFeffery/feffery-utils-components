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


class FefferyImagePaste(Component):
    """A FefferyImagePaste component.
粘贴板图片获取组件FefferyImagePaste

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- imageInfo (dict; optional):
    监听最近一次图片粘贴事件中载入图片的`base64`字符串及时间戳信息.

    `imageInfo` is a dict with keys:

    - base64 (string; optional):
        记录最新粘贴图片的`base64`字符串.

    - timestamp (number; optional):
        时间戳信息.

- disabled (boolean; default False):
    设置是否禁用当前组件的图片粘贴行为监听功能  默认值：`False`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyImagePaste'
    ImageInfo = TypedDict(
        "ImageInfo",
            {
            "base64": NotRequired[str],
            "timestamp": NotRequired[NumberType]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        imageInfo: typing.Optional["ImageInfo"] = None,
        disabled: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'imageInfo', 'disabled']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'imageInfo', 'disabled']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyImagePaste, self).__init__(**args)

setattr(FefferyImagePaste, "__init__", _explicitize_args(FefferyImagePaste.__init__))
