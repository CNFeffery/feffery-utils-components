// react核心
import React, { useState, useEffect, useRef } from 'react';
// 组件核心
import WAVES from 'vanta/dist/vanta.waves.min';
import * as THREE from 'three';
// 辅助库
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/animations/FefferyWavesBackground.react';

/**
 * 3D-Waves背景组件FefferyWavesBackground
 */
const FefferyWavesBackground = ({
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
    shininess,
    waveHeight,
    waveSpeed,
    zoom,
    setProps
}) => {

    const [wavesEffect, setWavesEffect] = useState(null);
    const wavesRef = useRef(null);

    useEffect(() => {
        if (!wavesEffect) {
            setWavesEffect(WAVES({
                el: wavesRef.current,
                THREE: THREE,
                mouseControls: mouseControls,
                touchControls: touchControls,
                gyroControls: gyroControls,
                minHeight: minHeight,
                minWidth: minWidth,
                scale: scale,
                scaleMobile: scaleMobile,
                color: color,
                shininess: shininess,
                waveHeight: waveHeight,
                waveSpeed: waveSpeed,
                zoom: zoom
            }))
        }
        return () => {
            if (wavesEffect) wavesEffect.destroy()
        }
    }, [wavesEffect])

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
            ref={wavesRef}
            data-dash-is-loading={useLoading()}
        >
            {children}
        </div>
    );
}

export default FefferyWavesBackground;

FefferyWavesBackground.defaultProps = defaultProps;
FefferyWavesBackground.propTypes = propTypes;