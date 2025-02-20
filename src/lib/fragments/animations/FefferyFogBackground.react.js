// react核心
import React, { useState, useEffect, useRef } from 'react';
// 组件核心
import FOG from 'vanta/dist/vanta.fog.min';
import * as THREE from 'three';
// 辅助库
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/animations/FefferyFogBackground.react';

/**
 * 3D-Fog背景组件FefferyFogBackground
 */
const FefferyFogBackground = ({
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
    highlightColor,
    midtoneColor,
    lowlightColor,
    baseColor,
    blurFactor,
    zoom,
    speed,
    setProps
}) => {

    const [fogEffect, setFogEffect] = useState(null);
    const fogRef = useRef(null);

    useEffect(() => {
        if (!fogEffect) {
            setFogEffect(FOG({
                el: fogRef.current,
                THREE: THREE,
                mouseControls: mouseControls,
                touchControls: touchControls,
                gyroControls: gyroControls,
                minHeight: minHeight,
                minWidth: minWidth,
                highlightColor: highlightColor,
                midtoneColor: midtoneColor,
                lowlightColor: lowlightColor,
                baseColor: baseColor,
                blurFactor: blurFactor,
                zoom: zoom,
                speed: speed
            }))
        }
        return () => {
            if (fogEffect) fogEffect.destroy()
        }
    }, [fogEffect])

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
            ref={fogRef}
            data-dash-is-loading={useLoading()}
        >
            {children}
        </div>
    );
}

export default FefferyFogBackground;

FefferyFogBackground.defaultProps = defaultProps;
FefferyFogBackground.propTypes = propTypes;