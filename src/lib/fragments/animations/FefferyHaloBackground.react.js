// react核心
import React, { useState, useEffect, useRef } from 'react';
// 组件核心
import HALO from 'vanta/dist/vanta.halo.min';
import * as THREE from 'three';
// 辅助库
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/animations/FefferyHaloBackground.react';

/**
 * 3D-Halo背景组件FefferyHaloBackground
 */
const FefferyHaloBackground = ({
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
    backgroundColor,
    baseColor,
    size,
    amplitudeFactor,
    xOffset,
    yOffset,
    setProps
}) => {

    const [haloEffect, setHaloEffect] = useState(null);
    const haloRef = useRef(null);

    useEffect(() => {
        if (!haloEffect) {
            setHaloEffect(HALO({
                el: haloRef.current,
                THREE: THREE,
                mouseControls: mouseControls,
                touchControls: touchControls,
                gyroControls: gyroControls,
                minHeight: minHeight,
                minWidth: minWidth,
                backgroundColor: backgroundColor,
                baseColor: baseColor,
                size: size,
                amplitudeFactor: amplitudeFactor,
                xOffset: xOffset,
                yOffset: yOffset
            }))
        }
        return () => {
            if (haloEffect) haloEffect.destroy()
        }
    }, [haloEffect])

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
            ref={haloRef}
            data-dash-is-loading={useLoading()}
        >
            {children}
        </div>
    );
}

export default FefferyHaloBackground;

FefferyHaloBackground.defaultProps = defaultProps;
FefferyHaloBackground.propTypes = propTypes;