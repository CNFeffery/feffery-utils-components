import React, { useState, useEffect, useRef } from 'react';
import HALO from 'vanta/dist/vanta.halo.min';
import * as THREE from 'three';
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { propTypes, defaultProps } from '../../components/animations/FefferyHaloBackground.react';

// 定义3d背景之halo背景组件FefferyHaloBackground
const FefferyHaloBackground = (props) => {
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
        baseColor,
        size,
        amplitudeFactor,
        xOffset,
        yOffset,
        setProps,
        loading_state
    } = props;

    const [haloEffect, setHaloEffect] = useState(null);
    const haloRef = useRef(null);

    useEffect(() => {
        if (!haloEffect) {
            setHaloEffect(HALO({
                el: haloRef.current,
                THREE: THREE,
                mouseControls: mouseControls,
                touchControls: touchControls,
                gyroControls: gyroControls,
                minHeight: minHeight,
                minWidth: minWidth,
                backgroundColor: backgroundColor,
                baseColor: baseColor,
                size: size,
                amplitudeFactor: amplitudeFactor,
                xOffset: xOffset,
                yOffset: yOffset
            }))
        }
        return () => {
            if (haloEffect) haloEffect.destroy()
        }
    }, [haloEffect])

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
            ref={haloRef}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        >
            {children}
        </div>
    );
}

export default FefferyHaloBackground;

FefferyHaloBackground.defaultProps = defaultProps;
FefferyHaloBackground.propTypes = propTypes;