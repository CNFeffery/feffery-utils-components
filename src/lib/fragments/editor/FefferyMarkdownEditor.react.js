import React, { useEffect, useMemo, useCallback, useState } from 'react';
import "cherry-markdown/dist/cherry-markdown.css";
import Cherry from 'cherry-markdown/dist/cherry-markdown.core';
import mermaidPlugin from 'cherry-markdown/dist/addons/cherry-code-block-mermaid-plugin';
import { pinyin } from 'pinyin_js';
import { v4 as uuidv4 } from 'uuid';
import upload from '../../utils/upload';
import MathJax from 'mathjax/es5/tex-svg';
import katex from 'katex';
import 'katex/dist/katex.css';
import useCss from '../../hooks/useCss';
import { isString, isUndefined } from 'lodash';
import { useRequest } from 'ahooks';
import { propTypes, defaultProps } from '../../components/editor/FefferyMarkdownEditor.react';
import FefferyStyle from '../../components/styleControl/FefferyStyle.react';


if (window.mermaid) {
    Cherry.usePlugin(mermaidPlugin, {
        mermaid: window.mermaid
    })
}

/**
 * markdown编辑器组件FefferyMarkdownEditor
 */
const FefferyMarkdownEditor = (props) => {
    // 取得必要属性或参数
    let {
        id,
        className,
        style,
        key,
        debounceWait,
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
        customSyntax,
        setProps,
        loading_state
    } = props;

    const [cherry, setCherry] = useState();
    const [valueTrigger, setValueTrigger] = useState('initial');

    const { run: syncValue } = useRequest(
        (text, html) => {
            setProps({
                value: text,
                html: html
            });
        },
        {
            debounceWait: debounceWait,
            manual: true
        }
    )

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
                        fineControl.videoFineControlOptions.poster = `${posterUrl}?poster=${isPoster || false}`;
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
        let customEngine = engine;
        let customSyntaxOptions = {};
        if (customSyntax?.length > 0) {
            customSyntax.forEach(item => {
                const { syntaxName, syntaxType, force, before, reg, result } = item;
                let tmpCustomSyntaxObj = {};

                if (syntaxType == 'inline') {
                    let myInlineHook = Cherry.createSyntaxHook(syntaxName, Cherry.constants.HOOKS_TYPE_LIST.SEN, {
                        makeHtml(str) {
                            return str.replace(this.RULE.reg, function () {
                                let filledResult = result;
                                // 检查并替换 'arguments[0]' 占位符
                                if (filledResult.includes('${arguments[0]}')) {
                                    filledResult = filledResult.replace('${arguments[0]}', arguments[0]);
                                }
                                // 检查并替换 'arguments[1]' 占位符
                                if (filledResult.includes('${arguments[1]}')) {
                                    filledResult = filledResult.replace('${arguments[1]}', arguments[1]);
                                }
                                // 检查并替换 'arguments[2]' 占位符
                                if (filledResult.includes('${arguments[2]}')) {
                                    filledResult = filledResult.replace('${arguments[2]}', arguments[2]);
                                }
                                // 检查并替换 'arguments[3]' 占位符
                                if (filledResult.includes('${arguments[3]}')) {
                                    filledResult = filledResult.replace('${arguments[3]}', arguments[3]);
                                }
                                // 检查并替换 'arguments[4]' 占位符
                                if (filledResult.includes('${arguments[4]}')) {
                                    filledResult = filledResult.replace('${arguments[4]}', arguments[4]);
                                }
                                return filledResult;
                            });
                        },
                        rule(str) {
                            return { reg: new RegExp(reg, 'g') };
                        },
                    });
                    tmpCustomSyntaxObj[syntaxName] = {
                        syntaxClass: myInlineHook,
                        force: force,
                        before: before
                    }
                    Object.assign(customSyntaxOptions, tmpCustomSyntaxObj);
                } else if (syntaxType == 'block') {
                    let myBlockHook = Cherry.createSyntaxHook(syntaxName, Cherry.constants.HOOKS_TYPE_LIST.PAR, {
                        needCache: true,
                        makeHtml(str, sentenceMakeFunc) {
                            const that = this;
                            return str.replace(this.RULE.reg, function () {
                                const lines = that.getLineCount(arguments[0]);
                                const { sign, html } = sentenceMakeFunc(arguments[1]);
                                let filledResult = result;
                                // 检查并替换 'sign' 占位符
                                if (filledResult.includes('${sign}')) {
                                    filledResult = filledResult.replace('${sign}', sign);
                                }
                                // 检查并替换 'lines' 占位符
                                if (filledResult.includes('${lines}')) {
                                    filledResult = filledResult.replace('${lines}', lines);
                                }
                                // 检查并替换 'html' 占位符
                                if (filledResult.includes('${html}')) {
                                    filledResult = filledResult.replace('${html}', html);
                                }
                                // 检查并替换 'arguments[0]' 占位符
                                if (filledResult.includes('${arguments[0]}')) {
                                    filledResult = filledResult.replace('${arguments[0]}', arguments[0]);
                                }
                                // 检查并替换 'arguments[1]' 占位符
                                if (filledResult.includes('${arguments[1]}')) {
                                    filledResult = filledResult.replace('${arguments[1]}', arguments[1]);
                                }
                                // 检查并替换 'arguments[2]' 占位符
                                if (filledResult.includes('${arguments[2]}')) {
                                    filledResult = filledResult.replace('${arguments[2]}', arguments[2]);
                                }
                                // 检查并替换 'arguments[3]' 占位符
                                if (filledResult.includes('${arguments[3]}')) {
                                    filledResult = filledResult.replace('${arguments[3]}', arguments[3]);
                                }
                                // 检查并替换 'arguments[4]' 占位符
                                if (filledResult.includes('${arguments[4]}')) {
                                    filledResult = filledResult.replace('${arguments[4]}', arguments[4]);
                                }
                                return that.pushCache(filledResult, sign, lines);
                            });
                        },
                        rule(str) {
                            return { reg: new RegExp(reg, 'g') };
                        },
                    });
                    tmpCustomSyntaxObj[syntaxName] = {
                        syntaxClass: myBlockHook,
                        force: force,
                        before: before
                    }
                    Object.assign(customSyntaxOptions, tmpCustomSyntaxObj);
                }
            });
        }
        customEngine.global = {
            ...customEngine.global,
            urlProcessor(url, srcType) {
                console.log(`url-processor`, url, srcType);
                return url;
            }
        }
        customEngine.customSyntax = customSyntaxOptions;
        let engineOptions = { engine: customEngine };
        let editorOptions = editor ? { editor: editor } : {};
        let toolbarsOptions = toolbars ? { toolbars: toolbars } : {};
        let fileTypeLimitMapOptions = fileTypeLimitMap ? { fileTypeLimitMap: fileTypeLimitMap } : {};
        let previewerOptions = previewer ? { previewer: previewer } : {};
        let callbackOptions = {
            callback: {
                afterChange: (text, html) => {
                    setValueTrigger('event');
                    syncValue(text, html);
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
    }, [engine, editor, toolbars, drawioIframeUrl, fileTypeLimitMap, previewer, theme, isPreviewOnly, autoScrollByCursor, forceAppend, locale, autoScrollByHashAfterInit, customSyntax])

    useEffect(() => {
        if (cherry && valueTrigger === 'initial') {
            cherry.setMarkdown(isUndefined(value) ? "" : value);
        }
        // Clear the effect
        return () => {
            setValueTrigger('initial');
        };
    }, [cherry, value]);
    
    useEffect(() => {
        let externals = {
            katex: katex,
            MathJax: MathJax,
        }
        if (window.echarts) {
            externals.echarts = window.echarts;
        }
        const cherryMarkdownEditor = new Cherry({
            ...editorAllConfig,
            id: containerId,
            value: value,
            externals: externals
        });
        if (cherryMarkdownEditor) {
            setCherry(cherryMarkdownEditor);
        }
        return () => {
            cherry?.destroy();
            setCherry(undefined);
        }
    }, []);

    return (
        <div
            id={containerId}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            key={key}
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