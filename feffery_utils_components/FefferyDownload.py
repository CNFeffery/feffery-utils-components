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


class FefferyDownload(Component):
    """A FefferyDownload component.
文件下载组件FefferyDownload

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- file (dict; optional):
    设置新的下载任务对应文件信息，每次触发下载后都会重置为空值.

    `file` is a dict with keys:

    - url (string; required):
        必填，文件资源地址.

    - name (string; optional):
        自定义文件下载后的文件名，可省略后缀名."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDownload'
    File = TypedDict(
        "File",
            {
            "url": str,
            "name": NotRequired[str]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        file: typing.Optional["File"] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'file']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'file']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyDownload, self).__init__(**args)

setattr(FefferyDownload, "__init__", _explicitize_args(FefferyDownload.__init__))
