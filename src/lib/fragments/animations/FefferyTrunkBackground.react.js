// react核心
import React, { useState, useEffect, useRef } from 'react';
// 组件核心
import TRUNK from 'vanta/dist/vanta.trunk.min';
import p5 from 'p5';
// 辅助库
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
// 参数类型
import { propTypes, defaultProps } from '../../components/animations/FefferyTrunkBackground.react';
import { useLoading } from '../../components/utils';

/**
 * 3D-Trunk背景组件FefferyTrunkBackground
 */
const FefferyTrunkBackground = ({
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
    spacing,
    chaos,
    setProps
}) => {

    const [trunkEffect, setTrunkEffect] = useState(null);
    const trunkRef = useRef(null);

    useEffect(() => {
        if (!trunkEffect) {
            setTrunkEffect(TRUNK({
                el: trunkRef.current,
                p5: p5,
                mouseControls: mouseControls,
                touchControls: touchControls,
                gyroControls: gyroControls,
                minHeight: minHeight,
                minWidth: minWidth,
                scale: scale,
                scaleMobile: scaleMobile,
                backgroundColor: backgroundColor,
                color: color,
                spacing: spacing,
                chaos: chaos
            }))
        }
        return () => {
            if (trunkEffect) trunkEffect.destroy()
        }
    }, [trunkEffect])

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
            ref={trunkRef}
            data-dash-is-loading={useLoading()}
        >
            {children}
        </div>
    );
}

export default FefferyTrunkBackground;

FefferyTrunkBackground.defaultProps = defaultProps;
FefferyTrunkBackground.propTypes = propTypes;