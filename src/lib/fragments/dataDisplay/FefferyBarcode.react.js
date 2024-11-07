import React, { useEffect, useRef } from 'react';
import JsBarcode from 'jsbarcode';
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { propTypes, defaultProps } from '../../components/dataDisplay/FefferyBarcode.react';

/**
 * 条形码组件FefferyBarcode
 */
const FefferyBarcode = (props) => {
    // 取得必要属性或参数
    const {
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
        setProps,
        loading_state
    } = props;

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
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }
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
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }
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
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        />
    );
}

export default FefferyBarcode;

FefferyBarcode.defaultProps = defaultProps;
FefferyBarcode.propTypes = propTypes;