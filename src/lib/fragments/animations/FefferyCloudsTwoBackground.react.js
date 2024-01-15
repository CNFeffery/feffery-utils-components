import React, { useState, useEffect, useRef } from 'react';
import CLOUDS2 from 'vanta/dist/vanta.clouds2.min';
import * as THREE from 'three';
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { propTypes, defaultProps } from '../../components/animations/FefferyCloudsTwoBackground.react';

// 定义3d背景之clouds2背景组件FefferyCloudsTwoBackground
const FefferyCloudsTwoBackground = (props) => {
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
        texturePath,
        backgroundColor,
        skyColor,
        cloudColor,
        lightColor,
        speed,
        setProps,
        loading_state
    } = props;

    const [clouds2Effect, setClouds2Effect] = useState(null);
    const clouds2Ref = useRef(null);

    useEffect(() => {
        if (!clouds2Effect) {
            setClouds2Effect(CLOUDS2({
                el: clouds2Ref.current,
                THREE: THREE,
                mouseControls: mouseControls,
                touchControls: touchControls,
                gyroControls: gyroControls,
                minHeight: minHeight,
                minWidth: minWidth,
                scale: scale,
                texturePath: texturePath,
                backgroundColor: backgroundColor,
                skyColor: skyColor,
                cloudColor: cloudColor,
                lightColor: lightColor,
                speed: speed
            }))
        }
        return () => {
            if (clouds2Effect) clouds2Effect.destroy()
        }
    }, [clouds2Effect])

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
            ref={clouds2Ref}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        >
            {children}
        </div>
    );
}

export default FefferyCloudsTwoBackground;

FefferyCloudsTwoBackground.defaultProps = defaultProps;
FefferyCloudsTwoBackground.propTypes = propTypes;