// react核心
import React, { useState, useEffect, useRef } from 'react';
// 组件核心
import RINGS from 'vanta/dist/vanta.rings.min';
import * as THREE from 'three';
// 辅助库
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
// 参数类型
import { propTypes, defaultProps } from '../../components/animations/FefferyRingsBackground.react';
import { useLoading } from '../../components/utils';

/**
 * 3D-Rings背景组件FefferyRingsBackground
 */
const FefferyRingsBackground = ({
    id,
    children,
    className,
    style,
    key,
    mouseControls,
    touchControls,
    gyroControls,
    minHeight,
    minWidth,
    scale,
    scaleMobile,
    color,
    backgroundColor,
    backgroundAlpha,
    setProps
}) => {

    const [ringsEffect, setRingsEffect] = useState(null);
    const ringsRef = useRef(null);

    useEffect(() => {
        if (!ringsEffect) {
            setRingsEffect(RINGS({
                el: ringsRef.current,
                THREE: THREE,
                mouseControls: mouseControls,
                touchControls: touchControls,
                gyroControls: gyroControls,
                minHeight: minHeight,
                minWidth: minWidth,
                scale: scale,
                scaleMobile: scaleMobile,
                color: color,
                backgroundColor: backgroundColor,
                backgroundAlpha: backgroundAlpha
            }))
        }
        return () => {
            if (ringsEffect) ringsEffect.destroy()
        }
    }, [ringsEffect])

    return (
        <div
            id={id}
            children={children}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            style={style}
            key={key}
            ref={ringsRef}
            data-dash-is-loading={useLoading()}
        >
            {children}
        </div>
    );
}

export default FefferyRingsBackground;

FefferyRingsBackground.defaultProps = defaultProps;
FefferyRingsBackground.propTypes = propTypes;