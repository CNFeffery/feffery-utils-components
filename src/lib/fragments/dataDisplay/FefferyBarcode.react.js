// react核心
import React, { useEffect, useRef } from 'react';
// 组件核心
import JsBarcode from 'jsbarcode';
// 辅助库
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/dataDisplay/FefferyBarcode.react';

/**
 * 条形码组件FefferyBarcode
 */
const FefferyBarcode = ({
    id,
    key,
    style,
    className,
    renderer,
    value,
    format,
    width,
    height,
    displayValue,
    text,
    fontOptions,
    font,
    fontSize,
    textAlign,
    textPosition,
    textMargin,
    background,
    lineColor,
    margin,
    marginTop,
    marginBottom,
    marginLeft,
    marginRight,
    flat,
    setProps
}) => {

    const component_loading = useLoading();

    const renderRef = useRef(null);

    useEffect(() => {
        new JsBarcode(
            renderRef.current,
            value,
            {
                format,
                width,
                height,
                displayValue,
                text,
                fontOptions,
                font,
                fontSize,
                textAlign,
                textPosition,
                textMargin,
                background,
                lineColor,
                margin,
                marginTop,
                marginBottom,
                marginLeft,
                marginRight,
                flat
            }
        )
    }, [value]);

    if (renderer === 'img') {
        return (
            <img
                id={id}
                key={key}
                className={
                    isString(className) ?
                        className :
                        (className ? useCss(className) : undefined)
                }
                style={style}
                ref={renderRef}
                data-dash-is-loading={component_loading}
            />
        )
    }

    else if (renderer === 'svg') {
        return (
            <svg
                id={id}
                key={key}
                className={
                    isString(className) ?
                        className :
                        (className ? useCss(className) : undefined)
                }
                style={style}
                ref={renderRef}
                data-dash-is-loading={component_loading}
            />
        )
    }

    return (
        <canvas
            id={id}
            key={key}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            style={style}
            ref={renderRef}
            data-dash-is-loading={component_loading}
        />
    );
}

export default FefferyBarcode;

FefferyBarcode.defaultProps = defaultProps;
FefferyBarcode.propTypes = propTypes;