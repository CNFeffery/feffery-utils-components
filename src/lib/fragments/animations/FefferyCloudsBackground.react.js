import React, { useState, useEffect, useRef } from 'react';
import CLOUDS from 'vanta/dist/vanta.clouds.min';
import * as THREE from 'three';
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { propTypes, defaultProps } from '../../components/animations/FefferyCloudsBackground.react';

/**
 * 3D-Clouds背景组件FefferyCloudsBackground
 */
const FefferyCloudsBackground = (props) => {
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
        backgroundColor,
        skyColor,
        cloudColor,
        cloudShadowColor,
        sunColor,
        sunGlareColor,
        sunlightColor,
        speed,
        setProps,
        loading_state
    } = props;

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
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        >
            {children}
        </div>
    );
}

export default FefferyCloudsBackground;

FefferyCloudsBackground.defaultProps = defaultProps;
FefferyCloudsBackground.propTypes = propTypes;