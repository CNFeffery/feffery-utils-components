import '@wangeditor/editor/dist/css/style.css' // 引入 css
import React, { useState, useEffect } from 'react'
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { i18nChangeLanguage } from '@wangeditor/editor';
import { Editor, Toolbar } from '@wangeditor/editor-for-react';
import toast, { Toaster } from 'react-hot-toast';
import { propTypes, defaultProps } from '../../components/editor/FefferyRichTextEditor.react';

// 定义富文本编辑器组件FefferyRichTextEditor
const FefferyRichTextEditor = (props) => {
    // 取得必要属性或参数
    const {
        id,
        className,
        style,
        key,
        toolbarClassName,
        toolbarStyle,
        editorClassName,
        editorStyle,
        locale,
        mode,
        htmlValue,
        textValue,
        toolbarConfig,
        editorConfig,
        uploadImage,
        uploadVideo,
        successMessage,
        errorMessage,
        setProps,
        loading_state
    } = props;

    // editor 实例
    const [editor, setEditor] = useState(null)

    uploadImage.maxFileSize = uploadImage.maxFileSize ? uploadImage.maxFileSize : 2 * 1024 * 1024;
    uploadVideo.maxFileSize = uploadVideo.maxFileSize ? uploadVideo.maxFileSize : 10 * 1024 * 1024;

    // 当达到maxLength限制时，触发该回调函数
    editorConfig.onMaxLength = function (editor) {
        toast.error(
            locale == 'zh-CN' ? '已超出最大长度限制' : 'Maximum length limit exceeded',
            { ...errorMessage }
        )
    }

    editorConfig.MENU_CONF = editorConfig.MENU_CONF ? editorConfig.MENU_CONF : {};
    // 上传图片相关回调
    editorConfig.MENU_CONF['uploadImage'] = {
        ...uploadImage,
        // 上传之前触发
        onBeforeUpload(file) {
            // file 选中的文件，格式如 { key: file }
            return file

            // 可以 return
            // 1. return file 或者 new 一个 file ，接下来将上传
            // 2. return false ，不上传这个 file
        },

        // 上传进度的回调函数
        onProgress(progress) {
            // progress 是 0-100 的数字
            console.log('progress', progress)
        },

        // 单个文件上传成功之后
        onSuccess(file, res) {
            toast.success(
                locale == 'zh-CN' ? `${file.name}上传成功！` : `${file.name} upload successful`,
                { ...successMessage }
            )
            // console.log(`${file.name}上传成功`, res)
        },

        // 单个文件上传失败
        onFailed(file, res) {
            toast.error(
                locale == 'zh-CN' ? `${file.name}上传失败！\n${res.message}` : `${file.name} upload failed.\n${res.message}`,
                { ...errorMessage }
            )
            // console.log(`${file.name}上传失败`, res)
        },

        // 上传错误，或者触发 timeout 超时
        onError(file, err, res) {
            toast.error(
                locale == 'zh-CN' ? `${file.name}上传出错！\n${err}\n${res.message}` : `${file.name} upload error.\n${err}\n${res.message}`,
                { ...errorMessage }
            )
            // console.log(`${file.name}上传出错`, err, res)
        },
    }

    // 上传视频相关回调
    editorConfig.MENU_CONF['uploadVideo'] = {
        ...uploadVideo,
        // 上传之前触发
        onBeforeUpload(file) {
            // file 选中的文件，格式如 { key: file }
            return file

            // 可以 return
            // 1. return file 或者 new 一个 file ，接下来将上传
            // 2. return false ，不上传这个 file
        },

        // 上传进度的回调函数
        onProgress(progress) {
            // progress 是 0-100 的数字
            console.log('progress', progress)
        },

        // 单个文件上传成功之后
        onSuccess(file, res) {
            toast.success(
                locale == 'zh-CN' ? `${file.name}上传成功！` : `${file.name} upload successful`,
                { ...successMessage }
            )
            // console.log(`${file.name}上传成功`, res)
        },

        // 单个文件上传失败
        onFailed(file, res) {
            toast.error(
                locale == 'zh-CN' ? `${file.name}上传失败！\n${res.message}` : `${file.name} upload failed.\n${res.message}`,
                { ...errorMessage }
            )
            // console.log(`${file.name}上传失败`, res)
        },

        // 上传错误，或者触发 timeout 超时
        onError(file, err, res) {
            toast.error(
                locale == 'zh-CN' ? `${file.name}上传出错！\n${err}\n${res.message}` : `${file.name} upload error.\n${err}\n${res.message}`,
                { ...errorMessage }
            )
            // console.log(`${file.name}上传出错`, err, res)
        },
    }

    // 监听编辑器值变化事件
    const onChange = (editor) => {
        setProps({
            htmlValue: editor.getHtml(),
            textValue: editor.getText()
        })
    }

    // 及时销毁editor，重要！
    useEffect(() => {
        i18nChangeLanguage(locale);
        return () => {
            if (editor == null) return
            editor.destroy()
            setEditor(null)
        }
    }, [editor])

    return (
        <div
            id={id}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            style={{
                border: '1px solid #ccc',
                zIndex: 9999,
                ...style
            }}
            key={key}
        >
            <Toolbar
                className={
                    isString(toolbarClassName) ?
                        toolbarClassName :
                        (toolbarClassName ? useCss(toolbarClassName) : undefined)
                }
                style={{
                    borderBottom: '1px solid #ccc',
                    ...toolbarStyle
                }}
                mode={mode}
                editor={editor}
                defaultConfig={toolbarConfig}
            />
            <Editor
                className={
                    isString(editorClassName) ?
                        editorClassName :
                        (editorClassName ? useCss(editorClassName) : undefined)
                }
                style={editorStyle}
                mode={mode}
                defaultConfig={editorConfig}
                value={htmlValue}
                onCreated={setEditor}
                onChange={onChange}
            />
            <Toaster />
        </div>
    );
}

export default FefferyRichTextEditor;

FefferyRichTextEditor.defaultProps = defaultProps;
FefferyRichTextEditor.propTypes = propTypes;