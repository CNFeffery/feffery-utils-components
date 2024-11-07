import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyRichTextEditor = React.lazy(() => import(/* webpackChunkName: "feffery_rich_text_editor" */ '../../fragments/editor/FefferyRichTextEditor.react'));

/**
 * 富文本编辑器组件FefferyRichTextEditor
 */
const FefferyRichTextEditor = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyRichTextEditor {...props} />
        </Suspense>
    );
}

FefferyRichTextEditor.propTypes = {
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
     * 组件语言，可选的有`'zh-CN'`、`'en'`
     * 默认值：`'zh-CN'`
     */
    locale: PropTypes.oneOf(['zh-CN', 'en']),

    /**
     * 编辑器模式，可选的有`'default'`、`'simple'`，`'default'`模式 - 集成了 wangEditor 所有功能，`'simple'`模式 - 仅有部分常见功能，但更加简洁易用
     * 默认值：`'default'`
     */
    mode: PropTypes.oneOf(['default', 'simple']),

    /**
     * 编辑器`html`格式内容
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
         * 配置工具栏显示的菜单key，默认工具栏从左至右菜单对应的key为<br/>
         * [<br/>
                &emsp;"headerSelect",<br/>
                &emsp;"blockquote",<br/>
                &emsp;"|",<br/>
                &emsp;"bold",<br/>
                &emsp;"underline",<br/>
                &emsp;"italic",<br/>
                &emsp;{<br/>
                    &emsp;&emsp;"key": "group-more-style",<br/>
                    &emsp;&emsp;"title": "更多",<br/>
                    &emsp;&emsp;"iconSvg": "<svg viewBox=\"0 0 1024 1024\"><path d=\"M204.8 505.6m-76.8 0a76.8 76.8 0 1 0 153.6 0 76.8 76.8 0 1 0-153.6 0Z\"></path><path d=\"M505.6 505.6m-76.8 0a76.8 76.8 0 1 0 153.6 0 76.8 76.8 0 1 0-153.6 0Z\"></path><path d=\"M806.4 505.6m-76.8 0a76.8 76.8 0 1 0 153.6 0 76.8 76.8 0 1 0-153.6 0Z\"></path></svg>",<br/>
                    &emsp;&emsp;"menuKeys": [<br/>
                        &emsp;&emsp;&emsp;"through",<br/>
                        &emsp;&emsp;&emsp;"code",<br/>
                        &emsp;&emsp;&emsp;"sup",<br/>
                        &emsp;&emsp;&emsp;"sub",<br/>
                        &emsp;&emsp;&emsp;"clearStyle"</br>
                    &emsp;&emsp;]<br/>
                &emsp;},<br/>
                &emsp;"color",<br/>
                &emsp;"bgColor",<br/>
                &emsp;"|",<br/>
                &emsp;"fontSize",<br/>
                &emsp;"fontFamily",<br/>
                &emsp;"lineHeight",<br/>
                &emsp;"|",<br/>
                &emsp;"bulletedList",<br/>
                &emsp;"numberedList",<br/>
                &emsp;"todo",<br/>
                &emsp;{<br/>
                    &emsp;&emsp;"key": "group-justify",<br/>
                    &emsp;&emsp;"title": "对齐",<br/>
                    &emsp;&emsp;"iconSvg": "<svg viewBox=\"0 0 1024 1024\"><path d=\"M768 793.6v102.4H51.2v-102.4h716.8z m204.8-230.4v102.4H51.2v-102.4h921.6z m-204.8-230.4v102.4H51.2v-102.4h716.8zM972.8 102.4v102.4H51.2V102.4h921.6z\"></path></svg>",<br/>
                    &emsp;&emsp;"menuKeys": [<br/>
                        &emsp;&emsp;&emsp;"justifyLeft",<br/>
                        &emsp;&emsp;&emsp;"justifyRight",<br/>
                        &emsp;&emsp;&emsp;"justifyCenter",<br/>
                        &emsp;&emsp;&emsp;"justifyJustify"</br>
                    &emsp;&emsp;]<br/>
                &emsp;},<br/>
                &emsp;{<br/>
                    &emsp;&emsp;"key": "group-indent",<br/>
                    &emsp;&emsp;"title": "缩进",<br/>
                    &emsp;&emsp;"iconSvg": "<svg viewBox=\"0 0 1024 1024\"><path d=\"M0 64h1024v128H0z m384 192h640v128H384z m0 192h640v128H384z m0 192h640v128H384zM0 832h1024v128H0z m0-128V320l256 192z\"></path></svg>",<br/>
                    &emsp;&emsp;"menuKeys": [<br/>
                        &emsp;&emsp;&emsp;"indent",<br/>
                        &emsp;&emsp;&emsp;"delIndent"</br>
                    &emsp;&emsp;]<br/>
                &emsp;},<br/>
                &emsp;"|",<br/>
                &emsp;"emotion",</br>
                &emsp;"insertLink",<br/>
                &emsp;{<br/>
                    &emsp;&emsp;"key": "group-image",<br/>
                    &emsp;&emsp;"title": "图片",<br/>
                    &emsp;&emsp;"iconSvg": "<svg viewBox=\"0 0 1024 1024\"><path d=\"M959.877 128l0.123 0.123v767.775l-0.123 0.122H64.102l-0.122-0.122V128.123l0.122-0.123h895.775zM960 64H64C28.795 64 0 92.795 0 128v768c0 35.205 28.795 64 64 64h896c35.205 0 64-28.795 64-64V128c0-35.205-28.795-64-64-64zM832 288.01c0 53.023-42.988 96.01-96.01 96.01s-96.01-42.987-96.01-96.01S682.967 192 735.99 192 832 234.988 832 288.01zM896 832H128V704l224.01-384 256 320h64l224.01-192z\"></path></svg>",<br/>
                    &emsp;&emsp;"menuKeys": [<br/>
                        &emsp;&emsp;&emsp;"insertImage",<br/>
                        &emsp;&emsp;&emsp;"uploadImage"<br/>
                    &emsp;&emsp;]<br/>
                &emsp;},<br/>
                &emsp;{<br/>
                    &emsp;&emsp;"key": "group-video",<br/>
                    &emsp;&emsp;"title": "视频",<br/>
                    &emsp;&emsp;"iconSvg": "<svg viewBox=\"0 0 1024 1024\"><path d=\"M981.184 160.096C837.568 139.456 678.848 128 512 128S186.432 139.456 42.816 160.096C15.296 267.808 0 386.848 0 512s15.264 244.16 42.816 351.904C186.464 884.544 345.152 896 512 896s325.568-11.456 469.184-32.096C1008.704 756.192 1024 637.152 1024 512s-15.264-244.16-42.816-351.904zM384 704V320l320 192-320 192z\"></path></svg>",<br/
                    &emsp;&emsp;"menuKeys": [<br/>
                        &emsp;&emsp;&emsp;"insertVideo",<br/>
                        &emsp;&emsp;&emsp;"uploadVideo"<br/>
                    &emsp;&emsp;]<br/>
                &emsp;},<br/>
                &emsp;"insertTable",<br/>
                &emsp;"codeBlock",<br/>
                &emsp;"divider",<br/>
                &emsp;"|",<br/>
                &emsp;"undo",<br/>
                &emsp;"redo",<br/>
                &emsp;"|",<br/>
                &emsp;"fullScreen"<br/>
            ]
        */
        toolbarKeys: PropTypes.array,

        /**
         * 是否将菜单弹出的`modal`添加到`body`下
         * 默认值：`false`
         */
        modalAppendToBody: PropTypes.bool,
    }),

    /**
     * 编辑器配置
     */
    editorConfig: PropTypes.shape({
        /**
         * 配置编辑器`placeholder`
         */
        placeholder: PropTypes.string,

        /**
         * 配置编辑器是否只读
         * 默认值：`false`
         */
        readOnly: PropTypes.bool,

        /**
         * 配置编辑器默认是否`focus`
         * 默认值：`true`
         */
        autoFocus: PropTypes.bool,

        /**
         * 配置编辑器是否支持滚动，注意，此时不要固定`editor-container`的高度，设置一个`min-height`即可，TIP：可将`scroll`设置为`false`的情况：编辑器高度自增、在线文档，如腾讯文档、语雀那样的
         * 默认值：`true`
         */
        scroll: PropTypes.bool,

        /**
         * 配置编辑器的`maxlength`，TIP：无特殊需求，请慎用`maxLength`，这可能会导致编辑器内容过多时，编辑卡顿
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
                 * 配置代码语言，可用的有：<br/>
                 * [<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "CSS",<br/>
                            &emsp;&emsp;"value": "css"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "HTML",<br/>
                            &emsp;&emsp;"value": "html"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "XML",<br/>
                            &emsp;&emsp;"value": "xml"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "Javascript",<br/>
                            &emsp;&emsp;"value": "javascript"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "Typescript",<br/>
                            &emsp;&emsp;"value": "typescript"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "JSX",<br/>
                            &emsp;&emsp;"value": "jsx"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "Go",<br/>
                            &emsp;&emsp;"value": "go"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "PHP",<br/>
                            &emsp;&emsp;"value": "php"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "C",<br/>
                            &emsp;&emsp;"value": "c"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "Python",<br/>
                            &emsp;&emsp;"value": "python"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "Java",<br/>
                            &emsp;&emsp;"value": "java"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "C++",<br/>
                            &emsp;&emsp;"value": "cpp"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "C#",<br/>
                            &emsp;&emsp;"value": "csharp"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "Visual Basic",<br/>
                            &emsp;&emsp;"value": "visual-basic"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "SQL",<br/>
                            &emsp;&emsp;"value": "sql"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "Ruby",<br/>
                            &emsp;&emsp;"value": "ruby"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "Swift",<br/>
                            &emsp;&emsp;"value": "swift"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "Bash",<br/>
                            &emsp;&emsp;"value": "bash"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "Lua",<br/>
                            &emsp;&emsp;"value": "lua"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "Groovy",<br/>
                            &emsp;&emsp;"value": "groovy"<br/>
                        &emsp;},<br/>
                        &emsp;{<br/>
                            &emsp;&emsp;"text": "Markdown",<br/>
                            &emsp;&emsp;"value": "markdown"<br/>
                        &emsp;}<br/>
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
         * 配置上传的服务端地址，服务端`response body`格式要求如下：<br/>
         * 上传成功的返回格式：<br/>
         * {<br/>
                &emsp;"errno": 0, // 注意：值是数字，不能是字符串<br/>
                &emsp;"data": {<br/>
                    &emsp;&emsp;"url": "xxx", // 图片 src ，必须<br/>
                    &emsp;&emsp;"alt": "yyy", // 图片描述文字，非必须<br/>
                    &emsp;&emsp;"href": "zzz" // 图片的链接，非必须<br/>
                &emsp;}<br/>
            }<br/>
         * 上传失败的返回格式：<br/>{<br/>
                &emsp;"errno": 1, // 只要不等于 0 就行<br/>
                &emsp;"message": "失败信息"<br/>
            }
         */
        server: PropTypes.string,

        /**
         * 配置上传的`form-data fieldName`
         * 默认值：`'wangeditor-uploaded-image'`
         */
        fieldName: PropTypes.string,

        /**
         * 配置单个文件的最大体积限制，单位为`B`
         * 默认值：`2 * 1024 * 1024`
         */
        maxFileSize: PropTypes.number,

        /**
         * 配置最多可上传几个文件
         * 默认值：`100`
         */
        maxNumberOfFiles: PropTypes.number,

        /**
         * 配置选择文件时的类型限制，默认为`['image/*']`，如不想限制，则设置为`[]`
         */
        allowedFileTypes: PropTypes.array,

        /**
         * 配置自定义上传参数，例如传递验证的`token`等，参数会被添加到`formData`中，一起上传到服务端
         */
        meta: PropTypes.object,

        /**
         * 配置是否将`meta`拼接到`url`参数中
         * 默认`false`
         */
        metaWithUrl: PropTypes.bool,

        /**
         * 配置自定义增加`http  header`
         */
        headers: PropTypes.object,

        /**
         * 配置跨域是否传递`cookie`
         * 默认值：`false`
         */
        withCredentials: PropTypes.bool,

        /**
         * 配置超时时间，单位：秒
         * 默认值：`10`
         */
        timeout: PropTypes.number,

        /**
         * 配置小于该值就插入`base64`格式（而不上传）
         * 默认值：`0`
         */
        base64LimitSize: PropTypes.number
    }),

    /**
     * 配置菜单视频上传
     */
    uploadVideo: PropTypes.shape({
        /**
         * 配置上传的服务端地址，服务端`response body`格式要求如下：<br/>
         * 上传成功的返回格式：<br/>
         * {<br/>
                &emsp;"errno": 0, // 注意：值是数字，不能是字符串<br/>
                &emsp;"data": {<br>
                    &emsp;&emsp;"url": "xxx", // 视频 src ，必须<br/>
                    &emsp;&emsp;"poster": "xxx.png" // 视频封面图片 url ，可选<br>
                &emsp;}<br/>
            }<br/>
         * 上传失败的返回格式：<br/>
            {<br/>
                &emsp;"errno": 1, // 只要不等于 0 就行<br/>
                &emsp;"message": "失败信息"<br/>
            }<br/>
         */
        server: PropTypes.string,

        /**
         * 配置上传的`form-data fieldName`
         * 默认值：`'wangeditor-uploaded-video'`
         */
        fieldName: PropTypes.string,

        /**
         * 配置单个文件的最大体积限制，单位为`B`
         * 默认值：`10 * 1024 * 1024`
         */
        maxFileSize: PropTypes.number,

        /**
         * 配置最多可上传几个文件
         * 默认值：`5`
         */
        maxNumberOfFiles: PropTypes.number,

        /**
         * 选择文件时的类型限制，默认为`['video/*']`，如不想限制，则设置为`[]`
         */
        allowedFileTypes: PropTypes.array,

        /**
         * 配置自定义上传参数，例如传递验证的`token`等，参数会被添加到`formData`中，一起上传到服务端
         */
        meta: PropTypes.object,

        /**
         * 配置是否将`meta`拼接到`url`参数中
         * 默认`false`
         */
        metaWithUrl: PropTypes.bool,

        /**
         * 配置自定义增加`http  header`
         */
        headers: PropTypes.object,

        /**
         * 配置跨域是否传递`cookie`
         * 默认值：`false`
         */
        withCredentials: PropTypes.bool,

        /**
         * 配置超时时间，单位：秒
         * 默认值：`10`
         */
        timeout: PropTypes.number
    }),

    /**
     * 成功的消息提示配置
     */
    successMessage: PropTypes.exact({
        /**
         * 设置消息的`css`类名
         */
        className: PropTypes.string,

        /**
         * 设置消息的`css`样式
         */
        style: PropTypes.object,

        /**
         * 设置消息提示显示时长（单位：毫秒）
         * 默认值：`4000`
         */
        duration: PropTypes.number,

        /**
         * 自定义消息提示图标
         */
        icon: PropTypes.node,

        /**
         * 设置消息提示的弹出方位，可选的有`'top-left'`、`'top-center'`、`'top-right'`、`'bottom-left'`、`'bottom-center'`、`'bottom-right'`
         * 默认值：`'top-center'`
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
         * 设置消息的`css`类名
         */
        className: PropTypes.string,

        /**
         * 设置消息的`css`样式
         */
        style: PropTypes.object,

        /**
         * 设置消息提示显示时长（单位：毫秒）
         * 默认值：`4000`
         */
        duration: PropTypes.number,

        /**
         * 自定义消息提示图标
         */
        icon: PropTypes.node,

        /**
         * 设置消息提示的弹出方位，可选的有`'top-left'`、`'top-center'`、`'top-right'`、`'bottom-left'`、`'bottom-center'`、`'bottom-right'`
         * 默认值：`'top-center'`
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
    mode: 'default',
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
        maxFileSize: 2 * 1024 * 1024,
        maxNumberOfFiles: 100,
        allowedFileTypes: ['image/*'],
        metaWithUrl: false,
        withCredentials: false,
        timeout: 10,
        base64LimitSize: 0
    },
    uploadVideo: {
        fieldName: 'wangeditor-uploaded-video',
        maxFileSize: 10 * 1024 * 1024,
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