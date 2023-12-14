import React, { useEffect, useMemo, useCallback } from 'react';
import "cherry-markdown/dist/cherry-markdown.css";
import Cherry from 'cherry-markdown';
import { pinyin } from 'pinyin_js';
import { v4 as uuidv4 } from 'uuid';
import upload from '../utils/upload';
import MathJax from 'mathjax/es5/tex-svg';
import katex from 'katex';
import 'katex/dist/katex.css';
import { propTypes, defaultProps } from '../components/FefferyMarkdownEditor.react';
import FefferyStyle from '../components/FefferyStyle.react';

// 定义markdown编辑器组件FefferyMarkdownEditor，api参数参考https://github.com/Tencent/cherry-markdown/wiki/%E9%85%8D%E7%BD%AE%E9%A1%B9%E5%85%A8%E8%A7%A3
const FefferyMarkdownEditor = (props) => {
    // 取得必要属性或参数
    let {
        id,
        className,
        style,
        value,
        html,
        engine,
        editor,
        toolbars,
        drawioIframeUrl,
        fileTypeLimitMap,
        uploadConfig,
        fineControl,
        previewer,
        theme,
        isPreviewOnly,
        autoScrollByCursor,
        forceAppend,
        locale,
        autoScrollByHashAfterInit,
        setProps,
        loading_state
    } = props;

    const containerId = useMemo(() => {
        return id || uuidv4();
    }, []);

    /**
     * 上传文件函数
     * @param file 上传文件的文件对象
     * @param callback 回调函数，回调函数接收两个参数，第一个参数为文件上传后的url，第二个参数可选，为额外配置信息
     */
    const fileUpload = useCallback((file, callback) => {
        // 安全获取嵌套对象属性函数
        function getNestedProperty(obj, path) {
            return path.split('.').reduce((acc, part) => acc && acc[part], obj);
        }
        uploadConfig.filename = uploadConfig.filename ? uploadConfig.filename : 'file';
        let uploadOptions = {
            ...uploadConfig,
            file: file,
            onProgress: (e) => {
                console.log(e);
            },
            onSuccess: (res) => {
                let url = getNestedProperty(res, uploadConfig.responseUrl || 'data.url');
                if (fineControl.isOpen) {
                    // 如果上传的是视频
                    if (/video/i.test(file.type)) {
                        fineControl.videoFineControlOptions = fineControl.videoFineControlOptions || {};
                        const { posterUrl, isPoster } = fineControl.videoFineControlOptions;
                        fineControl.videoFineControlOptions.poster = `${posterUrl || url}?poster=${isPoster || ''}`;
                        callback(url, fineControl.videoFineControlOptions);
                    } else if (/image/i.test(file.type)) {
                        // 如果上传的是图片
                        callback(url, fineControl.imageFineControlOptions);
                    } else {
                        // 如果上传的是文件
                        callback(url);
                    }
                } else {
                    callback(url);
                }
            },
            onError: (err) => {
                console.log(err);
            }
        }
        let req = upload(uploadOptions)
        if (req && req.then) {
            req.then(uploadOptions.onSuccess, uploadOptions.onError);
        }
    }, [])

    const editorAllConfig = useMemo(() => {
        engine.global = {
            ...engine.global,
            urlProcessor(url, srcType) {
                console.log(`url-processor`, url, srcType);
                return url;
            }
        }
        let engineOptions = { engine: engine };
        let editorOptions = editor ? { editor: editor } : {};
        let toolbarsOptions = toolbars ? { toolbars: toolbars } : {};
        let fileTypeLimitMapOptions = fileTypeLimitMap ? { fileTypeLimitMap: fileTypeLimitMap } : {};
        let previewerOptions = previewer ? { previewer: previewer } : {};
        let callbackOptions = {
            callback: {
                afterChange: (text, html) => {
                    setProps({
                        value: text,
                        html: html
                    });
                },
                changeString2Pinyin: pinyin
            }
        }
        let fileUploadOptions = uploadConfig.action ? { fileUpload: fileUpload } : {};
        return {
            ...engineOptions,
            ...editorOptions,
            ...toolbarsOptions,
            ...fileTypeLimitMapOptions,
            ...previewerOptions,
            ...callbackOptions,
            ...fileUploadOptions,
            drawioIframeUrl: drawioIframeUrl,
            theme: theme,
            isPreviewOnly: isPreviewOnly,
            autoScrollByCursor: autoScrollByCursor,
            forceAppend: forceAppend,
            locale: locale,
            autoScrollByHashAfterInit: autoScrollByHashAfterInit
        }
    }, [engine, editor, toolbars, drawioIframeUrl, fileTypeLimitMap, previewer, theme, isPreviewOnly, autoScrollByCursor, forceAppend, locale, autoScrollByHashAfterInit])

    useEffect(() => {
        const cherryInstance = new Cherry({
            ...editorAllConfig,
            id: containerId,
            value: value,
            externals: {
                katex: katex,
                MathJax: MathJax,
            }
        });
    }, []);

    return (
        <div
            id={containerId}
            className={className}
            style={style}
        >
            <FefferyStyle
                rawStyle={
                    `
                    iframe.cherry-dialog-iframe {
                        width: 100%;
                        height: 100%;
                    }
                    `
                }
            />
        </div>
    );
}

export default FefferyMarkdownEditor;

FefferyMarkdownEditor.defaultProps = defaultProps;
FefferyMarkdownEditor.propTypes = propTypes;