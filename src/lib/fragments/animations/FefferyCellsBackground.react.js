import React, { useState, useEffect, useRef } from 'react';
import CELLS from 'vanta/dist/vanta.cells.min';
import * as THREE from 'three';
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { propTypes, defaultProps } from '../../components/animations/FefferyCellsBackground.react';

// 定义3d背景之cells背景组件FefferyCellsBackground
const FefferyCellsBackground = (props) => {
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
        color1,
        color2,
        size,
        speed,
        setProps,
        loading_state
    } = props;

    const [cellsEffect, setCellsEffect] = useState(null);
    const cellsRef = useRef(null);

    useEffect(() => {
        if (!cellsEffect) {
            setCellsEffect(CELLS({
                el: cellsRef.current,
                THREE: THREE,
                mouseControls: mouseControls,
                touchControls: touchControls,
                gyroControls: gyroControls,
                minHeight: minHeight,
                minWidth: minWidth,
                scale: scale,
                color1: color1,
                color2: color2,
                size: size,
                speed: speed
            }))
        }
        return () => {
            if (cellsEffect) cellsEffect.destroy()
        }
    }, [cellsEffect])

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
            ref={cellsRef}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        >
            {children}
        </div>
    );
}

export default FefferyCellsBackground;

FefferyCellsBackground.defaultProps = defaultProps;
FefferyCellsBackground.propTypes = propTypes;