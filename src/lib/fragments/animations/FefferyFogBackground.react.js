import React, { useState, useEffect, useRef } from 'react';
import FOG from 'vanta/dist/vanta.fog.min';
import * as THREE from 'three';
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { propTypes, defaultProps } from '../../components/animations/FefferyFogBackground.react';

/**
 * 3D-Fog背景组件FefferyFogBackground
 */
const FefferyFogBackground = (props) => {
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
        highlightColor,
        midtoneColor,
        lowlightColor,
        baseColor,
        blurFactor,
        zoom,
        speed,
        setProps,
        loading_state
    } = props;

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
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        >
            {children}
        </div>
    );
}

export default FefferyFogBackground;

FefferyFogBackground.defaultProps = defaultProps;
FefferyFogBackground.propTypes = propTypes;