# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyMarkdownEditor(Component):
    """A FefferyMarkdownEditor component.
markdown编辑器组件FefferyMarkdownEditor

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- debounceWait (number; optional):
    用于配置value变化更新的防抖等待时长（单位：毫秒）  默认值：`200`.

- value (string; optional):
    编辑器内容.

- html (string; optional):
    编辑器`html`格式内容.

- engine (dict; optional):
    解析引擎配置.

    `engine` is a dict with keys:

    - global (dict; optional):
        全局配置.

        `global` is a dict with keys:

        - classicBr (boolean; optional):
            是否启用经典换行逻辑，`True`：一个换行会被忽略，两个以上连续换行会分割成段落；`False`：
            一个换行会转成`<br>`，两个连续换行会分割成段落，三个以上连续换行会转成`<br>`并分割段落
            默认值：`False`.

        - htmlWhiteList (string; optional):
            额外允许渲染的`html`标签，标签以英文竖线分隔，如：`'iframe|script|style'`，需要注意：启用`ifram`e、`script`等标签后，会产生`xss`注入，请根据实际场景判断是否需要启用，一般编辑权限可控的场景（如`api`文档系统）可以允许`iframe`、`script`等标签
            默认值：`''`.

    - syntax (dict; optional):
        内置语法配置.

        `syntax` is a dict with keys:

        - link (dict; optional):
            `link`配置.

            `link` is a boolean

          Or dict with keys:

    - target (a value equal to: '', '_blank'; optional):
        生成的`<a>`标签追加`target`属性的默认值，`''`：在`<a>`标签里不会追加`target`属性，`'_blank'`：在`<a>`标签里追加`target=\"_blank\"`属性.

    - rel (a value equal to: '', 'nofollow'; optional):
        生成的`<a>`标签追加rel属性的默认值，`''`：在`<a>`标签里不会追加`rel`属性，`'nofollow'`：在`<a>`标签里追加`rel=\"nofollow`\"属性.

        - autoLink (dict; optional):
            `autoLink`配置.

            `autoLink` is a boolean

      Or dict with keys:

    - target (a value equal to: '', '_blank'; optional):
        生成的`<a>`标签追加`target`属性的默认值，`''`：在`<a>`标签里不会追加`target`属性，`'_blank'`：在`<a>`标签里追加`target=\"_blank\"`属性.

    - rel (a value equal to: '', 'nofollow'; optional):
        生成的`<a>`标签追加rel属性的默认值，`''`：在`<a>`标签里不会追加`rel`属性，`'nofollow'`：在`<a>`标签里追加`rel=\"nofollow`\"属性.

    - enableShortLink (boolean; optional):
        是否开启短链接.

    - shortLinkLength (number; optional):
        短链接长度.

        - list (dict; optional):
            `list`配置.

            `list` is a boolean | dict with keys:

    - listNested (boolean; optional):
        同级列表类型转换后变为子级.

    - indentSpace (number; optional):
        默认`2`个空格缩进.

        - table (dict; optional):
            `table`配置.

            `table` is a boolean | dict with keys:

    - enableChart (boolean; optional)

        - inlineCode (dict; optional):
            `inlineCode`配置.

            `inlineCode` is a boolean | dict with keys:

    - theme (string; optional)

        - codeBlock (dict; optional):
            `codeBlock`配置.

            `codeBlock` is a boolean | dict with keys:

    - theme (string; optional):
        默认为深色主题`'dark'`.

    - wrap (boolean; optional):
        超出长度是否换行，`False`则显示滚动条  默认值：`True`.

    - lineNumber (boolean; optional):
        是否显示行号  默认值：`True`.

    - copyCode (boolean; optional):
        是否显示复制按钮  默认值：`True`.

    - editCode (boolean; optional):
        是否显示编辑按钮  默认值：`True`.

    - changeLang (boolean; optional):
        是否显示切换语言按钮  默认值：`True`.

    - indentedCodeBlock (boolean; optional):
        是否启用缩进代码块  默认值：`True`.

        - emoji (dict; optional):
            `emoji`配置.

            `emoji` is a boolean | dict with keys:

    - useUnicode (boolean; optional):
        是否使用`unicode`进行渲染  默认值：`True`.

        - fontEmphasis (dict; optional):
            `fontEmphasis`配置.

            `fontEmphasis` is a boolean | dict with keys:

    - allowWhitespace (boolean; optional):
        是否允许首尾空格，首尾、前后的定义：语法前**语法首+内容+语法尾**语法后<br/>  例：<br/>
        &emsp;`True`:<br/>            &emsp;&emsp;__ hello __  ====>
        <strong> hello </strong><br/>            &emsp;&emsp;__hello__
        ====>   <strong>hello</strong><br/>     &emsp;`False`:<br/>
        &emsp;&emsp;__ hello __  ====>   <em>_ hello _</em><br/>
        &emsp;&emsp;__hello__    ====>   <strong>hello</strong><br/>
        默认值：`False`.

        - strikethrough (dict; optional):
            `strikethrough`配置.

            `strikethrough` is a boolean | dict with keys:

    - needWhitespace (boolean; optional):
        是否必须有前后空格，首尾、前后的定义： 语法前**语法首+内容+语法尾**语法后<br/>  例：<br/>
        &emsp;`True`:<br/>             &emsp;&emsp;hello wor~~l~~d
        ====>   hello wor~~l~~d<br/>             &emsp;&emsp;hello wor
        ~~l~~ d   ====>   hello wor <del>l</del> d<br/>
        &emsp;`False`:<br/>             &emsp;&emsp;hello wor~~l~~d
        ====>   hello wor<del>l</del>d<br/>
        &emsp;&emsp;hello wor ~~l~~ d     ====>   hello wor
        <del>l</del> d<br/>  默认值：`False`.

        - mathBlock (dict; optional):
            `mathBlock`配置.

            `mathBlock` is a boolean | dict with keys:

    - engine (a value equal to: 'katex', 'MathJax'; optional):
        `'katex'`或`'MathJax'`  默认值：`'MathJax'`.

    - src (string; optional)

    - plugins (boolean; optional):
        是否加载插件  默认值：`True`.

        - inlineMath (dict; optional):
            `inlineMath`配置.

            `inlineMath` is a boolean | dict with keys:

    - engine (a value equal to: 'katex', 'MathJax'; optional):
        `'katex'`或`'MathJax'`  默认值：`'MathJax'`.

    - src (string; optional)

        - toc (dict; optional):
            `toc`配置.

            `toc` is a boolean | dict with keys:

    - allowMultiToc (boolean; optional):
        是否渲染多个目录，`False`表示只渲染一个目录  默认值：`False`.

        - header (dict; optional):
            `header`配置.

            `header` is a boolean | dict with keys:

    - anchorStyle (a value equal to: 'default', 'autonumber', 'none'; optional):
        标题的样式：`'default'`默认样式，标题前面有锚点，`'autonumber'`标题前面有自增序号锚点，`'none'`标题没有锚点
        默认值：`'default'`.

- editor (dict; optional):
    编辑器配置.

    `editor` is a dict with keys:

    - id (string; optional):
        `textarea`的`id`属性值.

    - name (string; optional):
        `textarea`的`name`属性值.

    - autoSave2Textarea (boolean; optional):
        是否自动将编辑区的内容回写到`textarea`里  默认值：`False`.

    - theme (string; optional):
        depend on codemirror theme name:
        `https://codemirror.net/demo/theme.htm`  默认值：'default'.

    - height (string; optional):
        编辑器的高度，如果挂载点存在内联设置的`height`则以内联样式为主  默认值：`100%`.

    - defaultModel (a value equal to: 'edit&preview', 'editOnly', 'previewOnly'; optional):
        编辑器初始化后的默认模式，`'edit&preview'`: 双栏编辑预览模式，`'editOnly'`:
        纯编辑模式（没有预览，可通过`toolbar`切换成双栏或预览模式），`'previewOnly'`:
        预览模式（没有编辑框，`toolbar`只显示“返回编辑”按钮，可通过`toolbar`切换成编辑模式）
        默认值：`'edit&preview'`.

    - convertWhenPaste (boolean; optional):
        粘贴时是否自动将`html`转成`markdown`  默认值：`True`.

    - codemirror (dict; optional)

        `codemirror` is a dict with keys:

        - autofocus (boolean; optional):
            是否自动`focus`  默认值：`True`.

    - writingStyle (a value equal to: 'normal', 'typewriter', 'focus'; optional):
        书写风格，`'normal'`普通，`'typewriter'`打字机，`'focus'`专注  默认`'normal'`.

    - keepDocumentScrollAfterInit (boolean; optional):
        在初始化后是否保持网页的滚动，`True`：保持滚动；`False`：网页自动滚动到编辑器初始化的位置
        默认值：`False`.

- toolbars (dict; optional):
    工具栏配置.

    `toolbars` is a dict with keys:

    - theme (a value equal to: 'light', 'dark'; optional):
        主题，可选的值为`'light'`、`'dark'`  默认值：`'light'`.

    - showToolbar (boolean; optional):
        是否展示顶部工具栏  默认值：`True`.

    - toolbar (list of dicts; optional):
        顶部工具栏配置.

        `toolbar` is a list of a value equal to: '|', 'bold',
        'italic', 'underline', 'strikethrough', 'sub', 'sup', 'ruby',
        'size', 'color', 'quote', 'detail', 'h1', 'h2', 'h3',
        'header', 'ul', 'ol', 'checklist', 'list', 'justify', 'panel',
        'image', 'audio', 'video', 'pdf', 'word', 'file', 'link',
        'hr', 'br', 'code', 'formula', 'toc', 'table', 'drawIo',
        'graph', 'undo', 'redo', 'theme', 'codeTheme',
        'mobilePreview', 'togglePreview', 'switchModel', 'copy',
        'export', 'fullScreen', 'settings'

      Or dict with keys:

        - insert (list of a value equal to: 'bold', 'italic', 'underline', 'strikethrough', 'sub', 'sup', 'ruby', 'quote', 'detail', 'h1', 'h2', 'h3', 'ul', 'ol', 'checklist', 'image', 'audio', 'video', 'pdf', 'word', 'file', 'link', 'hr', 'br', 'code', 'formula', 'toc', 'table', 'drawIo', 'undo', 'redo', 'mobilePreview', 'togglePreview', 'switchModel', 'copy', 'fullScreen's; optional)s

    - toolbarRight (list; optional):
        顶部右侧工具栏配置.

    - sidebar (list; optional):
        侧边栏配置.

    - bubble (boolean | list of a value equal to: '|', 'bold', 'italic', 'underline', 'strikethrough', 'sub', 'sup', 'ruby', 'size', 'color', 'quote', 'detail', 'h1', 'h2', 'h3', 'header', 'ul', 'ol', 'checklist', 'list', 'justify', 'panel', 'image', 'audio', 'video', 'pdf', 'word', 'file', 'link', 'hr', 'br', 'code', 'formula', 'toc', 'table', 'drawIo', 'graph', 'undo', 'redo', 'theme', 'codeTheme', 'mobilePreview', 'togglePreview', 'switchModel', 'copy', 'export', 'fullScreen', 'settings's; optional):
        选中文字时弹出的悬浮工具栏配置.

    - float (boolean | list of a value equal to: '|', 'bold', 'italic', 'underline', 'strikethrough', 'sub', 'sup', 'ruby', 'size', 'color', 'quote', 'detail', 'h1', 'h2', 'h3', 'header', 'ul', 'ol', 'checklist', 'list', 'justify', 'panel', 'image', 'audio', 'video', 'pdf', 'word', 'file', 'link', 'hr', 'br', 'code', 'formula', 'toc', 'table', 'drawIo', 'graph', 'undo', 'redo', 'theme', 'codeTheme', 'mobilePreview', 'togglePreview', 'switchModel', 'copy', 'export', 'fullScreen', 'settings's; optional):
        光标出现在行首位置时出现的提示工具栏配置.

    - shortcutKey (dict; optional):
        快捷键配置，如果配置为空，则使用`toolbar`的配置，例如：`{'Alt-1': 'header', 'Alt-2':
        'header', 'Ctrl-b': 'bold', 'Ctrl-Alt-m': 'formula'}`.

    - config (dict; optional):
        一些按钮的配置信息.

        `config` is a dict with keys:

        - formula (dict; optional)

            `formula` is a dict with keys:

            - showLatexLive (boolean; optional):
                `True`: 显示`www.latexlive.com`外链；`False`：不显示
                默认值：`True`.

            - templateConfig (boolean; optional):
                `False`: 使用默认模板  默认值：`False`.

- drawioIframeUrl (string; optional):
    打开`draw.io`编辑页的`url`，如果为空则`drawio`按钮失效.

- fileTypeLimitMap (dict; optional):
    上传文件的时候用来指定文件类型.

    `fileTypeLimitMap` is a dict with keys:

    - video (string; optional)

    - audio (string; optional)

    - image (string; optional)

    - word (string; optional)

    - pdf (string; optional)

    - file (string; optional)

- uploadConfig (dict; optional):
    设置文件上传相关信息.

    `uploadConfig` is a dict with keys:

    - action (string; optional):
        设置上传的地址.

    - headers (dict; optional):
        设置上传的请求头部.

    - data (dict; optional):
        设置上传时附带的额外参数.

    - withCredentials (boolean; optional):
        设置是否支持发送cookie凭证信息  默认值：`False`.

    - filename (string; optional):
        设置上传的文件字段名.

    - responseUrl (string; optional):
        设置上传接口响应中`url`的层级，如响应结果格式为`{data: {url:
        'xxx'}}`，则配置为`'data.url'`  默认值：`'data.url'`.

- fineControl (dict; optional):
    配置文件展示精细化控制，此功能只在配置了上传接口的情况下生效.

    `fineControl` is a dict with keys:

    - isOpen (boolean; optional):
        是否启用.

    - videoFineControlOptions (dict; optional):
        视频文件精细化控制选项.

        `videoFineControlOptions` is a dict with keys:

        - name (string; optional):
            视频文件的名称.

        - isPoster (boolean; optional):
            是否启用视频文件封面  默认值：`False`.

        - posterUrl (string; optional):
            自定义视频文件封面地址，如果不设置，则默认为视频文件地址.

        - isBorder (boolean; optional):
            是否显示边框  默认值：`False`.

        - isShadow (boolean; optional):
            是否显示阴影  默认`False`.

        - isRadius (boolean; optional):
            是否显示圆角  默认`False`.

    - imageFineControlOptions (dict; optional):
        图片文件精细化控制选项.

        `imageFineControlOptions` is a dict with keys:

        - name (string; optional):
            图片文件的名称.

        - isBorder (boolean; optional):
            是否显示边框  默认`False`.

        - isShadow (boolean; optional):
            是否显示阴影  默认`False`.

        - isRadius (boolean; optional):
            是否显示圆角  默认`False`.

        - width (string; optional):
            图片的宽度，可配置百分比，也可配置像素值  默认`'100%'`.

        - height (string; optional):
            图片的高度  默认`'auto'`.

- previewer (dict; optional):
    预览区域配置.

    `previewer` is a dict with keys:

    - dom (boolean; optional)

    - className (string; optional)

    - enablePreviewerBubble (boolean; optional):
        是否启用预览区域编辑能力（目前支持编辑图片尺寸、编辑表格内容）  默认值：`True`.

    - lazyLoadImg (dict; optional):
        配置图片懒加载的逻辑：如果不希望图片懒加载，可配置成`lazyLoadImg = {noLoadImgNum:
        -1}`<br/>  如果希望所有图片都无脑懒加载，可配置成`lazyLoadImg = {noLoadImgNum: 0,
        autoLoadImgNum: -1}`<br/>
        如果一共有15张图片，希望：1、前5张图片（1~5）直接加载；2、后5张图片（6~10）不论在不在视区内，都无脑懒加载；3、其他图片（11~15）在视区内时，进行懒加载；则配置应该为`lazyLoadImg
        = {noLoadImgNum: 5, autoLoadImgNum: 5}`.

        `lazyLoadImg` is a dict with keys:

        - loadingImgPath (string; optional):
            加载图片时如果需要展示`loading`图，则配`置`loading`图的地址.

        - maxNumPerTime (number; optional):
            同一时间最多有几个图片请求，最大同时加载`6`张图片.

        - noLoadImgNum (number; optional):
            不进行懒加载处理的图片数量，如果为`0`，即所有图片都进行懒加载处理，如果设置为`-1`，则所有图片都不进行懒加载处理.

        - autoLoadImgNum (number; optional):
            首次自动加载几张图片（不论图片是否滚动到视野内），`autoLoadImgNum =
            -1`表示会自动加载完所有图片.

        - maxTryTimesPerSrc (number; optional):
            针对加载失败的图片或`beforeLoadOneImgCallback`返回`False`的图片，最多尝试加载几次，为了防止死循环，最多`5`次，以图片的`src`为纬度统计重试次数.

- theme (list of dicts; optional):
    配置主题，第三方可以自行扩展主题.

    `theme` is a list of dicts with keys:

    - className (a value equal to: 'default', 'dark', 'light', 'green', 'red', 'violet', 'blue'; optional)

    - label (a value equal to: '默认', '暗黑', '明亮', '清新', '热情', '淡雅', '清幽'; optional)

- isPreviewOnly (boolean; optional):
    预览页面是否需要绑定事件  默认值：`False`.

- autoScrollByCursor (boolean; optional):
    预览区域是否跟随编辑器光标自动滚动  默认值：`True`.

- forceAppend (boolean; optional):
    外层容器不存在时，是否强制输出到`body`上  默认值：`True`.

- locale (a value equal to: 'zh_CN', 'en_US'; optional):
    语言设置，可选的有`'zh_CN'`、`'en_US'`  默认值：`'zh_CN'`.

- autoScrollByHashAfterInit (boolean; optional):
    编辑器初始化后是否检查`location.hash`尝试滚动到对应位置  默认值：`False`.

- customSyntax (list of dicts; optional):
    自定义语法.

    `customSyntax` is a list of dicts with keys:

    - syntaxName (string; optional):
        自定义语法名称.

    - force (boolean; optional):
        是否用自定义的语法覆盖默认语法  默认值：`False`.

    - before (string; optional):
        定义该自定义语法在什么语法之前执行.

    - syntaxType (a value equal to: 'inline', 'block'; optional):
        自定义语法类型，`'inline'`表示行内语法，`'block'`表示段落语法.

    - reg (string; optional):
        自定义语法的正则表达式.

    - result (string; optional):
        自定义语法的渲染结果."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyMarkdownEditor'
    EngineGlobal = TypedDict(
        "EngineGlobal",
            {
            "classicBr": NotRequired[bool],
            "htmlWhiteList": NotRequired[str]
        }
    )

    EngineSyntaxLink = TypedDict(
        "EngineSyntaxLink",
            {
            "target": NotRequired[Literal["", "_blank"]],
            "rel": NotRequired[Literal["", "nofollow"]]
        }
    )

    EngineSyntaxAutoLink = TypedDict(
        "EngineSyntaxAutoLink",
            {
            "target": NotRequired[Literal["", "_blank"]],
            "rel": NotRequired[Literal["", "nofollow"]],
            "enableShortLink": NotRequired[bool],
            "shortLinkLength": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    EngineSyntaxList = TypedDict(
        "EngineSyntaxList",
            {
            "listNested": NotRequired[bool],
            "indentSpace": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    EngineSyntaxTable = TypedDict(
        "EngineSyntaxTable",
            {
            "enableChart": NotRequired[bool]
        }
    )

    EngineSyntaxInlineCode = TypedDict(
        "EngineSyntaxInlineCode",
            {
            "theme": NotRequired[str]
        }
    )

    EngineSyntaxCodeBlock = TypedDict(
        "EngineSyntaxCodeBlock",
            {
            "theme": NotRequired[str],
            "wrap": NotRequired[bool],
            "lineNumber": NotRequired[bool],
            "copyCode": NotRequired[bool],
            "editCode": NotRequired[bool],
            "changeLang": NotRequired[bool],
            "indentedCodeBlock": NotRequired[bool]
        }
    )

    EngineSyntaxEmoji = TypedDict(
        "EngineSyntaxEmoji",
            {
            "useUnicode": NotRequired[bool]
        }
    )

    EngineSyntaxFontEmphasis = TypedDict(
        "EngineSyntaxFontEmphasis",
            {
            "allowWhitespace": NotRequired[bool]
        }
    )

    EngineSyntaxStrikethrough = TypedDict(
        "EngineSyntaxStrikethrough",
            {
            "needWhitespace": NotRequired[bool]
        }
    )

    EngineSyntaxMathBlock = TypedDict(
        "EngineSyntaxMathBlock",
            {
            "engine": NotRequired[Literal["katex", "MathJax"]],
            "src": NotRequired[str],
            "plugins": NotRequired[bool]
        }
    )

    EngineSyntaxInlineMath = TypedDict(
        "EngineSyntaxInlineMath",
            {
            "engine": NotRequired[Literal["katex", "MathJax"]],
            "src": NotRequired[str]
        }
    )

    EngineSyntaxToc = TypedDict(
        "EngineSyntaxToc",
            {
            "allowMultiToc": NotRequired[bool]
        }
    )

    EngineSyntaxHeader = TypedDict(
        "EngineSyntaxHeader",
            {
            "anchorStyle": NotRequired[Literal["default", "autonumber", "none"]]
        }
    )

    EngineSyntax = TypedDict(
        "EngineSyntax",
            {
            "link": NotRequired[typing.Union[bool, "EngineSyntaxLink"]],
            "autoLink": NotRequired[typing.Union[bool, "EngineSyntaxAutoLink"]],
            "list": NotRequired[typing.Union[bool, "EngineSyntaxList"]],
            "table": NotRequired[typing.Union[bool, "EngineSyntaxTable"]],
            "inlineCode": NotRequired[typing.Union[bool, "EngineSyntaxInlineCode"]],
            "codeBlock": NotRequired[typing.Union[bool, "EngineSyntaxCodeBlock"]],
            "emoji": NotRequired[typing.Union[bool, "EngineSyntaxEmoji"]],
            "fontEmphasis": NotRequired[typing.Union[bool, "EngineSyntaxFontEmphasis"]],
            "strikethrough": NotRequired[typing.Union[bool, "EngineSyntaxStrikethrough"]],
            "mathBlock": NotRequired[typing.Union[bool, "EngineSyntaxMathBlock"]],
            "inlineMath": NotRequired[typing.Union[bool, "EngineSyntaxInlineMath"]],
            "toc": NotRequired[typing.Union[bool, "EngineSyntaxToc"]],
            "header": NotRequired[typing.Union[bool, "EngineSyntaxHeader"]]
        }
    )

    Engine = TypedDict(
        "Engine",
            {
            "global": NotRequired["EngineGlobal"],
            "syntax": NotRequired["EngineSyntax"]
        }
    )

    EditorCodemirror = TypedDict(
        "EditorCodemirror",
            {
            "autofocus": NotRequired[bool]
        }
    )

    Editor = TypedDict(
        "Editor",
            {
            "id": NotRequired[str],
            "name": NotRequired[str],
            "autoSave2Textarea": NotRequired[bool],
            "theme": NotRequired[str],
            "height": NotRequired[str],
            "defaultModel": NotRequired[Literal["edit&preview", "editOnly", "previewOnly"]],
            "convertWhenPaste": NotRequired[bool],
            "codemirror": NotRequired["EditorCodemirror"],
            "writingStyle": NotRequired[Literal["normal", "typewriter", "focus"]],
            "keepDocumentScrollAfterInit": NotRequired[bool]
        }
    )

    ToolbarsToolbar = TypedDict(
        "ToolbarsToolbar",
            {
            "insert": NotRequired[typing.Sequence[Literal["bold", "italic", "underline", "strikethrough", "sub", "sup", "ruby", "quote", "detail", "h1", "h2", "h3", "ul", "ol", "checklist", "image", "audio", "video", "pdf", "word", "file", "link", "hr", "br", "code", "formula", "toc", "table", "drawIo", "undo", "redo", "mobilePreview", "togglePreview", "switchModel", "copy", "fullScreen"]]]
        }
    )

    ToolbarsConfigFormula = TypedDict(
        "ToolbarsConfigFormula",
            {
            "showLatexLive": NotRequired[bool],
            "templateConfig": NotRequired[bool]
        }
    )

    ToolbarsConfig = TypedDict(
        "ToolbarsConfig",
            {
            "formula": NotRequired["ToolbarsConfigFormula"]
        }
    )

    Toolbars = TypedDict(
        "Toolbars",
            {
            "theme": NotRequired[Literal["light", "dark"]],
            "showToolbar": NotRequired[bool],
            "toolbar": NotRequired[typing.Sequence[typing.Union[Literal["|", "bold", "italic", "underline", "strikethrough", "sub", "sup", "ruby", "size", "color", "quote", "detail", "h1", "h2", "h3", "header", "ul", "ol", "checklist", "list", "justify", "panel", "image", "audio", "video", "pdf", "word", "file", "link", "hr", "br", "code", "formula", "toc", "table", "drawIo", "graph", "undo", "redo", "theme", "codeTheme", "mobilePreview", "togglePreview", "switchModel", "copy", "export", "fullScreen", "settings"], "ToolbarsToolbar"]]],
            "toolbarRight": NotRequired[typing.Sequence],
            "sidebar": NotRequired[typing.Sequence],
            "bubble": NotRequired[typing.Union[bool, typing.Sequence[Literal["|", "bold", "italic", "underline", "strikethrough", "sub", "sup", "ruby", "size", "color", "quote", "detail", "h1", "h2", "h3", "header", "ul", "ol", "checklist", "list", "justify", "panel", "image", "audio", "video", "pdf", "word", "file", "link", "hr", "br", "code", "formula", "toc", "table", "drawIo", "graph", "undo", "redo", "theme", "codeTheme", "mobilePreview", "togglePreview", "switchModel", "copy", "export", "fullScreen", "settings"]]]],
            "float": NotRequired[typing.Union[bool, typing.Sequence[Literal["|", "bold", "italic", "underline", "strikethrough", "sub", "sup", "ruby", "size", "color", "quote", "detail", "h1", "h2", "h3", "header", "ul", "ol", "checklist", "list", "justify", "panel", "image", "audio", "video", "pdf", "word", "file", "link", "hr", "br", "code", "formula", "toc", "table", "drawIo", "graph", "undo", "redo", "theme", "codeTheme", "mobilePreview", "togglePreview", "switchModel", "copy", "export", "fullScreen", "settings"]]]],
            "shortcutKey": NotRequired[dict],
            "config": NotRequired["ToolbarsConfig"]
        }
    )

    FileTypeLimitMap = TypedDict(
        "FileTypeLimitMap",
            {
            "video": NotRequired[str],
            "audio": NotRequired[str],
            "image": NotRequired[str],
            "word": NotRequired[str],
            "pdf": NotRequired[str],
            "file": NotRequired[str]
        }
    )

    UploadConfig = TypedDict(
        "UploadConfig",
            {
            "action": NotRequired[str],
            "headers": NotRequired[dict],
            "data": NotRequired[dict],
            "withCredentials": NotRequired[bool],
            "filename": NotRequired[str],
            "responseUrl": NotRequired[str]
        }
    )

    FineControlVideoFineControlOptions = TypedDict(
        "FineControlVideoFineControlOptions",
            {
            "name": NotRequired[str],
            "isPoster": NotRequired[bool],
            "posterUrl": NotRequired[str],
            "isBorder": NotRequired[bool],
            "isShadow": NotRequired[bool],
            "isRadius": NotRequired[bool]
        }
    )

    FineControlImageFineControlOptions = TypedDict(
        "FineControlImageFineControlOptions",
            {
            "name": NotRequired[str],
            "isBorder": NotRequired[bool],
            "isShadow": NotRequired[bool],
            "isRadius": NotRequired[bool],
            "width": NotRequired[str],
            "height": NotRequired[str]
        }
    )

    FineControl = TypedDict(
        "FineControl",
            {
            "isOpen": NotRequired[bool],
            "videoFineControlOptions": NotRequired["FineControlVideoFineControlOptions"],
            "imageFineControlOptions": NotRequired["FineControlImageFineControlOptions"]
        }
    )

    PreviewerLazyLoadImg = TypedDict(
        "PreviewerLazyLoadImg",
            {
            "loadingImgPath": NotRequired[str],
            "maxNumPerTime": NotRequired[typing.Union[int, float, numbers.Number]],
            "noLoadImgNum": NotRequired[typing.Union[int, float, numbers.Number]],
            "autoLoadImgNum": NotRequired[typing.Union[int, float, numbers.Number]],
            "maxTryTimesPerSrc": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    Previewer = TypedDict(
        "Previewer",
            {
            "dom": NotRequired[bool],
            "className": NotRequired[str],
            "enablePreviewerBubble": NotRequired[bool],
            "lazyLoadImg": NotRequired["PreviewerLazyLoadImg"]
        }
    )

    Theme = TypedDict(
        "Theme",
            {
            "className": NotRequired[Literal["default", "dark", "light", "green", "red", "violet", "blue"]],
            "label": NotRequired[Literal["\u9ed8\u8ba4", "\u6697\u9ed1", "\u660e\u4eae", "\u6e05\u65b0", "\u70ed\u60c5", "\u6de1\u96c5", "\u6e05\u5e7d"]]
        }
    )

    CustomSyntax = TypedDict(
        "CustomSyntax",
            {
            "syntaxName": NotRequired[str],
            "force": NotRequired[bool],
            "before": NotRequired[str],
            "syntaxType": NotRequired[Literal["inline", "block"]],
            "reg": NotRequired[str],
            "result": NotRequired[str]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        debounceWait: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        value: typing.Optional[str] = None,
        html: typing.Optional[str] = None,
        engine: typing.Optional["Engine"] = None,
        editor: typing.Optional["Editor"] = None,
        toolbars: typing.Optional["Toolbars"] = None,
        drawioIframeUrl: typing.Optional[str] = None,
        fileTypeLimitMap: typing.Optional["FileTypeLimitMap"] = None,
        uploadConfig: typing.Optional["UploadConfig"] = None,
        fineControl: typing.Optional["FineControl"] = None,
        previewer: typing.Optional["Previewer"] = None,
        theme: typing.Optional[typing.Sequence["Theme"]] = None,
        isPreviewOnly: typing.Optional[bool] = None,
        autoScrollByCursor: typing.Optional[bool] = None,
        forceAppend: typing.Optional[bool] = None,
        locale: typing.Optional[Literal["zh_CN", "en_US"]] = None,
        autoScrollByHashAfterInit: typing.Optional[bool] = None,
        customSyntax: typing.Optional[typing.Sequence["CustomSyntax"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'debounceWait', 'value', 'html', 'engine', 'editor', 'toolbars', 'drawioIframeUrl', 'fileTypeLimitMap', 'uploadConfig', 'fineControl', 'previewer', 'theme', 'isPreviewOnly', 'autoScrollByCursor', 'forceAppend', 'locale', 'autoScrollByHashAfterInit', 'customSyntax']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'debounceWait', 'value', 'html', 'engine', 'editor', 'toolbars', 'drawioIframeUrl', 'fileTypeLimitMap', 'uploadConfig', 'fineControl', 'previewer', 'theme', 'isPreviewOnly', 'autoScrollByCursor', 'forceAppend', 'locale', 'autoScrollByHashAfterInit', 'customSyntax']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyMarkdownEditor, self).__init__(**args)
