// react核心
import React, { useState, useEffect, useRef } from 'react';
// 组件核心
import BIRDS from 'vanta/dist/vanta.birds.min';
import * as THREE from 'three';
// 辅助库
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/animations/FefferyBirdsBackground.react';

/**
 * 3D-Birds背景组件FefferyBirdsBackground
 */
const FefferyBirdsBackground = ({
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
    backgroundColor,
    backgroundAlpha,
    color1,
    color2,
    colorMode,
    quantity,
    birdSize,
    wingSpan,
    speedLimit,
    separation,
    alignment,
    cohesion,
    setProps
}) => {

    const [birdsEffect, setBirdsEffect] = useState(null);
    const birdsRef = useRef(null);

    useEffect(() => {
        if (!birdsEffect) {
            setBirdsEffect(BIRDS({
                el: birdsRef.current,
                THREE: THREE,
                mouseControls: mouseControls,
                touchControls: touchControls,
                gyroControls: gyroControls,
                minHeight: minHeight,
                minWidth: minWidth,
                scale: scale,
                scaleMobile: scaleMobile,
                backgroundColor: backgroundColor,
                backgroundAlpha: backgroundAlpha,
                color1: color1,
                color2: color2,
                colorMode: colorMode,
                quantity: quantity,
                birdSize: birdSize,
                wingSpan: wingSpan,
                speedLimit: speedLimit,
                separation: separation,
                alignment: alignment,
                cohesion: cohesion
            }))
        }
        return () => {
            if (birdsEffect) birdsEffect.destroy()
        }
    }, [birdsEffect])

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
            ref={birdsRef}
            data-dash-is-loading={useLoading()}
        >{children}</div>
    );
}

export default FefferyBirdsBackground;

FefferyBirdsBackground.defaultProps = defaultProps;
FefferyBirdsBackground.propTypes = propTypes;