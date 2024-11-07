import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyVditor = React.lazy(() => import(/* webpackChunkName: "feffery_vditor" */ '../../fragments/editor/FefferyVditor.react'));

/**
 * 类Typora的markdown编辑器组件FefferyVditor
 */
const FefferyVditor = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyVditor {...props} />
        </Suspense>
    );
}

// 定义递归PropTypes
const PropTreeNodeShape = {
    /**
     * 唯一标示
     */
    name: PropTypes.string,

    /**
     * svg图标
     */
    icon: PropTypes.string,

    /**
     * 提示
     */
    tip: PropTypes.string,

    /**
     * 提示位置，可选的有`'n'`、`'ne'`、`'nw'`、`'s'`、`'se'`、`'sw'`、`'w'`、`'e'`
     */
    tipPosition: PropTypes.oneOf(['n', 'ne', 'nw', 's', 'se', 'sw', 'w', 'e']),

    /**
     * 快捷键，格式为`⇧⌘/⌘/⌥⌘`
     */
    hotkey: PropTypes.string,

    /**
     * 插入编辑器中的后缀
     */
    suffix: PropTypes.string,

    /**
     * 插入编辑器中的前缀
     */
    prefix: PropTypes.string,

    /**
     * 样式名
     */
    className: PropTypes.string
}

const PropTreeNode = PropTypes.shape(PropTreeNodeShape);
PropTreeNodeShape.toolbar = PropTypes.arrayOf(PropTypes.oneOfType([
    PropTypes.oneOf([
        'emoji', 'headings', 'bold', 'italic', 'strike', '|', 'line', 'quote', 'list', 'ordered-list', 'check', 'outdent',
        'indent', 'code', 'inline-code', 'insert-after', 'insert-before', 'undo', 'redo', 'upload', 'link', 'table', 'record',
        'edit-mode', 'both', 'preview', 'fullscreen', 'outline', 'code-theme', 'content-theme', 'export', 'devtools', 'info',
        'help', 'br'
    ]),
    PropTreeNode
]));
const toolbarPropTypes = PropTypes.arrayOf(PropTypes.oneOfType([
    PropTypes.oneOf([
        'emoji', 'headings', 'bold', 'italic', 'strike', '|', 'line', 'quote', 'list', 'ordered-list', 'check', 'outdent',
        'indent', 'code', 'inline-code', 'insert-after', 'insert-before', 'undo', 'redo', 'upload', 'link', 'table', 'record',
        'edit-mode', 'both', 'preview', 'fullscreen', 'outline', 'code-theme', 'content-theme', 'export', 'devtools', 'info',
        'help', 'br'
    ]),
    PropTreeNode
]));

