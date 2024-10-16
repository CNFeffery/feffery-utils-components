# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyHighlightWords(Component):
    """A FefferyHighlightWords component.
关键词高亮组件FefferyHighlightWords

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

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
    非高亮部分元素css类名.

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
    _type = 'FefferyHighlightWords'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, caseSensitive=Component.UNDEFINED, highlightStyle=Component.UNDEFINED, highlightClassName=Component.UNDEFINED, useRegex=Component.UNDEFINED, searchWords=Component.UNDEFINED, textToHighlight=Component.UNDEFINED, unhighlightStyle=Component.UNDEFINED, unhighlightClassName=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'caseSensitive', 'highlightStyle', 'highlightClassName', 'useRegex', 'searchWords', 'textToHighlight', 'unhighlightStyle', 'unhighlightClassName', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'caseSensitive', 'highlightStyle', 'highlightClassName', 'useRegex', 'searchWords', 'textToHighlight', 'unhighlightStyle', 'unhighlightClassName', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyHighlightWords, self).__init__(**args)
