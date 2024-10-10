# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyShortcutPanel(Component):
    """A FefferyShortcutPanel component.


Keyword arguments:

- id (string; optional):
    组件id.

- locale (a value equal to: 'en', 'zh'; default 'zh'):
    设置语言，可选的有'en'、'zh'，默认为'zh'.

- data (list of dicts; required)

    `data` is a list of dicts with keys:

    - id (string; required):
        用于定义当前热键的唯一id，会在顶端热键面包屑中进行显示.

    - title (string; required):
        用于定义当前热键的标题信息.

    - hotkey (string; optional):
        用于定义当前热键对应的快捷键方式.

    - handler (string; optional):
        用于传入字符型的js函数体源码，作为当前热键被触发时的行为.

    - parent (string; optional):
        用于设置当前热键上一层级节点的id信息.

    - keywords (string; optional):
        用于设置当前热键被搜索时对应的关键词.

    - children (list of strings; optional):
        用于设置当前热键节点下一层级对应的节点id信息数组.

    - section (string; optional):
        用于设置分组标题文字.

- triggeredHotkey (dict; optional):
    监听记录最近一次被触发的热键id以及对应触发时间的时间戳信息.

    `triggeredHotkey` is a dict with keys:

    - id (string; optional):
        触发指令菜单项id.

    - timestamp (number; optional):
        触发时间戳信息.

- placeholder (string; optional):
    定义输入框提示内容，默认会根据locale赋以不同的缺省值.

- openHotkey (string; default 'cmd+k,ctrl+k'):
    设置唤出指令面板的快捷键组合，默认为'cmd+k,ctrl+k'.

- theme (a value equal to: 'light', 'dark'; default 'light'):
    设置主题，可选的有'light'、'dark'，默认为'light'.

- open (boolean; default False):
    传入True时手动展开指令面板，默认为False.

- close (boolean; default False):
    传入True时手动关闭指令面板，默认为False.

- panelStyles (dict; optional):
    用于配置指令面板相关样式参数.

    `panelStyles` is a dict with keys:

    - width (string; optional):
        设置面板宽度，默认为'640px'.

    - overflowBackground (string; optional):
        设置面板选项滚动区背景色，默认为'rgba(255, 255, 255, 0.5)'.

    - textColor (string; optional):
        设置面板字体颜色，默认为'rgb(60, 65, 73)'.

    - fontSize (string; optional):
        设置面板字体大小，默认为'16px'.

    - top (string; optional):
        设置面板距离顶端距离，默认为'20%'.

    - accentColor (string; optional):
        设置面板主色，默认为'rgb(110, 94, 210)'.

    - secondaryBackgroundColor (string; optional):
        设置面板次要背景色，默认为'rgb(239, 241, 244)'.

    - secondaryTextColor (string; optional):
        设置面板次要文字颜色，默认为'rgb(107, 111, 118)'.

    - selectedBackground (string; optional):
        设置面板选中项背景色，默认为'rgb(248, 249, 251)'.

    - actionsHeight (string; optional):
        设置面板选项区高度，默认为'300px'.

    - groupTextColor (string; optional):
        设置面板分组标签文字颜色，默认为'rgb(144, 149, 157)'.

    - zIndex (number; optional):
        设置面板的z-index信息，默认为1.

- searchValue (string; optional):
    用于监听用户当前已输入搜索内容.

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
    _type = 'FefferyShortcutPanel'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, locale=Component.UNDEFINED, data=Component.REQUIRED, triggeredHotkey=Component.UNDEFINED, placeholder=Component.UNDEFINED, openHotkey=Component.UNDEFINED, theme=Component.UNDEFINED, open=Component.UNDEFINED, close=Component.UNDEFINED, panelStyles=Component.UNDEFINED, searchValue=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'locale', 'data', 'triggeredHotkey', 'placeholder', 'openHotkey', 'theme', 'open', 'close', 'panelStyles', 'searchValue', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'locale', 'data', 'triggeredHotkey', 'placeholder', 'openHotkey', 'theme', 'open', 'close', 'panelStyles', 'searchValue', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyShortcutPanel, self).__init__(**args)
