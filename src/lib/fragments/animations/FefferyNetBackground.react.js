import React, { useState, useEffect, useRef } from 'react';
import NET from 'vanta/dist/vanta.net.min';
import * as THREE from 'three';
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { propTypes, defaultProps } from '../../components/animations/FefferyNetBackground.react';

/**
 * 3D-Net背景组件FefferyNetBackground
 */
const FefferyNetBackground = (props) => {
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
        backgroundColor,
        points,
        maxDistance,
        spacing,
        showDots,
        setProps,
        loading_state
    } = props;

    const [netEffect, setNetEffect] = useState(null);
    const netRef = useRef(null);

    useEffect(() => {
        if (!netEffect) {
            setNetEffect(NET({
                el: netRef.current,
                THREE: THREE,
                mouseControls: mouseControls,
                touchControls: touchControls,
                gyroControls: gyroControls,
                minHeight: minHeight,
                minWidth: minWidth,
                scale: scale,
                scaleMobile: scaleMobile,
                color: color,
                backgroundColor: backgroundColor,
                points: points,
                maxDistance: maxDistance,
                spacing: spacing,
                showDots: showDots
            }))
        }
        return () => {
            if (netEffect) netEffect.destroy()
        }
    }, [netEffect])

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
            ref={netRef}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        >
            {children}
        </div>
    );
}

export default FefferyNetBackground;

FefferyNetBackground.defaultProps = defaultProps;
FefferyNetBackground.propTypes = propTypes;