FefferyVditor.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名，支持[动态css](/advanced-classname)
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 用于配置`value`变化更新的防抖等待时长（单位：毫秒）
     * 默认值：`200`
     */
    debounceWait: PropTypes.number,

    /**
     * 设置历史记录间隔
     */
    undoDelay: PropTypes.number,

    /**
     * 设置编辑器总高度
     * 默认值：`'auto'`
     */
    height: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.number
    ]),

    /**
     * 设置编辑区域最小高度
     */
    minHeight: PropTypes.number,

    /**
     * 设置编辑器总宽度，支持`%`
     * 默认值：`'auto'`
     */
    width: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.number
    ]),

    /**
     * 设置输入区域为空时的提示
     */
    placeholder: PropTypes.string,

    /**
     * 设置语言，可选的有`'en_US'`、`'fr_FR'`、`'pt_BR'`、`'ja_JP'`、`'ko_KR'`、`'ru_RU'`、`'sv_SE'`、`'zh_CN'`、`'zh_TW'`
     * 默认值：`'zh_CN'`
     */
    lang: PropTypes.oneOf(['en_US', 'fr_FR', 'pt_BR', 'ja_JP', 'ko_KR', 'ru_RU', 'sv_SE', 'zh_CN', 'zh_TW']),

    /**
     * 设置`tab`键操作字符串，支持`\t`及任意字符串
     */
    tab: PropTypes.string,

    /**
     * 是否启用打字机模式
     * 默认值：`false`
     */
    typewriterMode: PropTypes.bool,

    /**
     * 配置`CDN`地址，可选的有`https://unpkg.com/vditor@${VDITOR_VERSION}`、`https://registry.npmmirror.com/vditor/${VDITOR_VERSION}/files`，VDITOR_VERSION是vditor版本号，可通过不设置此参数从浏览器请求信息中获取版本号信息，默认使用的是`https://unpkg.com/vditor@${VDITOR_VERSION}`，也可使用自行搭建的`CDN`地址
     */
    cdn: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.oneOf([
            `https://unpkg.com/vditor@${VDITOR_VERSION}`,
            `https://registry.npmmirror.com/vditor/${VDITOR_VERSION}/files`
        ])
    ]),

    /**
     * 设置模式，可选的有：`'sv'`(分屏预览)、`'ir'`(即时渲染)、`'wysiwyg'`(所见即所得)
     * 默认值：`'ir'`(所见即所得)
     */
    mode: PropTypes.oneOf(['wysiwyg', 'ir', 'sv']),


    /**
     * 是否显示日志
     * 默认值：`false`
     */
    debuggerMode: PropTypes.bool,

    /**
     * 编辑器`md`内容
     */
    value: PropTypes.string,

    /**
     * 设置编辑器主题，可选的有：`'classic'`、`'dark'`
     * 默认值：`'classic'`
     */
    theme: PropTypes.oneOf(['classic', 'dark']),

    /**
     * 设置图标风格，可选的有：`'ant'`、`'material'`
     * 默认值：`'ant'`
     */
    icon: PropTypes.oneOf(['ant', 'material']),

    /**
     * 设置工具栏
     */
    toolbar: toolbarPropTypes,

    /**
     * 工具栏配置
     */
    toolbarConfig: PropTypes.exact({
        /**
         * 是否隐藏工具栏
         * 默认值：`false`
        */
        hide: PropTypes.bool,

        /**
         * 是否固定工具栏
         * 默认值：`false`
         */
        pin: PropTypes.bool,
    }),

    /**
     * 计数器配置
     */
    counter: PropTypes.shape({
        /**
         * 是否启用计数器
         * 默认值：`false`
         */
        enable: PropTypes.bool,

        /**
         * 设置允许输入的最大值
         */
        max: PropTypes.number,

        /**
         * 设置统计类型，可选的有：`'markdown'`、`'text'`
         * 默认值：`'markdown'`
         */
        type: PropTypes.oneOf(['markdown', 'text'])
    }),

    /**
     * 缓存配置
     */
    cache: PropTypes.shape({
        /**
         * 是否使用`localStorage`进行缓存
         * 默认值：`true`
         */
        enable: PropTypes.bool,

        /**
         * 缓存`key`
         */
        id: PropTypes.string
    }),

    /**
     * 预览配置
     */
    preview: PropTypes.shape({
        /**
         * 配置预览`debounce`毫秒间隔
         */
        delay: PropTypes.number,

        /**
         * 配置预览区域最大宽度
         */
        maxWidth: PropTypes.number,

        /**
         * 配置显示模式，可选的有：`'both'`、`'editor'`
         * 默认值：`'both'`
         */
        mode: PropTypes.oneOf(['both', 'editor']),

        /**
         * 配置md解析请求
         */
        url: PropTypes.string,

        /**
         * 语言、样式等配置
         */
        hljs: PropTypes.shape({
            /**
             * 未指定语言时默认使用该语言
             */
            defaultLang: PropTypes.string,

            /**
             * 是否启用代码高亮
             * 默认值：`true`
             */
            enable: PropTypes.bool,

            /**
             * 配置菜单字号选项
             * 默认值：`'github'`
             */
            style: PropTypes.oneOf([
                'abap', 'algol', 'algol_nu', 'api', 'arduino', 'autumn', 'average', 'base16-snazzy', 'borland', 'bw',
                'catppuccin-frappe', 'catppuccin-latte', 'catppuccin-macchiato', 'catppuccin-mocha', 'colorful', 'compat',
                'doom-one', 'doom-one2', 'dracula', 'emacs', 'friendly', 'fruity', 'github-dark', 'github', 'gruvbox-light',
                'gruvbox', 'hr_high_contrast', 'hrdark', 'igor', 'lovelace', 'manni', 'modus-operandi', 'modus-vivendi',
                'monokai', 'monokailight', 'murphy', 'native', 'nord', 'onedark', 'onesenterprise', 'paraiso-dark',
                'paraiso-light', 'pastie', 'perldoc', 'pygments', 'rainbow_dash', 'rose-pine-dawn', 'rose-pine-moon',
                'rose-pine', 'rrt', 'solarized-dark', 'solarized-dark256', 'solarized-light', 'swapoff', 'tango',
                'tokyonight-day', 'tokyonight-moon', 'tokyonight-night', 'tokyonight-storm', 'trac', 'vim', 'vs', 'vulcan',
                'witchhazel', 'xcode-dark', 'xcode'
            ]),

            /**
             * 是否启用行号
             * 默认值：`false`
             */
            lineNumber: PropTypes.bool,

            /**
             * 自定义指定语言
             */
            langs: PropTypes.arrayOf(PropTypes.string)
        }),

        /**
         * `markdown`配置
         */
        markdown: PropTypes.shape({
            /**
             * 是否开启自动空格
             * 默认值：`false`
             */
            autoSpace: PropTypes.bool,

            /**
             * 是否开启自动链接
             * 默认值：`true`
             */
            gfmAutoLink: PropTypes.bool,

            /**
             * 是否开启自动矫正术语
             * 默认值：`false`
             */
            fixTermTypo: PropTypes.bool,

            /**
             * 是否开启插入目录
             * 默认值：`false`
             */
            toc: PropTypes.bool,

            /**
             * 是否开启脚注，默认为true
             */
            footnotes: PropTypes.bool,

            /**
             * `'wysiwyg'`和`'ir'`模式下是否对代码块进行渲染
             * 默认值：`true`
             */
            codeBlockPreview: PropTypes.bool,

            /**
             * `'wysiwyg'`和`'ir'`模式下是否对数学公式进行渲染
             * 默认值：`true`
             */
            mathBlockPreview: PropTypes.bool,

            /**
             * 段落开头是否空两格
             * 默认值：`false`
             */
            paragraphBeginningSpace: PropTypes.bool,

            /**
             * 是否启用过滤`XSS`
             * 默认值：`true`
             */
            sanitize: PropTypes.bool,

            /**
             * 是否为列表添加`data-style`属性
             * 默认值：`false`
             */
            listStyle: PropTypes.bool,

            /**
             * 链接相对路径前缀
             */
            linkBase: PropTypes.string,

            /**
             * 链接强制前缀
             */
            linkPrefix: PropTypes.string,

            /**
             * 是否启用`mark`标记
             * 默认值：`false`
             */
            mark: PropTypes.bool
        }),

        /**
         * 主题配置
         */
        theme: PropTypes.shape({
            /**
             * 当前主题
             * 默认值：`'light'`
             */
            current: PropTypes.string,

            /**
             * 可选主题列表
             * 默认值：`{"ant-design": "Ant Design", dark: "Dark", light: "Light", wechat: "WeChat"}`
             */
            list: PropTypes.object,

            /**
             * 主题样式地址
             * 默认值：`https://unpkg.com/vditor@${VDITOR_VERSION}/dist/css/content-theme`
             */
            path: PropTypes.string
        }),

        /**
         * 数学公式配置
         */
        math: PropTypes.shape({
            /**
             * 内联数学公式起始`$`后是否允许数字
             * 默认值：`false`
             */
            inlineDigit: PropTypes.bool,

            /**
             * 使用`MathJax`渲染时传入的宏定义
             */
            macros: PropTypes.object,

            /**
             * 配置数学公式渲染引擎，可选的值有`'KaTeX'`、`'MathJax'`
             * 默认值：`'KaTeX'`
             */
            engine: PropTypes.oneOf(['KaTeX', 'MathJax']),

            /**
             * 数学公式渲染引擎为`MathJax`时的参数
             */
            mathJaxOptions: PropTypes.any
        }),

        /**
         * 平台类型配置
         */
        actions: PropTypes.arrayOf(PropTypes.oneOfType([
            PropTypes.oneOf([
                'desktop', 'tablet', 'mobile', 'mp-wechat', 'zhihu'
            ]),
            PropTypes.shape({
                /** 
                 * 键名 
                 */
                key: PropTypes.string,
                /** 
                 * 按钮文本 
                 */
                text: PropTypes.string,
                /** 
                 * 按钮`className`值 
                 */
                className: PropTypes.string,
                /** 
                 * 按钮提示信息 
                 */
                tooltip: PropTypes.string
            })
        ])),

        /**
         * 多媒体渲染配置
         */
        render: PropTypes.shape({
            media: PropTypes.shape({
                /**
                 * 是否启用多媒体渲染
                 * 默认值：`true`
                 */
                enable: PropTypes.bool
            })
        })
    }),

    /**
     * 图片配置
     */
    image: PropTypes.shape({
        /**
         * 是否预览图片
         * 默认值：`true`
         */
        isPreview: PropTypes.bool
    }),

    /**
     * 链接配置
     */
    link: PropTypes.shape({
        /**
         * 是否打开链接地址
         * 默认值：`true`
         */
        isOpen: PropTypes.bool
    }),

    /**
     * hint配置
     */
    hint: PropTypes.shape({
        /**
         * 是否进行`md`解析
         * 默认值：`true`
         */
        parse: PropTypes.bool,

        /**
         * 提示`debounce`毫秒间隔
         * 默认值：`200`
         */
        delay: PropTypes.number,

        /**
         * 默认表情，可从`https://github.com/88250/lute/blob/master/parse/emoji_map.go`中选取，也可自定义
         * 默认值：`{'+1': '👍', '-1': '👎', 'heart': '❤️', 'cold_sweat': '😰'}`
         */
        emoji: PropTypes.object,

        /**
         * 常用表情提示
         */
        emojiTail: PropTypes.string,

        /**
         * 表情图片地址
         * 默认值：`https://unpkg.com/vditor@${VDITOR_VERSION}/dist/images/emoji`
         */
        emojiPath: PropTypes.string
    }),

    /**
     * 上传配置
     */
    upload: PropTypes.shape({
        /**
         * 上传`url`，为空则不会触发上传相关事件
         */
        url: PropTypes.string,

        /**
         * 上传文件最大`Byte`
         * 默认值：`10 * 1024 * 1024`
         */
        max: PropTypes.number,

        /**
         * 剪切板中包含图片地址时，使用此`url`重新上传
         */
        linkToImgUrl: PropTypes.string,

        /**
         * `CORS`上传验证，头为`X-Upload-Token`
         */
        token: PropTypes.any,

        /**
         * 跨站点访问控制
         * 默认值：`false`
         */
        withCredentials: PropTypes.bool,

        /**
         * 请求头设置
         */
        headers: PropTypes.object,

        /**
         * 文件上传类型，同`https://www.w3schools.com/tags/att_input_accept.asp`
         */
        accept: PropTypes.string,

        /**
         * 额外请求参数
         */
        extraData: PropTypes.object,

        /**
         * 是否允许多文件上传
         * 默认值：`true`
         */
        multiple: PropTypes.bool,

        /**
         * 上传字段名称
         * 默认值：`file[]`
         */
        fieldName: PropTypes.string
    }),

    /**
     * 拖拽配置
     */
    resize: PropTypes.shape({
        /**
         * 是否支持大小拖拽
         * 默认值：`false`
         */
        enable: PropTypes.bool,

        /**
         * 设置拖拽栏位置，可选的值有`'top'`、`'bottom'`
         * 默认值：`'bottom'`
         */
        position: PropTypes.oneOf(['top', 'bottom']),
    }),

    /**
     * 类名配置
     */
    classes: PropTypes.shape({
        /**
         * 预览元素上的`className`
         */
        preview: PropTypes.string
    }),

    /**
     * 全屏配置
     */
    fullscreen: PropTypes.shape({
        /**
         * 全屏层级
         * 默认值：`90`
         */
        index: PropTypes.number
    }),

    /**
     * 大纲配置
     */
    outline: PropTypes.shape({
        /**
         * 初始化是否展现大纲
         * 默认值：`false`
         */
        enable: PropTypes.bool,

        /**
         * 大纲位置，可选的值有`'left'`、`'right'`
         * 默认值：`'left'`
         */
        position: PropTypes.oneOf(['left', 'right'])
    }),

    /**
     * 编辑器`HTML`内容
     */
    htmlValue: PropTypes.string,

    /**
     * 选中内容的字符串
     */
    selectedValue: PropTypes.string,

    /**
     * 字数统计
     */
    wordCount: PropTypes.number,

    /**
     * 开启大小拖拽后监听拖拽后的高度
     */
    resizeHeight: PropTypes.number,

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
    setProps: PropTypes.func,
};

// 设置默认参数
FefferyVditor.defaultProps = {
    debounceWait: 200,
    lang: 'zh_CN',
    typewriterMode: false,
    mode: 'ir',
    debuggerMode: false,
    theme: 'classic',
    icon: 'ant',
    toolbar: [
        "emoji",
        "headings",
        "bold",
        "italic",
        "strike",
        "link",
        "|",
        "list",
        "ordered-list",
        "check",
        "outdent",
        "indent",
        "|",
        "quote",
        "line",
        "code",
        "inline-code",
        "insert-before",
        "insert-after",
        "|",
        "upload",
        "record",
        "table",
        "|",
        "undo",
        "redo",
        "|",
        "fullscreen",
        "edit-mode",
        {
            name: "more",
            toolbar: [
                "both",
                "code-theme",
                "content-theme",
                "export",
                "outline",
                "preview"
            ],
        },
    ],
    toolbarConfig: {
        hide: false,
        pin: false
    }
}

export default FefferyVditor;

export const propTypes = FefferyVditor.propTypes;
export const defaultProps = FefferyVditor.defaultProps;