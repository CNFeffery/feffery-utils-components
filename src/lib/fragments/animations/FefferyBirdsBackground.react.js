import React, { useState, useEffect, useRef } from 'react';
import BIRDS from 'vanta/dist/vanta.birds.min';
import * as THREE from 'three';
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { propTypes, defaultProps } from '../../components/animations/FefferyBirdsBackground.react';

// 定义3d背景之birds背景组件FefferyBirdsBackground
const FefferyBirdsBackground = (props) => {
    // 取得必要属性或参数
    let {
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
        setProps,
        loading_state
    } = props;

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
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        >
            {children}
        </div>
    );
}

export default FefferyBirdsBackground;

FefferyBirdsBackground.defaultProps = defaultProps;
FefferyBirdsBackground.propTypes = propTypes;