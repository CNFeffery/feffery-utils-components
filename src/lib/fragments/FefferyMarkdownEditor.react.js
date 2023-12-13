import React, { useEffect, useMemo } from 'react';
import "cherry-markdown/dist/cherry-markdown.css";
import Cherry from 'cherry-markdown';
import { pinyin } from 'pinyin_js';
import { v4 as uuidv4 } from 'uuid';
import { propTypes, defaultProps } from '../components/FefferyMarkdownEditor.react';

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
        return {
            ...engineOptions,
            ...editorOptions,
            ...toolbarsOptions,
            ...fileTypeLimitMapOptions,
            ...previewerOptions,
            ...callbackOptions,
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
            value: value
        });

        // 清理cherry实例
        return () => {
            cherryInstance.dispose();
        };
    }, []);

    return (
        <div
            id={containerId}
            className={className}
            style={style}
        />
    );
}

export default FefferyMarkdownEditor;

FefferyMarkdownEditor.defaultProps = defaultProps;
FefferyMarkdownEditor.propTypes = propTypes;