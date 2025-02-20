// react核心
import React, { useState, useEffect, useRef } from 'react';
// 组件核心
import CELLS from 'vanta/dist/vanta.cells.min';
import * as THREE from 'three';
// 辅助库
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/animations/FefferyCellsBackground.react';

/**
 * 3D-Cells背景组件FefferyCellsBackground
 */
const FefferyCellsBackground = ({
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
    setProps
}) => {

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
            data-dash-is-loading={useLoading()}
        >
            {children}
        </div>
    );
}

export default FefferyCellsBackground;

FefferyCellsBackground.defaultProps = defaultProps;
FefferyCellsBackground.propTypes = propTypes;