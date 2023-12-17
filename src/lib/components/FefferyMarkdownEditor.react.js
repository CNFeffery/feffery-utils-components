import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyMarkdownEditor = React.lazy(() => import(/* webpackChunkName: "feffery_markdown_editor" */ '../fragments/FefferyMarkdownEditor.react'));

const FefferyMarkdownEditor = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyMarkdownEditor {...props} />
        </Suspense>
    );
}

const toolbarOptions = [
    '|',
    'bold',
    'italic',
    'underline',
    'strikethrough',
    'sub',
    'sup',
    'ruby',
    'size',
    'color',
    'quote',
    'detail',
    'h1',
    'h2',
    'h3',
    'header',
    'ul',
    'ol',
    'checklist',
    'list',
    'justify',
    'panel',
    'image',
    'audio',
    'video',
    'pdf',
    'word',
    'file',
    'link',
    'hr',
    'br',
    'code',
    'formula',
    'toc',
    'table',
    'drawIo',
    'graph',
    'undo',
    'redo',
    'theme',
    'codeTheme',
    'mobilePreview',
    'togglePreview',
    'switchModel',
    'copy',
    'export',
    'fullScreen',
    'settings'
];
const insertOptions = [
    'bold',
    'italic',
    'underline',
    'strikethrough',
    'sub',
    'sup',
    'ruby',
    'quote',
    'detail',
    'h1',
    'h2',
    'h3',
    'ul',
    'ol',
    'checklist',
    'image',
    'audio',
    'video',
    'pdf',
    'word',
    'file',
    'link',
    'hr',
    'br',
    'code',
    'formula',
    'toc',
    'table',
    'drawIo',
    'undo',
    'redo',
    'mobilePreview',
    'togglePreview',
    'switchModel',
    'copy',
    'fullScreen'
];

