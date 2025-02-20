// react核心
import React, { useState, useEffect, useMemo } from 'react';
// 组件核心
import Vditor from "vditor";
// 样式
import "vditor/dist/index.css";
// 辅助库
import useCss from '../../hooks/useCss';
import { isString, isUndefined } from 'lodash';
import { useRequest } from 'ahooks';
import { v4 as uuidv4 } from 'uuid';
// 参数类型
import { propTypes, defaultProps } from '../../components/editor/FefferyVditor.react';

/**
 * 类Typora的markdown编辑器组件FefferyVditor
 */
const FefferyVditor = ({
    id,
    className,
    style,
    key,
    debounceWait,
    undoDelay,
    height,
    minHeight,
    width,
    placeholder,
    lang,
    tab,
    typewriterMode,
    cdn,
    mode,
    debuggerMode,
    value,
    theme,
    icon,
    toolbar,
    toolbarConfig,
    counter,
    cache,
    preview,
    image,
    link,
    hint,
    upload,
    resize,
    classes,
    fullscreen,
    outline,
    htmlValue,
    selectedValue,
    wordCount,
    resizeHeight,
    setProps
}) => {

    const [vd, setVd] = useState();
    const [valueTrigger, setValueTrigger] = useState('initial');

    const { run: syncValue } = useRequest(
        (value) => {
            setProps({
                value: value,
                htmlValue: vd.getHTML()
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

    const optionCounter = useMemo(() => {
        return {
            ...counter,
            after: (length) => {
                setProps({ wordCount: length })
            }
        }
    }, [counter])

    const optionResize = useMemo(() => {
        return {
            ...resize,
            after: (height) => {
                setProps({ resizeHeight: height })
            }
        }
    }, [resize])

    const options = useMemo(() => {
        const vars = {
            debugger: debuggerMode,
            counter: optionCounter,
            resize: optionResize,
            undoDelay,
            height,
            minHeight,
            width,
            placeholder,
            lang,
            tab,
            typewriterMode,
            cdn,
            mode,
            value,
            theme,
            icon,
            toolbar,
            toolbarConfig,
            cache,
            preview,
            image,
            link,
            hint,
            upload,
            classes,
            fullscreen,
            outline,
        };

        return Object.entries(vars).reduce((acc, [key, value]) => {
            if (!isUndefined(value)) {
                acc[key] = value;
            }
            return acc;
        }, {});
    }, [undoDelay, height, minHeight, width, placeholder, lang, tab, typewriterMode, cdn, mode, debuggerMode, value, theme, icon,
        toolbar, toolbarConfig, optionCounter, cache, preview, image, link, hint, upload, optionResize, classes, fullscreen, outline])

    useEffect(() => {
        if (vd && valueTrigger === 'initial') {
            vd.setValue(isUndefined(value) ? "" : value);
        }
        // Clear the effect
        return () => {
            setValueTrigger('initial');
        };
    }, [vd, value]);


    useEffect(() => {
        const vditor = new Vditor(containerId, {
            ...options,
            after: () => {
                setVd(vditor);
            },
            input: (value) => {
                setValueTrigger('event');
                syncValue(value);
            },
            select: (value) => {
                setProps({ selectedValue: value })
            }
        });
        // Clear the effect
        return () => {
            vd?.destroy();
            setVd(undefined);
        };
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
        />
    );
}

export default FefferyVditor;

FefferyVditor.defaultProps = defaultProps;
FefferyVditor.propTypes = propTypes;