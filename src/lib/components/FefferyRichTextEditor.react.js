import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyRichTextEditor = React.lazy(() => import(/* webpackChunkName: "feffery_rich_text_editor" */ '../fragments/FefferyRichTextEditor.react'));

const FefferyRichTextEditor = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyRichTextEditor {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyRichTextEditor.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 组件类名
     */
    className: PropTypes.string,

    /**
     * 设置组件的样式
     */
    style: PropTypes.object,

    /**
     * 辅助刷新用唯一标识key值
     */
    key: PropTypes.string,

    /**
     * 工具栏类名
     */
    toolbarClassName: PropTypes.string,

    /**
     * 设置工具栏的样式
     */
    toolbarStyle: PropTypes.object,

    /**
     * 编辑器类名
     */
    editorClassName: PropTypes.string,

    /**
     * 设置编辑器的样式
     */
    editorStyle: PropTypes.object,

    /**
     * 组件语言，默认可支持中文和英文，默认为中文
     */
    locale: PropTypes.oneOf(['zh-CN', 'en']),

    /**
     * 编辑器html格式内容
     */
    htmlValue: PropTypes.string,

    /**
     * 编辑器纯文本内容
     */
    textValue: PropTypes.string,

    /**
     * 工具栏配置
     */
    toolbarConfig: PropTypes.shape({
        /**
         * 配置工具栏显示的菜单key，默认工具栏从左至右菜单对应的key为
         * [
                "headerSelect",
                "blockquote",
                "|",
                "bold",
                "underline",
                "italic",
                {
                    "key": "group-more-style",
                    "title": "更多",
                    "iconSvg": "<svg viewBox=\"0 0 1024 1024\"><path d=\"M204.8 505.6m-76.8 0a76.8 76.8 0 1 0 153.6 0 76.8 76.8 0 1 0-153.6 0Z\"></path><path d=\"M505.6 505.6m-76.8 0a76.8 76.8 0 1 0 153.6 0 76.8 76.8 0 1 0-153.6 0Z\"></path><path d=\"M806.4 505.6m-76.8 0a76.8 76.8 0 1 0 153.6 0 76.8 76.8 0 1 0-153.6 0Z\"></path></svg>",
                    "menuKeys": [
                        "through",
                        "code",
                        "sup",
                        "sub",
                        "clearStyle"
                    ]
                },
                "color",
                "bgColor",
                "|",
                "fontSize",
                "fontFamily",
                "lineHeight",
                "|",
                "bulletedList",
                "numberedList",
                "todo",
                {
                    "key": "group-justify",
                    "title": "对齐",
                    "iconSvg": "<svg viewBox=\"0 0 1024 1024\"><path d=\"M768 793.6v102.4H51.2v-102.4h716.8z m204.8-230.4v102.4H51.2v-102.4h921.6z m-204.8-230.4v102.4H51.2v-102.4h716.8zM972.8 102.4v102.4H51.2V102.4h921.6z\"></path></svg>",
                    "menuKeys": [
                        "justifyLeft",
                        "justifyRight",
                        "justifyCenter",
                        "justifyJustify"
                    ]
                },
                {
                    "key": "group-indent",
                    "title": "缩进",
                    "iconSvg": "<svg viewBox=\"0 0 1024 1024\"><path d=\"M0 64h1024v128H0z m384 192h640v128H384z m0 192h640v128H384z m0 192h640v128H384zM0 832h1024v128H0z m0-128V320l256 192z\"></path></svg>",
                    "menuKeys": [
                        "indent",
                        "delIndent"
                    ]
                },
                "|",
                "emotion",
                "insertLink",
                {
                    "key": "group-image",
                    "title": "图片",
                    "iconSvg": "<svg viewBox=\"0 0 1024 1024\"><path d=\"M959.877 128l0.123 0.123v767.775l-0.123 0.122H64.102l-0.122-0.122V128.123l0.122-0.123h895.775zM960 64H64C28.795 64 0 92.795 0 128v768c0 35.205 28.795 64 64 64h896c35.205 0 64-28.795 64-64V128c0-35.205-28.795-64-64-64zM832 288.01c0 53.023-42.988 96.01-96.01 96.01s-96.01-42.987-96.01-96.01S682.967 192 735.99 192 832 234.988 832 288.01zM896 832H128V704l224.01-384 256 320h64l224.01-192z\"></path></svg>",
                    "menuKeys": [
                        "insertImage",
                        "uploadImage"
                    ]
                },
                {
                    "key": "group-video",
                    "title": "视频",
                    "iconSvg": "<svg viewBox=\"0 0 1024 1024\"><path d=\"M981.184 160.096C837.568 139.456 678.848 128 512 128S186.432 139.456 42.816 160.096C15.296 267.808 0 386.848 0 512s15.264 244.16 42.816 351.904C186.464 884.544 345.152 896 512 896s325.568-11.456 469.184-32.096C1008.704 756.192 1024 637.152 1024 512s-15.264-244.16-42.816-351.904zM384 704V320l320 192-320 192z\"></path></svg>",
                    "menuKeys": [
                        "insertVideo",
                        "uploadVideo"
                    ]
                },
                "insertTable",
                "codeBlock",
                "divider",
                "|",
                "undo",
                "redo",
                "|",
                "fullScreen"
            ]
        */
        toolbarKeys: PropTypes.array,

        /**
         * 是否将菜单弹出的modal添加到body下，默认为false
         */
        modalAppendToBody: PropTypes.bool,
    }),

    /**
     * 编辑器配置
     */
    editorConfig: PropTypes.shape({
        /**
     * 配置编辑器placeholder
     */
        placeholder: PropTypes.string,

        /**
         * 配置编辑器是否只读，默认为false
         */
        readOnly: PropTypes.bool,

        /**
         * 配置编辑器默认是否focus ，默认为true
         */
        autoFocus: PropTypes.bool,

        /**
         * 配置编辑器是否支持滚动，默认为true。
         * 注意，此时不要固定editor-container的高度，设置一个min-height即可，
         * TIP：可将 scroll 设置为 false 的情况：编辑器高度自增、在线文档，如腾讯文档、语雀那样的
         */
        scroll: PropTypes.bool,

        /**
         * 配置编辑器的maxlength，TIP：无特殊需求，请慎用maxLength，这可能会导致编辑器内容过多时，编辑卡顿
         */
        maxLength: PropTypes.number,

        /**
         * 配置菜单
         */
        MENU_CONF: PropTypes.shape({
            /**
         * 配置菜单文字颜色选项
         */
            color: PropTypes.array,

            /**
             * 配置菜单背景颜色选项
             */
            bgColor: PropTypes.array,

            /**
             * 配置菜单字号选项
             */
            fontSize: PropTypes.exact({
                fontSizeList: PropTypes.arrayOf(PropTypes.oneOfType([
                    PropTypes.string,
                    PropTypes.exact({
                        name: PropTypes.string,
                        value: PropTypes.string
                    })
                ]))
            }),

            /**
             * 配置菜单字体选项
             */
            fontFamily: PropTypes.exact({
                fontFamilyList: PropTypes.arrayOf(PropTypes.oneOfType([
                    PropTypes.string,
                    PropTypes.exact({
                        name: PropTypes.string,
                        value: PropTypes.string
                    })
                ]))
            }),

            /**
             * 配置菜单行高选项
             */
            lineHeight: PropTypes.exact({
                lineHeightList: PropTypes.arrayOf(PropTypes.string)
            }),

            /**
             * 配置菜单表情选项
             */
            emotions: PropTypes.exact({
                emotions: PropTypes.arrayOf(PropTypes.string)
            }),

            /**
             * 配置代码高亮
             */
            codeSelectLang: PropTypes.exact({
                /**
                 * 配置代码语言，可用的有：
                 * [
                        {
                            "text": "CSS",
                            "value": "css"
                        },
                        {
                            "text": "HTML",
                            "value": "html"
                        },
                        {
                            "text": "XML",
                            "value": "xml"
                        },
                        {
                            "text": "Javascript",
                            "value": "javascript"
                        },
                        {
                            "text": "Typescript",
                            "value": "typescript"
                        },
                        {
                            "text": "JSX",
                            "value": "jsx"
                        },
                        {
                            "text": "Go",
                            "value": "go"
                        },
                        {
                            "text": "PHP",
                            "value": "php"
                        },
                        {
                            "text": "C",
                            "value": "c"
                        },
                        {
                            "text": "Python",
                            "value": "python"
                        },
                        {
                            "text": "Java",
                            "value": "java"
                        },
                        {
                            "text": "C++",
                            "value": "cpp"
                        },
                        {
                            "text": "C#",
                            "value": "csharp"
                        },
                        {
                            "text": "Visual Basic",
                            "value": "visual-basic"
                        },
                        {
                            "text": "SQL",
                            "value": "sql"
                        },
                        {
                            "text": "Ruby",
                            "value": "ruby"
                        },
                        {
                            "text": "Swift",
                            "value": "swift"
                        },
                        {
                            "text": "Bash",
                            "value": "bash"
                        },
                        {
                            "text": "Lua",
                            "value": "lua"
                        },
                        {
                            "text": "Groovy",
                            "value": "groovy"
                        },
                        {
                            "text": "Markdown",
                            "value": "markdown"
                        }
                    ]
                 */
                codeLangs: PropTypes.arrayOf(PropTypes.exact({
                    text: PropTypes.string,
                    value: PropTypes.string
                })),
            })
        })
    }),

    /**
             * 配置菜单图片上传
             */
    uploadImage: PropTypes.shape({
        /**
         * 配置上传的服务端地址，
         * 服务端 response body 格式要求如下：
         * 上传成功的返回格式：{
                "errno": 0, // 注意：值是数字，不能是字符串
                "data": {
                    "url": "xxx", // 图片 src ，必须
                    "alt": "yyy", // 图片描述文字，非必须
                    "href": "zzz" // 图片的链接，非必须
                }
            }
         * 上传失败的返回格式：{
                "errno": 1, // 只要不等于 0 就行
                "message": "失败信息"
            }
         */
        server: PropTypes.string,

        /**
         * 配置上传的form-data fieldName ，默认值'wangeditor-uploaded-image'
         */
        fieldName: PropTypes.string,

        /**
         * 配置单个文件的最大体积限制，默认为2M
         */
        maxFileSize: PropTypes.number,

        /**
         * 配置最多可上传几个文件，默认为100
         */
        maxNumberOfFiles: PropTypes.number,

        /**
         * 配置选择文件时的类型限制，默认为['image/*']。如不想限制，则设置为[]
         */
        allowedFileTypes: PropTypes.array,

        /**
         * 配置自定义上传参数，例如传递验证的token等。参数会被添加到formData中，一起上传到服务端
         */
        meta: PropTypes.object,

        /**
         * 配置是否将meta拼接到url参数中，默认false
         */
        metaWithUrl: PropTypes.bool,

        /**
         * 配置自定义增加 http  header
         */
        headers: PropTypes.object,

        /**
         * 配置跨域是否传递cookie ，默认为false
         */
        withCredentials: PropTypes.bool,

        /**
         * 配置超时时间，默认为10秒
         */
        timeout: PropTypes.number,

        /**
         * 配置小于该值就插入base64格式（而不上传），默认为0
         */
        base64LimitSize: PropTypes.number
    }),

    /**
     * 配置菜单视频上传
     */
    uploadVideo: PropTypes.shape({
        /**
         * 配置上传的服务端地址，
         * 服务端 response body 格式要求如下：
         * 上传成功的返回格式：{
                "errno": 0, // 注意：值是数字，不能是字符串
                "data": {
                    "url": "xxx", // 视频 src ，必须
                    "poster": "xxx.png" // 视频封面图片 url ，可选
                }
            }
         * 上传失败的返回格式：{
                "errno": 1, // 只要不等于 0 就行
                "message": "失败信息"
            }
         */
        server: PropTypes.string,

        /**
         * 配置上传的form-data fieldName ，默认值 'wangeditor-uploaded-video'
         */
        fieldName: PropTypes.string,

        /**
         * 配置单个文件的最大体积限制，默认为10M
         */
        maxFileSize: PropTypes.number,

        /**
         * 配置最多可上传几个文件，默认为5
         */
        maxNumberOfFiles: PropTypes.number,

        /**
         * 选择文件时的类型限制，默认为['video/*']。如不想限制，则设置为[]
         */
        allowedFileTypes: PropTypes.array,

        /**
         * 配置自定义上传参数，例如传递验证的token等。参数会被添加到formData中，一起上传到服务端
         */
        meta: PropTypes.object,

        /**
         * 配置是否将meta拼接到url参数中，默认false
         */
        metaWithUrl: PropTypes.bool,

        /**
         * 配置自定义增加 http  header
         */
        headers: PropTypes.object,

        /**
         * 配置跨域是否传递cookie ，默认为false
         */
        withCredentials: PropTypes.bool,

        /**
         * 配置超时时间，默认为10秒
         */
        timeout: PropTypes.number
    }),

    /**
     * 成功的消息提示配置
     */
    successMessage: PropTypes.exact({
        /**
         * 设置消息的css类名
         */
        className: PropTypes.string,

        /**
         * 设置消息的css样式
         */
        style: PropTypes.object,

        /**
         * 设置消息提示显示时长（单位：毫秒），默认为4000
         */
        duration: PropTypes.number,

        /**
         * 自定义消息提示图标
         */
        icon: PropTypes.node,

        /**
         * 设置消息提示的弹出方位，可选的有'top-left'、'top-center'、'top-right'、'bottom-left'、'bottom-center'、'bottom-right'，默认为'top-center'
         */
        position: PropTypes.oneOf([
            'top-left', 'top-center', 'top-right', 'bottom-left', 'bottom-center', 'bottom-right'
        ]),
    }),

    /**
     * 错误的消息提示配置
     */
    errorMessage: PropTypes.exact({
        /**
         * 设置消息的css类名
         */
        className: PropTypes.string,

        /**
         * 设置消息的css样式
         */
        style: PropTypes.object,

        /**
         * 设置消息提示显示时长（单位：毫秒），默认为4000
         */
        duration: PropTypes.number,

        /**
         * 自定义消息提示图标
         */
        icon: PropTypes.node,

        /**
         * 设置消息提示的弹出方位，可选的有'top-left'、'top-center'、'top-right'、'bottom-left'、'bottom-center'、'bottom-right'，默认为'top-center'
         */
        position: PropTypes.oneOf([
            'top-left', 'top-center', 'top-right', 'bottom-left', 'bottom-center', 'bottom-right'
        ]),
    }),

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
FefferyRichTextEditor.defaultProps = {
    locale: 'zh-CN',
    toolbarConfig: {
        modalAppendToBody: false
    },
    editorConfig: {
        readOnly: false,
        autoFocus: true,
        scroll: true
    },
    uploadImage: {
        fieldName: 'wangeditor-uploaded-image',
        maxFileSize: 2,
        maxNumberOfFiles: 100,
        allowedFileTypes: ['image/*'],
        metaWithUrl: false,
        withCredentials: false,
        timeout: 10,
        base64LimitSize: 0
    },
    uploadVideo: {
        fieldName: 'wangeditor-uploaded-video',
        maxFileSize: 10,
        maxNumberOfFiles: 5,
        allowedFileTypes: ['video/*'],
        metaWithUrl: false,
        withCredentials: false,
        timeout: 10
    }
}

export default FefferyRichTextEditor;

export const propTypes = FefferyRichTextEditor.propTypes;
export const defaultProps = FefferyRichTextEditor.defaultProps;