// 定义参数或属性
FefferyMarkdownEditor.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * css类名
     */
    className: PropTypes.string,

    /**
     * 自定义css字典
     */
    style: PropTypes.object,

    /**
     * 辅助刷新用唯一标识key值
     */
    key: PropTypes.string,

    /**
     * 编辑器内容
     */
    value: PropTypes.string,

    /**
     * 编辑器html格式内容
     */
    html: PropTypes.string,

    /**
         * 解析引擎配置
         */
    engine: PropTypes.shape({
        /**
         * 全局配置
         */
        global: PropTypes.shape({
            /**
             * 是否启用经典换行逻辑,
             * true：一个换行会被忽略，两个以上连续换行会分割成段落，
             * false： 一个换行会转成<br>，两个连续换行会分割成段落，三个以上连续换行会转成<br>并分割段落,
             * 默认为false
             */
            classicBr: PropTypes.bool,
            /**
             * 额外允许渲染的html标签
             * 标签以英文竖线分隔，如：htmlWhiteList: 'iframe|script|style'
             * 默认为空，默认允许渲染的html见src/utils/sanitize.js whiteList 属性
             * 需要注意：
             *    - 启用iframe、script等标签后，会产生xss注入，请根据实际场景判断是否需要启用
             *    - 一般编辑权限可控的场景（如api文档系统）可以允许iframe、script等标签
             */
            htmlWhiteList: PropTypes.string
        }),
        /**
         * 内置语法配置
         */
        syntax: PropTypes.exact({
            link: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 生成的<a>标签追加target属性的默认值 空：在<a>标签里不会追加target属性， _blank：在<a>标签里追加target="_blank"属性
                     */
                    target: PropTypes.oneOf(['', '_blank']),
                    /**
                     * 生成的<a>标签追加rel属性的默认值 空：在<a>标签里不会追加rel属性， nofollow：在<a>标签里追加rel="nofollow：在"属性
                     */
                    rel: PropTypes.oneOf(['', 'nofollow'])
                })
            ]),
            autoLink: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 生成的<a>标签追加target属性的默认值 空：在<a>标签里不会追加target属性， _blank：在<a>标签里追加target="_blank"属性
                     */
                    target: PropTypes.oneOf(['', '_blank']),
                    /**
                     * 生成的<a>标签追加rel属性的默认值 空：在<a>标签里不会追加rel属性， nofollow：在<a>标签里追加rel="nofollow：在"属性
                     */
                    rel: PropTypes.oneOf(['', 'nofollow']),
                    /**
                     * 是否开启短链接
                     */
                    enableShortLink: PropTypes.bool,
                    /**
                     * 短链接长度
                     */
                    shortLinkLength: PropTypes.number
                })
            ]),
            list: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 同级列表类型转换后变为子级
                     */
                    listNested: PropTypes.bool,
                    /**
                     * 默认2个空格缩进
                     */
                    indentSpace: PropTypes.number
                })
            ]),
            table: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    enableChart: PropTypes.bool
                })
            ]),
            inlineCode: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 
                     */
                    theme: PropTypes.string
                })
            ]),
            codeBlock: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.shape({
                    /**
                     * 默认为深色主题'dark'
                     */
                    theme: PropTypes.string,
                    /**
                     * 超出长度是否换行，false则显示滚动条，默认为true
                     */
                    wrap: PropTypes.bool,
                    /**
                     * 是否显示行号，默认为true
                     */
                    lineNumber: PropTypes.bool,
                    /**
                     * 是否显示复制按钮，默认为true
                     */
                    copyCode: PropTypes.bool,
                    /**
                     * 是否显示编辑按钮，默认为true
                     */
                    editCode: PropTypes.bool,
                    /**
                     * 是否显示切换语言按钮，默认为true
                     */
                    changeLang: PropTypes.bool,
                    /**
                     * 是否启用缩进代码块，默认为true
                     */
                    indentedCodeBlock: PropTypes.bool,
                })
            ]),
            emoji: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 是否使用unicode进行渲染，默认为true
                     */
                    useUnicode: PropTypes.bool
                })
            ]),
            fontEmphasis: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 是否允许首尾空格
                     * 首尾、前后的定义： 语法前**语法首+内容+语法尾**语法后
                     * 例：
                     *    true:
                     *           __ hello __  ====>   <strong> hello </strong>
                     *           __hello__    ====>   <strong>hello</strong>
                     *    false:
                     *           __ hello __  ====>   <em>_ hello _</em>
                     *           __hello__    ====>   <strong>hello</strong>
                     *  默认为false
                     */
                    allowWhitespace: PropTypes.bool
                }),
            ]),
            strikethrough: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 是否必须有前后空格
                     * 首尾、前后的定义： 语法前**语法首+内容+语法尾**语法后
                     * 例：
                     *    true:
                     *            hello wor~~l~~d     ====>   hello wor~~l~~d
                     *            hello wor ~~l~~ d   ====>   hello wor <del>l</del> d
                     *    false:
                     *            hello wor~~l~~d     ====>   hello wor<del>l</del>d
                     *            hello wor ~~l~~ d     ====>   hello wor <del>l</del> d
                     * 默认为false
                     */
                    needWhitespace: PropTypes.bool
                }),
            ]),
            mathBlock: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 'katex'或'MathJax'，默认为'MathJax'
                     */
                    engine: PropTypes.oneOf(['katex', 'MathJax']),
                    src: PropTypes.string,
                    /**
                     * 是否加载插件，默认为true
                     */
                    plugins: PropTypes.bool
                })
            ]),
            inlineMath: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 'katex'或'MathJax'，默认为'MathJax'
                     */
                    engine: PropTypes.oneOf(['katex', 'MathJax']),
                    src: PropTypes.string
                })
            ]),
            toc: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 是否渲染多个目录，false表示只渲染一个目录，默认为false
                     */
                    allowMultiToc: PropTypes.bool
                })
            ]),
            header: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 标题的样式：
                     *  - default       默认样式，标题前面有锚点
                     *  - autonumber    标题前面有自增序号锚点
                     *  - none          标题没有锚点
                     * 默认为'default'
                     */
                    anchorStyle: PropTypes.oneOf(['default', 'autonumber', 'none']),
                })
            ]),
        })
    }),

    /**
     * 编辑器配置
     */
    editor: PropTypes.exact({
        /**
         * textarea 的id属性值
         */
        id: PropTypes.string,
        /**
         * textarea 的name属性值
         */
        name: PropTypes.string,
        /**
         * 是否自动将编辑区的内容回写到textarea里，默认为false
         */
        autoSave2Textarea: PropTypes.bool,
        /**
         * depend on codemirror theme name: https://codemirror.net/demo/theme.htm，默认为'default'
         */
        theme: PropTypes.string,
        /**
         * 编辑器的高度，默认100%，如果挂载点存在内联设置的height则以内联样式为主
         */
        height: PropTypes.string,
        /**
         * 编辑器初始化后的默认模式，一共有三种模式：1、双栏编辑预览模式；2、纯编辑模式；3、预览模式。
         * edit&preview: 双栏编辑预览模式,
         * editOnly: 纯编辑模式（没有预览，可通过toolbar切换成双栏或预览模式）,
         * previewOnly: 预览模式（没有编辑框，toolbar只显示“返回编辑”按钮，可通过toolbar切换成编辑模式），
         * 默认为'edit&preview'
         */
        defaultModel: PropTypes.oneOf(['edit&preview', 'editOnly', 'previewOnly']),
        /**
         * 粘贴时是否自动将html转成markdown，默认为true
         */
        convertWhenPaste: PropTypes.bool,
        codemirror: PropTypes.exact({
            /**
             * 是否自动focus 默认为true
             */
            autofocus: PropTypes.bool
        }),
        /**
         * 书写风格，normal 普通 | typewriter 打字机 | focus 专注，默认'normal'
         */
        writingStyle: PropTypes.oneOf(['normal', 'typewriter', 'focus']),
        /**
         * 在初始化后是否保持网页的滚动，true：保持滚动；false：网页自动滚动到编辑器初始化的位置，默认为false
         */
        keepDocumentScrollAfterInit: PropTypes.bool
    }),

    /**
     * 工具栏配置
     */
    toolbars: PropTypes.exact({
        /**
         * 主题，可选的值为'light'和'dark'，默认为'light'
         */
        theme: PropTypes.oneOf(['light', 'dark']),
        /**
         * 是否展示顶部工具栏，默认为true； true：展示工具栏; toolbars.showToolbar=false 与 toolbars.toolbar=false 等效
         */
        showToolbar: PropTypes.bool,
        /**
         * 具体要展示的工具栏菜单key
         */
        toolbar: PropTypes.arrayOf(PropTypes.oneOfType([
            PropTypes.oneOf(toolbarOptions),
            PropTypes.exact({
                insert: PropTypes.arrayOf(PropTypes.oneOf(insertOptions))
            })
        ])),
        toolbarRight: PropTypes.array,
        sidebar: PropTypes.array,
        bubble: PropTypes.oneOfType([
            PropTypes.bool,
            PropTypes.arrayOf(PropTypes.oneOf(toolbarOptions))
        ]),
        float: PropTypes.oneOfType([
            PropTypes.bool,
            PropTypes.arrayOf(PropTypes.oneOf(toolbarOptions))
        ]),
        /**
         * 快捷键配置，如果配置为空，则使用toolbar的配置。
         * 例如：{'Alt-1': 'header', 'Alt-2': 'header', 'Ctrl-b': 'bold', 'Ctrl-Alt-m': 'formula'}
         */
        shortcutKey: PropTypes.object,
        /**
         * 一些按钮的配置信息
         */
        config: PropTypes.exact({
            formula: PropTypes.exact({
                /**
                 * true: 显示 www.latexlive.com 外链； false：不显示，默认为true
                 */
                showLatexLive: PropTypes.bool,
                /**
                 * false: 使用默认模板，默认为false
                 */
                templateConfig: PropTypes.bool
            })
        })
    }),

    /**
     * 打开draw.io编辑页的url，如果为空则drawio按钮失效
     */
    drawioIframeUrl: PropTypes.string,

    /**
     * 上传文件的时候用来指定文件类型
     */
    fileTypeLimitMap: PropTypes.exact({
        video: PropTypes.string,
        audio: PropTypes.string,
        image: PropTypes.string,
        word: PropTypes.string,
        pdf: PropTypes.string,
        file: PropTypes.string
    }),

    /**
     * 设置文件上传相关信息
     */
    uploadConfig: PropTypes.exact({
        /**
         * 设置上传的地址
         */
        action: PropTypes.string,
        /**
         * 设置上传的请求头部
         */
        headers: PropTypes.object,
        /**
         * 设置上传时附带的额外参数
         */
        data: PropTypes.object,
        /**
         * 设置是否支持发送cookie凭证信息，默认为false
         */
        withCredentials: PropTypes.bool,
        /**
         * 设置上传的文件字段名
         */
        filename: PropTypes.string,
        /**
         * 设置上传接口响应中url的层级，如响应结果格式为{data: {url: 'xxx'}}，则配置为'data.url'，默认为'data.url'
         */
        responseUrl: PropTypes.string
    }),

    /**
     * 配置文件展示精细化控制，此功能只在配置了上传接口的情况下生效
     */
    fineControl: PropTypes.exact({
        /**
         * 是否启用
         */
        isOpen: PropTypes.bool,
        /**
         * 视频文件精细化控制选项
         */
        videoFineControlOptions: PropTypes.shape({
            /**
             * 视频文件的名称
             */
            name: PropTypes.string,
            /**
             * 是否启用视频文件封面，默认为false
             */
            isPoster: PropTypes.bool,
            /**
             * 自定义视频文件封面地址，如果不设置，则默认为视频文件地址
             */
            posterUrl: PropTypes.string,
            /**
             * 是否显示边框，默认false
             */
            isBorder: PropTypes.bool,
            /**
             * 是否显示阴影，默认false
             */
            isShadow: PropTypes.bool,
            /**
             * 是否显示圆角，默认false
             */
            isRadius: PropTypes.bool
        }),
        /**
         * 图片文件精细化控制选项
         */
        imageFineControlOptions: PropTypes.shape({
            /**
             * 图片文件的名称
             */
            name: PropTypes.string,
            /**
             * 是否显示边框，默认false
             */
            isBorder: PropTypes.bool,
            /**
             * 是否显示阴影，默认false
             */
            isShadow: PropTypes.bool,
            /**
             * 是否显示圆角，默认false
             */
            isRadius: PropTypes.bool,
            /**
             * 图片的宽度，默认'100%'，可配置百分比，也可配置像素值
             */
            width: PropTypes.string,
            /**
             * 图片的高度，默认'auto'
             */
            height: PropTypes.string
        }),
    }),

    /**
     * 预览区域配置
     */
    previewer: PropTypes.exact({
        dom: PropTypes.bool,
        className: PropTypes.string,
        /**
         * 是否启用预览区域编辑能力（目前支持编辑图片尺寸、编辑表格内容），默认为true
         */
        enablePreviewerBubble: PropTypes.bool,
        /**
         * 配置图片懒加载的逻辑
         * - 如果不希望图片懒加载，可配置成 lazyLoadImg = {noLoadImgNum: -1}
         * - 如果希望所有图片都无脑懒加载，可配置成 lazyLoadImg = {noLoadImgNum: 0, autoLoadImgNum: -1}
         * - 如果一共有15张图片，希望：
         *    1、前5张图片（1~5）直接加载；
         *    2、后5张图片（6~10）不论在不在视区内，都无脑懒加载；
         *    3、其他图片（11~15）在视区内时，进行懒加载；
         *    则配置应该为：lazyLoadImg = {noLoadImgNum: 5, autoLoadImgNum: 5}
         */
        lazyLoadImg: PropTypes.shape({
            /**
             * 加载图片时如果需要展示loading图，则配置loading图的地址
             */
            loadingImgPath: PropTypes.string,
            /**
             * 同一时间最多有几个图片请求，最大同时加载6张图片
             */
            maxNumPerTime: PropTypes.number,
            /**
             * 不进行懒加载处理的图片数量，如果为0，即所有图片都进行懒加载处理， 如果设置为-1，则所有图片都不进行懒加载处理
             */
            noLoadImgNum: PropTypes.number,
            /**
             * 首次自动加载几张图片（不论图片是否滚动到视野内），autoLoadImgNum = -1 表示会自动加载完所有图片
             */
            autoLoadImgNum: PropTypes.number,
            /**
             * 针对加载失败的图片 或 beforeLoadOneImgCallback 返回false 的图片，最多尝试加载几次，为了防止死循环，最多5次。以图片的src为纬度统计重试次数
             */
            maxTryTimesPerSrc: PropTypes.number
        }),
    }),

    /**
     * 配置主题，第三方可以自行扩展主题
     */
    theme: PropTypes.arrayOf(PropTypes.exact({
        className: PropTypes.oneOf(['default', 'dark', 'light', 'green', 'red', 'violet', 'blue']),
        label: PropTypes.oneOf(['默认', '暗黑', '明亮', '清新', '热情', '淡雅', '清幽'])
    })),

    /**
     * 预览页面是否需要绑定事件，默认为false
     */
    isPreviewOnly: PropTypes.bool,

    /**
     * 预览区域是否跟随编辑器光标自动滚动，默认为true
     */
    autoScrollByCursor: PropTypes.bool,

    /**
     * 外层容器不存在时，是否强制输出到body上，默认为true
     */
    forceAppend: PropTypes.bool,

    /**
     * 语言设置，默认为'zh_CN'
     */
    locale: PropTypes.oneOf(['zh_CN', 'en_US']),

    /**
     * 编辑器初始化后是否检查 location.hash 尝试滚动到对应位置，默认为false
     */
    autoScrollByHashAfterInit: PropTypes.bool,

    /**
     * 自定义语法
     */
    customSyntax: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 自定义语法名称
             */
            syntaxName: PropTypes.string,
            /**
             * 是否用自定义的语法覆盖默认语法，默认为false
             */
            force: PropTypes.bool,
            /**
             * 定义该自定义语法在什么语法之前执行
             */
            before: PropTypes.string,
            /**
             * 自定义语法类型，'inline'表示行内语法，'block'表示段落语法
             */
            syntaxType: PropTypes.oneOf(['inline', 'block']),
            /**
             * 自定义语法的正则表达式
             */
            reg: PropTypes.string,
            /**
             * 自定义语法的渲染结果
             */
            result: PropTypes.string
        })
    ),

    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

