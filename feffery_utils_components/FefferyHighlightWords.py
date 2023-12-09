# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyHighlightWords(Component):
    """A FefferyHighlightWords component.


Keyword arguments:

- id (string; optional):
    组件id.

- caseSensitive (boolean; default False):
    设置是否大小写敏感，默认为False.

- className (string; optional):
    css类名.

- highlightClassName (string; default 'feffery-highlight-words-highlight'):
    设置高亮部分的css样式类，默认为'feffery-highlight-words-highlight'.

- highlightStyle (dict; optional):
    设置高亮部分的css样式.

- key (string; optional):
    辅助刷新用唯一标识key值.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- searchWords (list of strings; optional):
    设置要进行高亮的字符（或正则模式数组），当useRegex为True时会视作正则模式数组.

- style (dict; optional):
    自定义css字典.

- textToHighlight (string; optional):
    设置文本内容字符串.

- unhighlightClassName (string; optional):
    设置非高亮部分的css样式类.

- unhighlightStyle (dict; optional):
    设置非高亮部分的css样式.

- useRegex (boolean; default False):
    设置是否开启正则表达式模式，默认为False."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyHighlightWords'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, caseSensitive=Component.UNDEFINED, highlightClassName=Component.UNDEFINED, highlightStyle=Component.UNDEFINED, useRegex=Component.UNDEFINED, searchWords=Component.UNDEFINED, textToHighlight=Component.UNDEFINED, unhighlightClassName=Component.UNDEFINED, unhighlightStyle=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'caseSensitive', 'className', 'highlightClassName', 'highlightStyle', 'key', 'loading_state', 'searchWords', 'style', 'textToHighlight', 'unhighlightClassName', 'unhighlightStyle', 'useRegex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'caseSensitive', 'className', 'highlightClassName', 'highlightStyle', 'key', 'loading_state', 'searchWords', 'style', 'textToHighlight', 'unhighlightClassName', 'unhighlightStyle', 'useRegex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyHighlightWords, self).__init__(**args)
