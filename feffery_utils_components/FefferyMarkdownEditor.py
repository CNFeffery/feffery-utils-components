# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyMarkdownEditor(Component):
    """A FefferyMarkdownEditor component.


Keyword arguments:

- id (string; optional):
    组件id.

- autoScrollByCursor (boolean; default True):
    预览区域是否跟随编辑器光标自动滚动，默认为True.

- autoScrollByHashAfterInit (boolean; default False):
    编辑器初始化后是否检查 location.hash 尝试滚动到对应位置，默认为False.

- className (string; optional):
    css类名.

- customSyntax (list of dicts; optional):
    自定义语法.

    `customSyntax` is a list of dicts with keys:

    - before (string; optional):
        定义该自定义语法在什么语法之前执行.

    - force (boolean; optional):
        是否用自定义的语法覆盖默认语法，默认为False.

    - reg (string; optional):
        自定义语法的正则表达式.

    - result (string; optional):
        自定义语法的渲染结果.

    - syntaxName (string; optional):
        自定义语法名称.

    - syntaxType (a value equal to: 'inline', 'block'; optional):
        自定义语法类型，'inline'表示行内语法，'block'表示段落语法.

- drawioIframeUrl (string; default ''):
    打开draw.io编辑页的url，如果为空则drawio按钮失效.

- editor (dict; default {    id: 'code',    name: 'code',    autoSave2Textarea: False,    theme: 'default',    height: '100%',    defaultModel: 'edit&preview',    convertWhenPaste: True,    codemirror: {        autofocus: True,    },    writingStyle: 'normal',    keepDocumentScrollAfterInit: False,}):
    编辑器配置.

    `editor` is a dict with keys:

    - autoSave2Textarea (boolean; optional):
        是否自动将编辑区的内容回写到textarea里，默认为False.

    - codemirror (dict; optional)

        `codemirror` is a dict with keys:

        - autofocus (boolean; optional):
            是否自动focus 默认为True.

    - convertWhenPaste (boolean; optional):
        粘贴时是否自动将html转成markdown，默认为True.

    - defaultModel (a value equal to: 'edit&preview', 'editOnly', 'previewOnly'; optional):
        编辑器初始化后的默认模式，一共有三种模式：1、双栏编辑预览模式；2、纯编辑模式；3、预览模式。  edit&preview:
        双栏编辑预览模式,  editOnly: 纯编辑模式（没有预览，可通过toolbar切换成双栏或预览模式）,
        previewOnly: 预览模式（没有编辑框，toolbar只显示“返回编辑”按钮，可通过toolbar切换成编辑模式），
        默认为'edit&preview'.

    - height (string; optional):
        编辑器的高度，默认100%，如果挂载点存在内联设置的height则以内联样式为主.

    - id (string; optional):
        textarea 的id属性值.

    - keepDocumentScrollAfterInit (boolean; optional):
        在初始化后是否保持网页的滚动，True：保持滚动；False：网页自动滚动到编辑器初始化的位置，默认为False.

    - name (string; optional):
        textarea 的name属性值.

    - theme (string; optional):
        depend on codemirror theme name:
        https://codemirror.net/demo/theme.htm，默认为'default'.

    - writingStyle (a value equal to: 'normal', 'typewriter', 'focus'; optional):
        书写风格，normal 普通 | typewriter 打字机 | focus 专注，默认'normal'.

- engine (dict; default {    global: {        classicBr: False,        htmlWhiteList: '',    },    syntax: {        link: {            target: '',            rel: '',        },        autoLink: {            target: '',            rel: '',            enableShortLink: True,            shortLinkLength: 20,        },        list: {            listNested: False,            indentSpace: 2,        },        inlineCode: {            theme: 'red',        },        codeBlock: {            theme: 'dark',            wrap: True,            lineNumber: True,            copyCode: True,            editCode: True,            changeLang: True,            indentedCodeBlock: True,        },        emoji: {            useUnicode: True,        },        fontEmphasis: {            allowWhitespace: False,        },        strikethrough: {            needWhitespace: False,        },        mathBlock: {            engine: 'MathJax',            src: '',            plugins: True,        },        inlineMath: {            engine: 'MathJax',            src: '',        },        toc: {            allowMultiToc: False,        },        header: {            anchorStyle: 'default',        },    },}):
    解析引擎配置.

    `engine` is a dict with keys:

    - global (dict; optional):
        全局配置.

        `global` is a dict with keys:

        - classicBr (boolean; optional):
            是否启用经典换行逻辑,  True：一个换行会被忽略，两个以上连续换行会分割成段落，  False：
            一个换行会转成<br>，两个连续换行会分割成段落，三个以上连续换行会转成<br>并分割段落,  默认为False.

        - htmlWhiteList (string; optional):
            额外允许渲染的html标签  标签以英文竖线分隔，如：htmlWhiteList:
            'iframe|script|style'
            默认为空，默认允许渲染的html见src/utils/sanitize.js whiteList 属性  需要注意：
               - 启用iframe、script等标签后，会产生xss注入，请根据实际场景判断是否需要启用     -
            一般编辑权限可控的场景（如api文档系统）可以允许iframe、script等标签.

    - syntax (dict; optional):
        内置语法配置.

        `syntax` is a dict with keys:

        - autoLink (dict; optional)

            `autoLink` is a boolean

          Or dict with keys:

    - enableShortLink (boolean; optional):
        是否开启短链接.

    - rel (a value equal to: '', 'nofollow'; optional):
        生成的<a>标签追加rel属性的默认值 空：在<a>标签里不会追加rel属性，
        nofollow：在<a>标签里追加rel=\"nofollow：在\"属性.

    - shortLinkLength (number; optional):
        短链接长度.

    - target (a value equal to: '', '_blank'; optional):
        生成的<a>标签追加target属性的默认值 空：在<a>标签里不会追加target属性，
        _blank：在<a>标签里追加target=\"_blank\"属性.

        - codeBlock (dict; optional)

            `codeBlock` is a boolean

      Or dict with keys:

    - changeLang (boolean; optional):
        是否显示切换语言按钮，默认为True.

    - copyCode (boolean; optional):
        是否显示复制按钮，默认为True.

    - editCode (boolean; optional):
        是否显示编辑按钮，默认为True.

    - indentedCodeBlock (boolean; optional):
        是否启用缩进代码块，默认为True.

    - lineNumber (boolean; optional):
        是否显示行号，默认为True.

    - theme (string; optional):
        默认为深色主题'dark'.

    - wrap (boolean; optional):
        超出长度是否换行，False则显示滚动条，默认为True.

        - emoji (dict; optional)

            `emoji` is a boolean | dict with keys:

    - useUnicode (boolean; optional):
        是否使用unicode进行渲染，默认为True.

        - fontEmphasis (dict; optional)

            `fontEmphasis` is a boolean | dict with keys:

    - allowWhitespace (boolean; optional):
        是否允许首尾空格  首尾、前后的定义： 语法前**语法首+内容+语法尾**语法后  例：     True:
        __ hello __  ====>   <strong> hello </strong>
        __hello__    ====>   <strong>hello</strong>     False:
        __ hello __  ====>   <em>_ hello _</em>            __hello__
        ====>   <strong>hello</strong>   默认为False.

        - header (dict; optional)

            `header` is a boolean | dict with keys:

    - anchorStyle (a value equal to: 'default', 'autonumber', 'none'; optional):
        标题的样式：   - default       默认样式，标题前面有锚点   - autonumber
        标题前面有自增序号锚点   - none          标题没有锚点  默认为'default'.

        - inlineCode (dict; optional)

            `inlineCode` is a boolean | dict with keys:

    - theme (string; optional)

        - inlineMath (dict; optional)

            `inlineMath` is a boolean | dict with keys:

    - engine (a value equal to: 'katex', 'MathJax'; optional):
        'katex'或'MathJax'，默认为'MathJax'.

    - src (string; optional)

        - link (dict; optional)

            `link` is a boolean | dict with keys:

    - rel (a value equal to: '', 'nofollow'; optional):
        生成的<a>标签追加rel属性的默认值 空：在<a>标签里不会追加rel属性，
        nofollow：在<a>标签里追加rel=\"nofollow：在\"属性.

    - target (a value equal to: '', '_blank'; optional):
        生成的<a>标签追加target属性的默认值 空：在<a>标签里不会追加target属性，
        _blank：在<a>标签里追加target=\"_blank\"属性.

        - list (dict; optional)

            `list` is a boolean | dict with keys:

    - indentSpace (number; optional):
        默认2个空格缩进.

    - listNested (boolean; optional):
        同级列表类型转换后变为子级.

        - mathBlock (dict; optional)

            `mathBlock` is a boolean | dict with keys:

    - engine (a value equal to: 'katex', 'MathJax'; optional):
        'katex'或'MathJax'，默认为'MathJax'.

    - plugins (boolean; optional):
        是否加载插件，默认为True.

    - src (string; optional)

        - strikethrough (dict; optional)

            `strikethrough` is a boolean | dict with keys:

    - needWhitespace (boolean; optional):
        是否必须有前后空格  首尾、前后的定义： 语法前**语法首+内容+语法尾**语法后  例：     True:
        hello wor~~l~~d     ====>   hello wor~~l~~d             hello
        wor ~~l~~ d   ====>   hello wor <del>l</del> d     False:
        hello wor~~l~~d     ====>   hello wor<del>l</del>d
        hello wor ~~l~~ d     ====>   hello wor <del>l</del> d
        默认为False.

        - table (dict; optional)

            `table` is a boolean | dict with keys:

    - enableChart (boolean; optional)

        - toc (dict; optional)

            `toc` is a boolean | dict with keys:

    - allowMultiToc (boolean; optional):
        是否渲染多个目录，False表示只渲染一个目录，默认为False.

- fileTypeLimitMap (dict; default {    video: 'video/*',    audio: 'audio/*',    image: 'image/*',    word: '.doc,.docx',    pdf: '.pdf',    file: '*',}):
    上传文件的时候用来指定文件类型.

    `fileTypeLimitMap` is a dict with keys:

    - audio (string; optional)

    - file (string; optional)

    - image (string; optional)

    - pdf (string; optional)

    - video (string; optional)

    - word (string; optional)

- fineControl (dict; default {    isOpen: False,    videoFineControlOptions: {        isPoster: False,        isBorder: False,        isShadow: False,        isRadius: False    },    imageFineControlOptions: {        isBorder: False,        isShadow: False,        isRadius: False,        width: '100%',        height: 'auto'    }}):
    配置文件展示精细化控制，此功能只在配置了上传接口的情况下生效.

    `fineControl` is a dict with keys:

    - imageFineControlOptions (dict; optional):
        图片文件精细化控制选项.

        `imageFineControlOptions` is a dict with keys:

        - height (string; optional):
            图片的高度，默认'auto'.

        - isBorder (boolean; optional):
            是否显示边框，默认False.

        - isRadius (boolean; optional):
            是否显示圆角，默认False.

        - isShadow (boolean; optional):
            是否显示阴影，默认False.

        - name (string; optional):
            图片文件的名称.

        - width (string; optional):
            图片的宽度，默认'100%'，可配置百分比，也可配置像素值.

    - isOpen (boolean; optional):
        是否启用.

    - videoFineControlOptions (dict; optional):
        视频文件精细化控制选项.

        `videoFineControlOptions` is a dict with keys:

        - isBorder (boolean; optional):
            是否显示边框，默认False.

        - isPoster (boolean; optional):
            是否启用视频文件封面，默认为False.

        - isRadius (boolean; optional):
            是否显示圆角，默认False.

        - isShadow (boolean; optional):
            是否显示阴影，默认False.

        - name (string; optional):
            视频文件的名称.

        - posterUrl (string; optional):
            自定义视频文件封面地址，如果不设置，则默认为视频文件地址.

- forceAppend (boolean; default True):
    外层容器不存在时，是否强制输出到body上，默认为True.

- html (string; optional):
    编辑器html格式内容.

- isPreviewOnly (boolean; default False):
    预览页面是否需要绑定事件，默认为False.

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

- locale (a value equal to: 'zh_CN', 'en_US'; default 'zh_CN'):
    语言设置，默认为'zh_CN'.

- previewer (dict; default {    dom: False,    className: 'cherry-markdown',    enablePreviewerBubble: True,    lazyLoadImg: {        loadingImgPath: '',        maxNumPerTime: 2,        noLoadImgNum: 5,        autoLoadImgNum: 5,        maxTryTimesPerSrc: 2,        beforeLoadOneImgCallback: (img) => {            return True;        },        failLoadOneImgCallback: (img) => { },        afterLoadOneImgCallback: (img) => { },        afterLoadAllImgCallback: () => { },    },}):
    预览区域配置.

    `previewer` is a dict with keys:

    - className (string; optional)

    - dom (boolean; optional)

    - enablePreviewerBubble (boolean; optional):
        是否启用预览区域编辑能力（目前支持编辑图片尺寸、编辑表格内容），默认为True.

    - lazyLoadImg (dict; optional):
        配置图片懒加载的逻辑  - 如果不希望图片懒加载，可配置成 lazyLoadImg = {noLoadImgNum: -1}
        - 如果希望所有图片都无脑懒加载，可配置成 lazyLoadImg = {noLoadImgNum: 0,
        autoLoadImgNum: -1}  - 如果一共有15张图片，希望：     1、前5张图片（1~5）直接加载；
        2、后5张图片（6~10）不论在不在视区内，都无脑懒加载；     3、其他图片（11~15）在视区内时，进行懒加载；
        则配置应该为：lazyLoadImg = {noLoadImgNum: 5, autoLoadImgNum: 5}.

        `lazyLoadImg` is a dict with keys:

        - autoLoadImgNum (number; optional):
            首次自动加载几张图片（不论图片是否滚动到视野内），autoLoadImgNum = -1 表示会自动加载完所有图片.

        - loadingImgPath (string; optional):
            加载图片时如果需要展示loading图，则配置loading图的地址.

        - maxNumPerTime (number; optional):
            同一时间最多有几个图片请求，最大同时加载6张图片.

        - maxTryTimesPerSrc (number; optional):
            针对加载失败的图片 或 beforeLoadOneImgCallback 返回False
            的图片，最多尝试加载几次，为了防止死循环，最多5次。以图片的src为纬度统计重试次数.

        - noLoadImgNum (number; optional):
            不进行懒加载处理的图片数量，如果为0，即所有图片都进行懒加载处理， 如果设置为-1，则所有图片都不进行懒加载处理.

- style (dict; optional):
    自定义css字典.

- theme (list of dicts; default [    { className: 'default', label: '默认' },    { className: 'dark', label: '暗黑' },    { className: 'light', label: '明亮' },    { className: 'green', label: '清新' },    { className: 'red', label: '热情' },    { className: 'violet', label: '淡雅' },    { className: 'blue', label: '清幽' },]):
    配置主题，第三方可以自行扩展主题.

    `theme` is a list of dicts with keys:

    - className (a value equal to: 'default', 'dark', 'light', 'green', 'red', 'violet', 'blue'; optional)

    - label (a value equal to: '默认', '暗黑', '明亮', '清新', '热情', '淡雅', '清幽'; optional)

- toolbars (dict; default {    theme: 'dark',    showToolbar: True,    toolbar: [        'bold',        'italic',        'strikethrough',        '|',        'color',        'header',        'ruby',        '|',        'list',        'panel',        'detail',        {            insert: ['image', 'audio', 'video', 'link', 'hr', 'br', 'code', 'formula', 'toc', 'table', 'line-table', 'bar-table', 'pdf', 'word']        },        'settings',    ],    toolbarRight: [],    sidebar: [],    bubble: ['bold', 'italic', 'underline', 'strikethrough', 'sub', 'sup', 'quote', '|', 'size', 'color'],    float: ['h1', 'h2', 'h3', '|', 'checklist', 'quote', 'table', 'code'],    shortcutKey: {},    config: {        formula: {            showLatexLive: True,            templateConfig: False,        },    },}):
    工具栏配置.

    `toolbars` is a dict with keys:

    - bubble (boolean

      Or list of a value equal to: '|', 'bold', 'italic', 'underline', 'strikethrough', 'sub', 'sup', 'ruby', 'size', 'color', 'quote', 'detail', 'h1', 'h2', 'h3', 'header', 'ul', 'ol', 'checklist', 'list', 'justify', 'panel', 'image', 'audio', 'video', 'pdf', 'word', 'file', 'link', 'hr', 'br', 'code', 'formula', 'toc', 'table', 'drawIo', 'graph', 'undo', 'redo', 'theme', 'codeTheme', 'mobilePreview', 'togglePreview', 'switchModel', 'copy', 'export', 'fullScreen', 'settings's; optional)

    - config (dict; optional):
        一些按钮的配置信息.

        `config` is a dict with keys:

        - formula (dict; optional)

            `formula` is a dict with keys:

            - showLatexLive (boolean; optional):
                True: 显示 www.latexlive.com 外链； False：不显示，默认为True.

            - templateConfig (boolean; optional):
                False: 使用默认模板，默认为False.

    - float (boolean | list of a value equal to: '|', 'bold', 'italic', 'underline', 'strikethrough', 'sub', 'sup', 'ruby', 'size', 'color', 'quote', 'detail', 'h1', 'h2', 'h3', 'header', 'ul', 'ol', 'checklist', 'list', 'justify', 'panel', 'image', 'audio', 'video', 'pdf', 'word', 'file', 'link', 'hr', 'br', 'code', 'formula', 'toc', 'table', 'drawIo', 'graph', 'undo', 'redo', 'theme', 'codeTheme', 'mobilePreview', 'togglePreview', 'switchModel', 'copy', 'export', 'fullScreen', 'settings's; optional)

    - shortcutKey (dict; optional):
        快捷键配置，如果配置为空，则使用toolbar的配置。  例如：{'Alt-1': 'header', 'Alt-2':
        'header', 'Ctrl-b': 'bold', 'Ctrl-Alt-m': 'formula'}.

    - showToolbar (boolean; optional):
        是否展示顶部工具栏，默认为True； True：展示工具栏; toolbars.showToolbar=False 与
        toolbars.toolbar=False 等效.

    - sidebar (list; optional)

    - theme (a value equal to: 'light', 'dark'; optional):
        主题，可选的值为'light'和'dark'，默认为'light'.

    - toolbar (list of dicts; optional):
        具体要展示的工具栏菜单key.

        `toolbar` is a list of a value equal to: '|', 'bold',
        'italic', 'underline', 'strikethrough', 'sub', 'sup', 'ruby',
        'size', 'color', 'quote', 'detail', 'h1', 'h2', 'h3',
        'header', 'ul', 'ol', 'checklist', 'list', 'justify', 'panel',
        'image', 'audio', 'video', 'pdf', 'word', 'file', 'link',
        'hr', 'br', 'code', 'formula', 'toc', 'table', 'drawIo',
        'graph', 'undo', 'redo', 'theme', 'codeTheme',
        'mobilePreview', 'togglePreview', 'switchModel', 'copy',
        'export', 'fullScreen', 'settings' | dict with keys:

        - insert (list of a value equal to: 'bold', 'italic', 'underline', 'strikethrough', 'sub', 'sup', 'ruby', 'quote', 'detail', 'h1', 'h2', 'h3', 'ul', 'ol', 'checklist', 'image', 'audio', 'video', 'pdf', 'word', 'file', 'link', 'hr', 'br', 'code', 'formula', 'toc', 'table', 'drawIo', 'undo', 'redo', 'mobilePreview', 'togglePreview', 'switchModel', 'copy', 'fullScreen's; optional)s

    - toolbarRight (list; optional)

- uploadConfig (dict; default {    headers: {},    data: {},    withCredentials: False,    filename: 'file',    responseUrl: 'data.url',}):
    设置文件上传相关信息.

    `uploadConfig` is a dict with keys:

    - action (string; optional):
        设置上传的地址.

    - data (dict; optional):
        设置上传时附带的额外参数.

    - filename (string; optional):
        设置上传的文件字段名.

    - headers (dict; optional):
        设置上传的请求头部.

    - responseUrl (string; optional):
        设置上传接口响应中url的层级，如响应结果格式为{data: {url:
        'xxx'}}，则配置为'data.url'，默认为'data.url'.

    - withCredentials (boolean; optional):
        设置是否支持发送cookie凭证信息，默认为False.

- value (string; optional):
    编辑器内容."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyMarkdownEditor'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, value=Component.UNDEFINED, html=Component.UNDEFINED, engine=Component.UNDEFINED, editor=Component.UNDEFINED, toolbars=Component.UNDEFINED, drawioIframeUrl=Component.UNDEFINED, fileTypeLimitMap=Component.UNDEFINED, uploadConfig=Component.UNDEFINED, fineControl=Component.UNDEFINED, previewer=Component.UNDEFINED, theme=Component.UNDEFINED, isPreviewOnly=Component.UNDEFINED, autoScrollByCursor=Component.UNDEFINED, forceAppend=Component.UNDEFINED, locale=Component.UNDEFINED, autoScrollByHashAfterInit=Component.UNDEFINED, customSyntax=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'autoScrollByCursor', 'autoScrollByHashAfterInit', 'className', 'customSyntax', 'drawioIframeUrl', 'editor', 'engine', 'fileTypeLimitMap', 'fineControl', 'forceAppend', 'html', 'isPreviewOnly', 'key', 'loading_state', 'locale', 'previewer', 'style', 'theme', 'toolbars', 'uploadConfig', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'autoScrollByCursor', 'autoScrollByHashAfterInit', 'className', 'customSyntax', 'drawioIframeUrl', 'editor', 'engine', 'fileTypeLimitMap', 'fineControl', 'forceAppend', 'html', 'isPreviewOnly', 'key', 'loading_state', 'locale', 'previewer', 'style', 'theme', 'toolbars', 'uploadConfig', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyMarkdownEditor, self).__init__(**args)
