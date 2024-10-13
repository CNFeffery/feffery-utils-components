import React, { useState, useEffect, useRef } from 'react';
import GLOBE from 'vanta/dist/vanta.globe.min';
import * as THREE from 'three';
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { propTypes, defaultProps } from '../../components/animations/FefferyGlobeBackground.react';

/**
 * 3D-Globe背景组件FefferyGlobeBackground
 */
const FefferyGlobeBackground = (props) => {
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
        color,
        color2,
        size,
        setProps,
        loading_state
    } = props;

    const [globeEffect, setGlobeEffect] = useState(null);
    const globeRef = useRef(null);

    useEffect(() => {
        if (!globeEffect) {
            setGlobeEffect(GLOBE({
                el: globeRef.current,
                THREE: THREE,
                mouseControls: mouseControls,
                touchControls: touchControls,
                gyroControls: gyroControls,
                minHeight: minHeight,
                minWidth: minWidth,
                scale: scale,
                scaleMobile: scaleMobile,
                backgroundColor: backgroundColor,
                color: color,
                color2: color2,
                size: size
            }))
        }
        return () => {
            if (globeEffect) globeEffect.destroy()
        }
    }, [globeEffect])

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
            ref={globeRef}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        >
            {children}
        </div>
    );
}

export default FefferyGlobeBackground;

FefferyGlobeBackground.defaultProps = defaultProps;
FefferyGlobeBackground.propTypes = propTypes;