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


class FefferyVditor(Component):
    """A FefferyVditor component.
类Typora的markdown编辑器组件FefferyVditor

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- debounceWait (number; default 200):
    用于配置`value`变化更新的防抖等待时长（单位：毫秒） 默认值：`200`.

- undoDelay (number; optional):
    设置历史记录间隔.

- height (string | number; optional):
    设置编辑器总高度 默认值：`'auto'`.

- minHeight (number; optional):
    设置编辑区域最小高度.

- width (string | number; optional):
    设置编辑器总宽度，支持`%` 默认值：`'auto'`.

- placeholder (string; optional):
    设置输入区域为空时的提示.

- lang (a value equal to: 'en_US', 'fr_FR', 'pt_BR', 'ja_JP', 'ko_KR', 'ru_RU', 'sv_SE', 'zh_CN', 'zh_TW'; default 'zh_CN'):
    设置语言，可选的有`'en_US'`、`'fr_FR'`、`'pt_BR'`、`'ja_JP'`、`'ko_KR'`、`'ru_RU'`、`'sv_SE'`、`'zh_CN'`、`'zh_TW'`
    默认值：`'zh_CN'`.

- tab (string; optional):
    设置`tab`键操作字符串，支持`\t`及任意字符串.

- typewriterMode (boolean; default False):
    是否启用打字机模式 默认值：`False`.

- cdn (string | a value equal to: 'https://unpkg.com/vditor@3.10.9', 'https://registry.npmmirror.com/vditor/3.10.9/files'; optional):
    配置`CDN`地址，可选的内置推荐地址有`'https://unpkg.com/vditor@3.10.9'`、`'https://registry.npmmirror.com/vditor/3.10.9/files'`，也可使用其他自定义`CDN`地址.

- mode (a value equal to: 'wysiwyg', 'ir', 'sv'; default 'ir'):
    设置模式，可选的有：`'sv'`(分屏预览)、`'ir'`(即时渲染)、`'wysiwyg'`(所见即所得) 默认值：`'ir'`.

- debuggerMode (boolean; default False):
    是否显示日志 默认值：`False`.

- value (string; optional):
    编辑器`md`内容.

- theme (a value equal to: 'classic', 'dark'; default 'classic'):
    设置编辑器主题，可选的有：`'classic'`、`'dark'` 默认值：`'classic'`.

- icon (a value equal to: 'ant', 'material'; default 'ant'):
    设置图标风格，可选的有：`'ant'`、`'material'` 默认值：`'ant'`.

- toolbar (optional):
    设置工具栏.

- toolbarConfig (dict; optional):
    工具栏配置.

    `toolbarConfig` is a dict with keys:

    - hide (boolean; optional):
        是否隐藏工具栏 默认值：`False`.

    - pin (boolean; optional):
        是否固定工具栏 默认值：`False`.

- counter (dict; optional):
    计数器配置.

    `counter` is a dict with keys:

    - enable (boolean; optional):
        是否启用计数器 默认值：`False`.

    - max (number; optional):
        设置允许输入的最大值.

    - type (a value equal to: 'markdown', 'text'; optional):
        设置统计类型，可选的有：`'markdown'`、`'text'` 默认值：`'markdown'`.

- cache (dict; optional):
    缓存配置.

    `cache` is a dict with keys:

    - enable (boolean; optional):
        是否使用`localStorage`进行缓存 默认值：`True`.

    - id (string; optional):
        缓存`key`.

- preview (dict; optional):
    预览配置.

    `preview` is a dict with keys:

    - delay (number; optional):
        配置预览`debounce`毫秒间隔.

    - maxWidth (number; optional):
        配置预览区域最大宽度.

    - mode (a value equal to: 'both', 'editor'; optional):
        配置显示模式，可选的有：`'both'`、`'editor'` 默认值：`'both'`.

    - url (string; optional):
        配置md解析请求.

    - hljs (dict; optional):
        语言、样式等配置.

        `hljs` is a dict with keys:

        - defaultLang (string; optional):
            未指定语言时默认使用该语言.

        - enable (boolean; optional):
            是否启用代码高亮 默认值：`True`.

        - style (a value equal to: 'abap', 'algol', 'algol_nu', 'api', 'arduino', 'autumn', 'average', 'base16-snazzy', 'borland', 'bw', 'catppuccin-frappe', 'catppuccin-latte', 'catppuccin-macchiato', 'catppuccin-mocha', 'colorful', 'compat', 'doom-one', 'doom-one2', 'dracula', 'emacs', 'friendly', 'fruity', 'github-dark', 'github', 'gruvbox-light', 'gruvbox', 'hr_high_contrast', 'hrdark', 'igor', 'lovelace', 'manni', 'modus-operandi', 'modus-vivendi', 'monokai', 'monokailight', 'murphy', 'native', 'nord', 'onedark', 'onesenterprise', 'paraiso-dark', 'paraiso-light', 'pastie', 'perldoc', 'pygments', 'rainbow_dash', 'rose-pine-dawn', 'rose-pine-moon', 'rose-pine', 'rrt', 'solarized-dark', 'solarized-dark256', 'solarized-light', 'swapoff', 'tango', 'tokyonight-day', 'tokyonight-moon', 'tokyonight-night', 'tokyonight-storm', 'trac', 'vim', 'vs', 'vulcan', 'witchhazel', 'xcode-dark', 'xcode'; optional):
            配置菜单字号选项 默认值：`'github'`.

        - lineNumber (boolean; optional):
            是否启用行号 默认值：`False`.

        - langs (list of strings; optional):
            自定义指定语言.

    - markdown (dict; optional):
        `markdown`配置.

        `markdown` is a dict with keys:

        - autoSpace (boolean; optional):
            是否开启自动空格 默认值：`False`.

        - gfmAutoLink (boolean; optional):
            是否开启自动链接 默认值：`True`.

        - fixTermTypo (boolean; optional):
            是否开启自动矫正术语 默认值：`False`.

        - toc (boolean; optional):
            是否开启插入目录 默认值：`False`.

        - footnotes (boolean; optional):
            是否开启脚注，默认为True.

        - codeBlockPreview (boolean; optional):
            `'wysiwyg'`和`'ir'`模式下是否对代码块进行渲染 默认值：`True`.

        - mathBlockPreview (boolean; optional):
            `'wysiwyg'`和`'ir'`模式下是否对数学公式进行渲染 默认值：`True`.

        - paragraphBeginningSpace (boolean; optional):
            段落开头是否空两格 默认值：`False`.

        - sanitize (boolean; optional):
            是否启用过滤`XSS` 默认值：`True`.

        - listStyle (boolean; optional):
            是否为列表添加`data-style`属性 默认值：`False`.

        - linkBase (string; optional):
            链接相对路径前缀.

        - linkPrefix (string; optional):
            链接强制前缀.

        - mark (boolean; optional):
            是否启用`mark`标记 默认值：`False`.

    - theme (dict; optional):
        主题配置.

        `theme` is a dict with keys:

        - current (string; optional):
            当前主题 默认值：`'light'`.

        - list (dict; optional):
            可选主题列表 默认值：`{\"ant-design\": \"Ant Design\", dark:
            \"Dark\", light: \"Light\", wechat: \"WeChat\"}`.

        - path (string; optional):
            主题样式地址
            默认值：`https://unpkg.com/vditor@3.10.9/dist/css/content-theme`.

    - math (dict; optional):
        数学公式配置.

        `math` is a dict with keys:

        - inlineDigit (boolean; optional):
            内联数学公式起始`$`后是否允许数字 默认值：`False`.

        - macros (dict; optional):
            使用`MathJax`渲染时传入的宏定义.

        - engine (a value equal to: 'KaTeX', 'MathJax'; optional):
            配置数学公式渲染引擎，可选的值有`'KaTeX'`、`'MathJax'` 默认值：`'KaTeX'`.

        - mathJaxOptions (boolean

      Or number | string | dict | list; optional):
            数学公式渲染引擎为`MathJax`时的参数.

    - actions (list of dicts; optional):
        平台类型配置.

        `actions` is a list of a value equal to: 'desktop', 'tablet',
        'mobile', 'mp-wechat', 'zhihu' | dict with keys:

        - key (string; optional):

            键名.

        - text (string; optional):

            按钮文本.

        - className (string; optional):

            按钮`className`值.

        - tooltip (string; optional):

            按钮提示信息.s

    - render (dict; optional):
        多媒体渲染配置.

        `render` is a dict with keys:

        - media (dict; optional)

            `media` is a dict with keys:

            - enable (boolean; optional):
                是否启用多媒体渲染 默认值：`True`.

- image (dict; optional):
    图片配置.

    `image` is a dict with keys:

    - isPreview (boolean; optional):
        是否预览图片 默认值：`True`.

- link (dict; optional):
    链接配置.

    `link` is a dict with keys:

    - isOpen (boolean; optional):
        是否打开链接地址 默认值：`True`.

- hint (dict; optional):
    hint配置.

    `hint` is a dict with keys:

    - parse (boolean; optional):
        是否进行`md`解析 默认值：`True`.

    - delay (number; optional):
        提示`debounce`毫秒间隔 默认值：`200`.

    - emoji (dict; optional):
        默认表情，可从`https://github.com/88250/lute/blob/master/parse/emoji_map.go`中选取，也可自定义
        默认值：`{'+1': '👍', '-1': '👎', 'heart': '❤️', 'cold_sweat':
        '😰'}`.

    - emojiTail (string; optional):
        常用表情提示.

    - emojiPath (string; optional):
        表情图片地址
        默认值：`https://unpkg.com/vditor@3.10.9/dist/images/emoji`.

- upload (dict; optional):
    上传配置.

    `upload` is a dict with keys:

    - url (string; optional):
        上传`url`，为空则不会触发上传相关事件.

    - max (number; optional):
        上传文件最大`Byte` 默认值：`10 * 1024 * 1024`.

    - linkToImgUrl (string; optional):
        剪切板中包含图片地址时，使用此`url`重新上传.

    - token (boolean | number | string | dict | list; optional):
        `CORS`上传验证，头为`X-Upload-Token`.

    - withCredentials (boolean; optional):
        跨站点访问控制 默认值：`False`.

    - headers (dict; optional):
        请求头设置.

    - accept (string; optional):
        文件上传类型，同`https://www.w3schools.com/tags/att_input_accept.asp`.

    - extraData (dict; optional):
        额外请求参数.

    - multiple (boolean; optional):
        是否允许多文件上传 默认值：`True`.

    - fieldName (string; optional):
        上传字段名称 默认值：`file[]`.

- resize (dict; optional):
    拖拽配置.

    `resize` is a dict with keys:

    - enable (boolean; optional):
        是否支持大小拖拽 默认值：`False`.

    - position (a value equal to: 'top', 'bottom'; optional):
        设置拖拽栏位置，可选的值有`'top'`、`'bottom'` 默认值：`'bottom'`.

- classes (dict; optional):
    类名配置.

    `classes` is a dict with keys:

    - preview (string; optional):
        预览元素上的`className`.

- fullscreen (dict; optional):
    全屏配置.

    `fullscreen` is a dict with keys:

    - index (number; optional):
        全屏层级 默认值：`90`.

- outline (dict; optional):
    大纲配置.

    `outline` is a dict with keys:

    - enable (boolean; optional):
        初始化是否展现大纲 默认值：`False`.

    - position (a value equal to: 'left', 'right'; optional):
        大纲位置，可选的值有`'left'`、`'right'` 默认值：`'left'`.

- htmlValue (string; optional):
    编辑器`HTML`内容.

- selectedValue (string; optional):
    选中内容的字符串.

- wordCount (number; optional):
    字数统计.

- resizeHeight (number; optional):
    开启大小拖拽后监听拖拽后的高度."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyVditor'
    ToolbarConfig = TypedDict(
        "ToolbarConfig",
            {
            "hide": NotRequired[bool],
            "pin": NotRequired[bool]
        }
    )

    Counter = TypedDict(
        "Counter",
            {
            "enable": NotRequired[bool],
            "max": NotRequired[NumberType],
            "type": NotRequired[Literal["markdown", "text"]]
        }
    )

    Cache = TypedDict(
        "Cache",
            {
            "enable": NotRequired[bool],
            "id": NotRequired[str]
        }
    )

    PreviewHljs = TypedDict(
        "PreviewHljs",
            {
            "defaultLang": NotRequired[str],
            "enable": NotRequired[bool],
            "style": NotRequired[Literal["abap", "algol", "algol_nu", "api", "arduino", "autumn", "average", "base16-snazzy", "borland", "bw", "catppuccin-frappe", "catppuccin-latte", "catppuccin-macchiato", "catppuccin-mocha", "colorful", "compat", "doom-one", "doom-one2", "dracula", "emacs", "friendly", "fruity", "github-dark", "github", "gruvbox-light", "gruvbox", "hr_high_contrast", "hrdark", "igor", "lovelace", "manni", "modus-operandi", "modus-vivendi", "monokai", "monokailight", "murphy", "native", "nord", "onedark", "onesenterprise", "paraiso-dark", "paraiso-light", "pastie", "perldoc", "pygments", "rainbow_dash", "rose-pine-dawn", "rose-pine-moon", "rose-pine", "rrt", "solarized-dark", "solarized-dark256", "solarized-light", "swapoff", "tango", "tokyonight-day", "tokyonight-moon", "tokyonight-night", "tokyonight-storm", "trac", "vim", "vs", "vulcan", "witchhazel", "xcode-dark", "xcode"]],
            "lineNumber": NotRequired[bool],
            "langs": NotRequired[typing.Sequence[str]]
        }
    )

    PreviewMarkdown = TypedDict(
        "PreviewMarkdown",
            {
            "autoSpace": NotRequired[bool],
            "gfmAutoLink": NotRequired[bool],
            "fixTermTypo": NotRequired[bool],
            "toc": NotRequired[bool],
            "footnotes": NotRequired[bool],
            "codeBlockPreview": NotRequired[bool],
            "mathBlockPreview": NotRequired[bool],
            "paragraphBeginningSpace": NotRequired[bool],
            "sanitize": NotRequired[bool],
            "listStyle": NotRequired[bool],
            "linkBase": NotRequired[str],
            "linkPrefix": NotRequired[str],
            "mark": NotRequired[bool]
        }
    )

    PreviewTheme = TypedDict(
        "PreviewTheme",
            {
            "current": NotRequired[str],
            "list": NotRequired[dict],
            "path": NotRequired[str]
        }
    )

    PreviewMath = TypedDict(
        "PreviewMath",
            {
            "inlineDigit": NotRequired[bool],
            "macros": NotRequired[dict],
            "engine": NotRequired[Literal["KaTeX", "MathJax"]],
            "mathJaxOptions": NotRequired[typing.Any]
        }
    )

    PreviewActions = TypedDict(
        "PreviewActions",
            {
            "key": NotRequired[str],
            "text": NotRequired[str],
            "className": NotRequired[str],
            "tooltip": NotRequired[str]
        }
    )

    PreviewRenderMedia = TypedDict(
        "PreviewRenderMedia",
            {
            "enable": NotRequired[bool]
        }
    )

    PreviewRender = TypedDict(
        "PreviewRender",
            {
            "media": NotRequired["PreviewRenderMedia"]
        }
    )

    Preview = TypedDict(
        "Preview",
            {
            "delay": NotRequired[NumberType],
            "maxWidth": NotRequired[NumberType],
            "mode": NotRequired[Literal["both", "editor"]],
            "url": NotRequired[str],
            "hljs": NotRequired["PreviewHljs"],
            "markdown": NotRequired["PreviewMarkdown"],
            "theme": NotRequired["PreviewTheme"],
            "math": NotRequired["PreviewMath"],
            "actions": NotRequired[typing.Sequence[typing.Union[Literal["desktop", "tablet", "mobile", "mp-wechat", "zhihu"], "PreviewActions"]]],
            "render": NotRequired["PreviewRender"]
        }
    )

    Image = TypedDict(
        "Image",
            {
            "isPreview": NotRequired[bool]
        }
    )

    Link = TypedDict(
        "Link",
            {
            "isOpen": NotRequired[bool]
        }
    )

    Hint = TypedDict(
        "Hint",
            {
            "parse": NotRequired[bool],
            "delay": NotRequired[NumberType],
            "emoji": NotRequired[dict],
            "emojiTail": NotRequired[str],
            "emojiPath": NotRequired[str]
        }
    )

    Upload = TypedDict(
        "Upload",
            {
            "url": NotRequired[str],
            "max": NotRequired[NumberType],
            "linkToImgUrl": NotRequired[str],
            "token": NotRequired[typing.Any],
            "withCredentials": NotRequired[bool],
            "headers": NotRequired[dict],
            "accept": NotRequired[str],
            "extraData": NotRequired[dict],
            "multiple": NotRequired[bool],
            "fieldName": NotRequired[str]
        }
    )

    Resize = TypedDict(
        "Resize",
            {
            "enable": NotRequired[bool],
            "position": NotRequired[Literal["top", "bottom"]]
        }
    )

    Classes = TypedDict(
        "Classes",
            {
            "preview": NotRequired[str]
        }
    )

    Fullscreen = TypedDict(
        "Fullscreen",
            {
            "index": NotRequired[NumberType]
        }
    )

    Outline = TypedDict(
        "Outline",
            {
            "enable": NotRequired[bool],
            "position": NotRequired[Literal["left", "right"]]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        debounceWait: typing.Optional[NumberType] = None,
        undoDelay: typing.Optional[NumberType] = None,
        height: typing.Optional[typing.Union[str, NumberType]] = None,
        minHeight: typing.Optional[NumberType] = None,
        width: typing.Optional[typing.Union[str, NumberType]] = None,
        placeholder: typing.Optional[str] = None,
        lang: typing.Optional[Literal["en_US", "fr_FR", "pt_BR", "ja_JP", "ko_KR", "ru_RU", "sv_SE", "zh_CN", "zh_TW"]] = None,
        tab: typing.Optional[str] = None,
        typewriterMode: typing.Optional[bool] = None,
        cdn: typing.Optional[typing.Union[str, Literal["https://unpkg.com/vditor@3.10.9", "https://registry.npmmirror.com/vditor/3.10.9/files"]]] = None,
        mode: typing.Optional[Literal["wysiwyg", "ir", "sv"]] = None,
        debuggerMode: typing.Optional[bool] = None,
        value: typing.Optional[str] = None,
        theme: typing.Optional[Literal["classic", "dark"]] = None,
        icon: typing.Optional[Literal["ant", "material"]] = None,
        toolbar: typing.Optional[typing.Any] = None,
        toolbarConfig: typing.Optional["ToolbarConfig"] = None,
        counter: typing.Optional["Counter"] = None,
        cache: typing.Optional["Cache"] = None,
        preview: typing.Optional["Preview"] = None,
        image: typing.Optional["Image"] = None,
        link: typing.Optional["Link"] = None,
        hint: typing.Optional["Hint"] = None,
        upload: typing.Optional["Upload"] = None,
        resize: typing.Optional["Resize"] = None,
        classes: typing.Optional["Classes"] = None,
        fullscreen: typing.Optional["Fullscreen"] = None,
        outline: typing.Optional["Outline"] = None,
        htmlValue: typing.Optional[str] = None,
        selectedValue: typing.Optional[str] = None,
        wordCount: typing.Optional[NumberType] = None,
        resizeHeight: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'debounceWait', 'undoDelay', 'height', 'minHeight', 'width', 'placeholder', 'lang', 'tab', 'typewriterMode', 'cdn', 'mode', 'debuggerMode', 'value', 'theme', 'icon', 'toolbar', 'toolbarConfig', 'counter', 'cache', 'preview', 'image', 'link', 'hint', 'upload', 'resize', 'classes', 'fullscreen', 'outline', 'htmlValue', 'selectedValue', 'wordCount', 'resizeHeight']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'debounceWait', 'undoDelay', 'height', 'minHeight', 'width', 'placeholder', 'lang', 'tab', 'typewriterMode', 'cdn', 'mode', 'debuggerMode', 'value', 'theme', 'icon', 'toolbar', 'toolbarConfig', 'counter', 'cache', 'preview', 'image', 'link', 'hint', 'upload', 'resize', 'classes', 'fullscreen', 'outline', 'htmlValue', 'selectedValue', 'wordCount', 'resizeHeight']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyVditor, self).__init__(**args)

setattr(FefferyVditor, "__init__", _explicitize_args(FefferyVditor.__init__))
