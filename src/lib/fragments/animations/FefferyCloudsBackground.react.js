// react核心
import React, { useState, useEffect, useRef } from 'react';
// 组件核心
import CLOUDS from 'vanta/dist/vanta.clouds.min';
import * as THREE from 'three';
// 辅助库
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/animations/FefferyCloudsBackground.react';

/**
 * 3D-Clouds背景组件FefferyCloudsBackground
 */
const FefferyCloudsBackground = ({
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
    skyColor,
    cloudColor,
    cloudShadowColor,
    sunColor,
    sunGlareColor,
    sunlightColor,
    speed,
    setProps
}) => {

    const [cloudsEffect, setCloudsEffect] = useState(null);
    const cloudsRef = useRef(null);

    useEffect(() => {
        if (!cloudsEffect) {
            setCloudsEffect(CLOUDS({
                el: cloudsRef.current,
                THREE: THREE,
                mouseControls: mouseControls,
                touchControls: touchControls,
                gyroControls: gyroControls,
                minHeight: minHeight,
                minWidth: minWidth,
                backgroundColor: backgroundColor,
                skyColor: skyColor,
                cloudColor: cloudColor,
                cloudShadowColor: cloudShadowColor,
                sunColor: sunColor,
                sunGlareColor: sunGlareColor,
                sunlightColor: sunlightColor,
                speed: speed
            }))
        }
        return () => {
            if (cloudsEffect) cloudsEffect.destroy()
        }
    }, [cloudsEffect])

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
            ref={cloudsRef}
            data-dash-is-loading={useLoading()}
        >
            {children}
        </div>
    );
}

export default FefferyCloudsBackground;

FefferyCloudsBackground.defaultProps = defaultProps;
FefferyCloudsBackground.propTypes = propTypes;