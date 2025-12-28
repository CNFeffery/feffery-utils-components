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


class FefferyHighlightWords(Component):
    """A FefferyHighlightWords component.
关键词高亮组件FefferyHighlightWords

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string | dict; optional):
    当前组件css类名.

- caseSensitive (boolean; default False):
    是否启用大小写敏感  默认值：`False`.

- highlightStyle (dict; optional):
    高亮部分元素css样式.

- highlightClassName (string; default 'feffery-highlight-words-highlight'):
    高亮部分元素css类名  默认值：`'feffery-highlight-words-highlight'`.

- useRegex (boolean; default False):
    是否开启正则表达式模式  默认值：`False`.

- searchWords (list of strings; optional):
    设置要进行高亮的目标字符或正则表达式数组.

- textToHighlight (string; optional):
    原始文本内容.

- unhighlightStyle (dict; optional):
    非高亮部分元素css样式.

- unhighlightClassName (string; optional):
    非高亮部分元素css类名."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyHighlightWords'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        caseSensitive: typing.Optional[bool] = None,
        highlightStyle: typing.Optional[dict] = None,
        highlightClassName: typing.Optional[str] = None,
        useRegex: typing.Optional[bool] = None,
        searchWords: typing.Optional[typing.Sequence[str]] = None,
        textToHighlight: typing.Optional[str] = None,
        unhighlightStyle: typing.Optional[dict] = None,
        unhighlightClassName: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'caseSensitive', 'highlightStyle', 'highlightClassName', 'useRegex', 'searchWords', 'textToHighlight', 'unhighlightStyle', 'unhighlightClassName']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'caseSensitive', 'highlightStyle', 'highlightClassName', 'useRegex', 'searchWords', 'textToHighlight', 'unhighlightStyle', 'unhighlightClassName']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyHighlightWords, self).__init__(**args)

setattr(FefferyHighlightWords, "__init__", _explicitize_args(FefferyHighlightWords.__init__))