// 设置默认参数
FefferyMarkdownEditor.defaultProps = {
    engine: {
        global: {
            classicBr: false,
            htmlWhiteList: '',
        },
        syntax: {
            link: {
                target: '',
                rel: '',
            },
            autoLink: {
                target: '',
                rel: '',
                enableShortLink: true,
                shortLinkLength: 20,
            },
            list: {
                listNested: false,
                indentSpace: 2,
            },
            inlineCode: {
                theme: 'red',
            },
            codeBlock: {
                theme: 'dark',
                wrap: true,
                lineNumber: true,
                copyCode: true,
                editCode: true,
                changeLang: true,
                indentedCodeBlock: true,
            },
            emoji: {
                useUnicode: true,
            },
            fontEmphasis: {
                allowWhitespace: false,
            },
            strikethrough: {
                needWhitespace: false,
            },
            mathBlock: {
                engine: 'MathJax',
                src: '',
                plugins: true,
            },
            inlineMath: {
                engine: 'MathJax',
                src: '',
            },
            toc: {
                allowMultiToc: false,
            },
            header: {
                anchorStyle: 'default',
            },
        },
    },
    editor: {
        id: 'code',
        name: 'code',
        autoSave2Textarea: false,
        theme: 'default',
        height: '100%',
        defaultModel: 'edit&preview',
        convertWhenPaste: true,
        codemirror: {
            autofocus: true,
        },
        writingStyle: 'normal',
        keepDocumentScrollAfterInit: false,
    },
    toolbars: {
        theme: 'dark',
        showToolbar: true,
        toolbar: [
            'bold',
            'italic',
            'strikethrough',
            '|',
            'color',
            'header',
            'ruby',
            '|',
            'list',
            'panel',
            'detail',
            {
                insert: ['image', 'audio', 'video', 'link', 'hr', 'br', 'code', 'formula', 'toc', 'table', 'line-table', 'bar-table', 'pdf', 'word']
            },
            'graph',
            'settings',
        ],
        toolbarRight: [],
        sidebar: [],
        bubble: ['bold', 'italic', 'underline', 'strikethrough', 'sub', 'sup', 'quote', '|', 'size', 'color'],
        float: ['h1', 'h2', 'h3', '|', 'checklist', 'quote', 'table', 'code'],
        shortcutKey: {},
        config: {
            formula: {
                showLatexLive: true,
                templateConfig: false,
            },
        },
    },
    drawioIframeUrl: '',
    fileTypeLimitMap: {
        video: 'video/*',
        audio: 'audio/*',
        image: 'image/*',
        word: '.doc,.docx',
        pdf: '.pdf',
        file: '*',
    },
    uploadConfig: {
        headers: {},
        data: {},
        withCredentials: false,
        filename: 'file',
        responseUrl: 'data.url',
    },
    fineControl: {
        isOpen: false,
        videoFineControlOptions: {
            isPoster: false,
            isBorder: false,
            isShadow: false,
            isRadius: false
        },
        imageFineControlOptions: {
            isBorder: false,
            isShadow: false,
            isRadius: false,
            width: '100%',
            height: 'auto'
        }
    },
    previewer: {
        dom: false,
        className: 'cherry-markdown',
        enablePreviewerBubble: true,
        lazyLoadImg: {
            loadingImgPath: '',
            maxNumPerTime: 2,
            noLoadImgNum: 5,
            autoLoadImgNum: 5,
            maxTryTimesPerSrc: 2,
            beforeLoadOneImgCallback: (img) => {
                return true;
            },
            failLoadOneImgCallback: (img) => { },
            afterLoadOneImgCallback: (img) => { },
            afterLoadAllImgCallback: () => { },
        },
    },
    theme: [
        { className: 'default', label: '默认' },
        { className: 'dark', label: '暗黑' },
        { className: 'light', label: '明亮' },
        { className: 'green', label: '清新' },
        { className: 'red', label: '热情' },
        { className: 'violet', label: '淡雅' },
        { className: 'blue', label: '清幽' },
    ],
    isPreviewOnly: false,
    autoScrollByCursor: true,
    forceAppend: true,
    locale: 'zh_CN',
    autoScrollByHashAfterInit: false
}

export default FefferyMarkdownEditor;

export const propTypes = FefferyMarkdownEditor.propTypes;
export const defaultProps = FefferyMarkdownEditor.defaultProps;