# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyVditor(Component):
    """A FefferyVditor component.


Keyword arguments:

- id (string; optional):
    组件id.

- cache (dict; optional):
    缓存配置.

    `cache` is a dict with keys:

    - enable (boolean; optional):
        是否使用localStorage进行缓存，默认为True.

    - id (string; optional):
        缓存key.

- cdn (string | a value equal to: `https://unpkg.com/vditor@${VDITOR_VERSION}`, `https://registry.npmmirror.com/vditor/${VDITOR_VERSION}/files`; optional):
    配置CDN地址，
    可选的有`https://unpkg.com/vditor@${VDITOR_VERSION}`、`https://registry.npmmirror.com/vditor/${VDITOR_VERSION}/files`，
    VDITOR_VERSION是vditor版本号，可通过不设置此参数从浏览器请求信息中获取版本号信息，默认使用的是`https://unpkg.com/vditor@${VDITOR_VERSION}`，
    也可使用自行搭建的cdn地址.

- className (string; optional):
    组件类名.

- classes (dict; optional):
    类名配置.

    `classes` is a dict with keys:

    - preview (string; optional):
        预览元素上的className.

- counter (dict; optional):
    计数器配置.

    `counter` is a dict with keys:

    - enable (boolean; optional):
        是否启用计数器，默认为False.

    - max (number; optional):
        设置允许输入的最大值.

    - type (a value equal to: 'markdown', 'text'; optional):
        设置统计类型，可选的有：'markdown'和'text'，默认为'markdown'.

- debounceWait (number; default 200):
    用于配置value变化更新的防抖等待时长（单位：毫秒），默认为200.

- debuggerMode (boolean; default False):
    是否显示日志，默认为False.

- fullscreen (dict; optional):
    全屏配置.

    `fullscreen` is a dict with keys:

    - index (number; optional):
        全屏层级，默认为90.

- height (string | number; optional):
    设置编辑器总高度，默认为'auto'.

- hint (dict; optional)

    `hint` is a dict with keys:

    - delay (number; optional):
        提示 debounce 毫秒间隔，默认为200.

    - emoji (dict; optional):
        默认表情，可从https://github.com/88250/lute/blob/master/parse/emoji_map.go中选取，也可自定义，
        默认为{ '+1': '👍', '-1': '👎', 'heart': '❤️', 'cold_sweat': '😰' }.

    - emojiPath (string; optional):
        表情图片地址，默认为https://unpkg.com/vditor@${VDITOR_VERSION}/dist/images/emoji.

    - emojiTail (string; optional):
        常用表情提示.

    - parse (boolean; optional):
        是否进行 md 解析，默认为True.

- htmlValue (string; optional):
    编辑器HTML内容.

- icon (a value equal to: 'ant', 'material'; default 'ant'):
    设置图标风格，可选的有：'ant'和'material'，默认为'ant'.

- image (dict; optional):
    图片配置.

    `image` is a dict with keys:

    - isPreview (boolean; optional):
        是否预览图片，默认为True.

- key (string; optional):
    辅助刷新用唯一标识key值.

- lang (a value equal to: 'en_US', 'fr_FR', 'pt_BR', 'ja_JP', 'ko_KR', 'ru_RU', 'sv_SE', 'zh_CN', 'zh_TW'; default 'zh_CN'):
    设置语言，可选的有：'en_US'、'fr_FR'、'pt_BR'、'ja_JP'、'ko_KR'、'ru_RU'、'sv_SE'、'zh_CN'和'zh_TW'，默认为'zh_CN'.

- link (dict; optional):
    链接配置.

    `link` is a dict with keys:

    - isOpen (boolean; optional):
        是否打开链接地址，默认为True.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- minHeight (number; optional):
    设置编辑区域最小高度.

- mode (a value equal to: 'wysiwyg', 'ir', 'sv'; default 'ir'):
    设置模式，可选的有：'sv'(分屏预览)、'ir'(即时渲染)和'wysiwyg'(所见即所得)，默认为'ir'(所见即所得).

- outline (dict; optional):
    大纲配置.

    `outline` is a dict with keys:

    - enable (boolean; optional):
        初始化是否展现大纲，默认值为False.

    - position (a value equal to: 'left', 'right'; optional):
        大纲位置，可选的值有'left'和'right'，默认值为'left'.

- placeholder (string; optional):
    设置输入区域为空时的提示.

- preview (dict; optional):
    预览配置.

    `preview` is a dict with keys:

    - actions (list of dicts; optional):
        平台类型配置.

        `actions` is a list of a value equal to: 'desktop', 'tablet',
        'mobile', 'mp-wechat', 'zhihu'

      Or dict with keys:

        - className (string; optional):

            按钮className 值.

        - key (string; optional):

            键名.

        - text (string; optional):

            按钮文本.

        - tooltip (string; optional):

            按钮提示信息.s

    - delay (number; optional):
        配置预览debounce毫秒间隔.

    - hljs (dict; optional):
        语言、样式等配置.

        `hljs` is a dict with keys:

        - defaultLang (string; optional):
            未指定语言时默认使用该语言.

        - enable (boolean; optional):
            是否启用代码高亮，默认为True.

        - langs (list of strings; optional):
            自定义指定语言.

        - lineNumber (boolean; optional):
            是否启用行号，默认为False.

        - style (a value equal to: 'abap', 'algol', 'algol_nu', 'api', 'arduino', 'autumn', 'average', 'base16-snazzy', 'borland', 'bw', 'catppuccin-frappe', 'catppuccin-latte', 'catppuccin-macchiato', 'catppuccin-mocha', 'colorful', 'compat', 'doom-one', 'doom-one2', 'dracula', 'emacs', 'friendly', 'fruity', 'github-dark', 'github', 'gruvbox-light', 'gruvbox', 'hr_high_contrast', 'hrdark', 'igor', 'lovelace', 'manni', 'modus-operandi', 'modus-vivendi', 'monokai', 'monokailight', 'murphy', 'native', 'nord', 'onedark', 'onesenterprise', 'paraiso-dark', 'paraiso-light', 'pastie', 'perldoc', 'pygments', 'rainbow_dash', 'rose-pine-dawn', 'rose-pine-moon', 'rose-pine', 'rrt', 'solarized-dark', 'solarized-dark256', 'solarized-light', 'swapoff', 'tango', 'tokyonight-day', 'tokyonight-moon', 'tokyonight-night', 'tokyonight-storm', 'trac', 'vim', 'vs', 'vulcan', 'witchhazel', 'xcode-dark', 'xcode'; optional):
            配置菜单字号选项，默认为'github'.

    - markdown (dict; optional):
        markdown配置.

        `markdown` is a dict with keys:

        - autoSpace (boolean; optional):
            是否开启自动空格，默认为False.

        - codeBlockPreview (boolean; optional):
            wysiwyg 和 ir 模式下是否对代码块进行渲染，默认为True.

        - fixTermTypo (boolean; optional):
            是否开启自动矫正术语，默认为False.

        - footnotes (boolean; optional):
            是否开启脚注，默认为True.

        - gfmAutoLink (boolean; optional):
            是否开启自动链接，默认为True.

        - linkBase (string; optional):
            链接相对路径前缀.

        - linkPrefix (string; optional):
            链接强制前缀.

        - listStyle (boolean; optional):
            是否为列表添加data-style属性，默认为False.

        - mark (boolean; optional):
            是否启用 mark 标记，默认为False.

        - mathBlockPreview (boolean; optional):
            wysiwyg 和 ir 模式下是否对数学公式进行渲染，默认为True.

        - paragraphBeginningSpace (boolean; optional):
            段落开头是否空两格，默认为False.

        - sanitize (boolean; optional):
            是否启用过滤 XSS，默认为True.

        - toc (boolean; optional):
            是否开启插入目录，默认为False.

    - math (dict; optional):
        数学公式配置.

        `math` is a dict with keys:

        - engine (a value equal to: 'KaTeX', 'MathJax'; optional):
            配置数学公式渲染引擎，可选的值有'KaTeX'和'MathJax'，默认为'KaTeX'.

        - inlineDigit (boolean; optional):
            内联数学公式起始 $ 后是否允许数字，默认为False.

        - macros (dict; optional):
            使用 MathJax 渲染时传入的宏定义.

        - mathJaxOptions (boolean | number | string | dict | list; optional):
            数学公式渲染引擎为MathJax时的参数.

    - maxWidth (number; optional):
        配置预览区域最大宽度.

    - mode (a value equal to: 'both', 'editor'; optional):
        配置显示模式，可选的有：'both'和'editor'，默认为'both'.

    - render (dict; optional):
        多媒体渲染配置.

        `render` is a dict with keys:

        - media (dict; optional)

            `media` is a dict with keys:

            - enable (boolean; optional):
                是否启用多媒体渲染，默认为True.

    - theme (dict; optional):
        主题配置.

        `theme` is a dict with keys:

        - current (string; optional):
            当前主题，默认为'light'.

        - list (dict; optional):
            可选主题列表，默认为{ \"ant-design\": \"Ant Design\", dark:
            \"Dark\", light: \"Light\", wechat: \"WeChat\" }.

        - path (string; optional):
            主题样式地址，默认为https://unpkg.com/vditor@${VDITOR_VERSION}/dist/css/content-theme.

    - url (string; optional):
        配置md解析请求.

- resize (dict; optional):
    拖拽配置.

    `resize` is a dict with keys:

    - enable (boolean; optional):
        是否支持大小拖拽，默认为False.

    - position (a value equal to: 'top', 'bottom'; optional):
        设置拖拽栏位置，可选的值有'top'和'bottom'，默认为'bottom'.

- resizeHeight (number; optional):
    开启大小拖拽后监听拖拽后的高度.

- selectedValue (string; optional):
    选中内容的字符串.

- style (dict; optional):
    设置组件的样式.

- tab (string; optional):
    设置tab键操作字符串，支持\t及任意字符串.

- theme (a value equal to: 'classic', 'dark'; default 'classic'):
    设置编辑器主题，可选的有：'classic'和'dark'，默认为'classic'.

- toolbar (default [    "emoji",    "headings",    "bold",    "italic",    "strike",    "link",    "|",    "list",    "ordered-list",    "check",    "outdent",    "indent",    "|",    "quote",    "line",    "code",    "inline-code",    "insert-before",    "insert-after",    "|",    "upload",    "record",    "table",    "|",    "undo",    "redo",    "|",    "fullscreen",    "edit-mode",    {        name: "more",        toolbar: [            "both",            "code-theme",            "content-theme",            "export",            "outline",            "preview"        ],    },]):
    设置工具栏.

- toolbarConfig (dict; default {    hide: False,    pin: False}):
    工具栏配置.

    `toolbarConfig` is a dict with keys:

    - hide (boolean; optional):
        是否隐藏工具栏，默认为False.

    - pin (boolean; optional):
        是否固定工具栏，默认为False.

- typewriterMode (boolean; default False):
    是否启用打字机模式，默认为False.

- undoDelay (number; optional):
    设置历史记录间隔.

- upload (dict; optional):
    上传配置.

    `upload` is a dict with keys:

    - accept (string; optional):
        文件上传类型，同https://www.w3schools.com/tags/att_input_accept.asp.

    - extraData (dict; optional):
        额外请求参数.

    - fieldName (string; optional):
        上传字段名称，默认值：file[].

    - headers (dict; optional):
        请求头设置.

    - linkToImgUrl (string; optional):
        剪切板中包含图片地址时，使用此 url 重新上传.

    - max (number; optional):
        上传文件最大 Byte，默认为10 * 1024 * 1024.

    - multiple (boolean; optional):
        是否允许多文件上传，默认值：True.

    - token (boolean | number | string | dict | list; optional):
        CORS 上传验证，头为 X-Upload-Token.

    - url (string; optional):
        上传 url，为空则不会触发上传相关事件.

    - withCredentials (boolean; optional):
        跨站点访问控制，默认为False.

- value (string; optional):
    编辑器md内容.

- width (string | number; optional):
    设置编辑器总宽度，支持%，，默认为'auto'.

- wordCount (number; optional):
    字数统计."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyVditor'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, debounceWait=Component.UNDEFINED, undoDelay=Component.UNDEFINED, height=Component.UNDEFINED, minHeight=Component.UNDEFINED, width=Component.UNDEFINED, placeholder=Component.UNDEFINED, lang=Component.UNDEFINED, tab=Component.UNDEFINED, typewriterMode=Component.UNDEFINED, cdn=Component.UNDEFINED, mode=Component.UNDEFINED, debuggerMode=Component.UNDEFINED, value=Component.UNDEFINED, theme=Component.UNDEFINED, icon=Component.UNDEFINED, toolbar=Component.UNDEFINED, toolbarConfig=Component.UNDEFINED, counter=Component.UNDEFINED, cache=Component.UNDEFINED, preview=Component.UNDEFINED, image=Component.UNDEFINED, link=Component.UNDEFINED, hint=Component.UNDEFINED, upload=Component.UNDEFINED, resize=Component.UNDEFINED, classes=Component.UNDEFINED, fullscreen=Component.UNDEFINED, outline=Component.UNDEFINED, htmlValue=Component.UNDEFINED, selectedValue=Component.UNDEFINED, wordCount=Component.UNDEFINED, resizeHeight=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'cache', 'cdn', 'className', 'classes', 'counter', 'debounceWait', 'debuggerMode', 'fullscreen', 'height', 'hint', 'htmlValue', 'icon', 'image', 'key', 'lang', 'link', 'loading_state', 'minHeight', 'mode', 'outline', 'placeholder', 'preview', 'resize', 'resizeHeight', 'selectedValue', 'style', 'tab', 'theme', 'toolbar', 'toolbarConfig', 'typewriterMode', 'undoDelay', 'upload', 'value', 'width', 'wordCount']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'cache', 'cdn', 'className', 'classes', 'counter', 'debounceWait', 'debuggerMode', 'fullscreen', 'height', 'hint', 'htmlValue', 'icon', 'image', 'key', 'lang', 'link', 'loading_state', 'minHeight', 'mode', 'outline', 'placeholder', 'preview', 'resize', 'resizeHeight', 'selectedValue', 'style', 'tab', 'theme', 'toolbar', 'toolbarConfig', 'typewriterMode', 'undoDelay', 'upload', 'value', 'width', 'wordCount']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyVditor, self).__init__(**args)
