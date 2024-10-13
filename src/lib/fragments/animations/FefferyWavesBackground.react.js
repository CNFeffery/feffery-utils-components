import React, { useState, useEffect, useRef } from 'react';
import WAVES from 'vanta/dist/vanta.waves.min';
import * as THREE from 'three';
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { propTypes, defaultProps } from '../../components/animations/FefferyWavesBackground.react';

/**
 * 3D-Waves背景组件FefferyWavesBackground
 */
const FefferyWavesBackground = (props) => {
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
        color,
        shininess,
        waveHeight,
        waveSpeed,
        zoom,
        setProps,
        loading_state
    } = props;

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
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        >
            {children}
        </div>
    );
}

export default FefferyWavesBackground;

FefferyWavesBackground.defaultProps = defaultProps;
FefferyWavesBackground.propTypes = propTypes;