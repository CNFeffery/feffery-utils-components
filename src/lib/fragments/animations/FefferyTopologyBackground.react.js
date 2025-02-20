// react核心
import React, { useState, useEffect, useRef } from 'react';
// 组件核心
import TOPOLOGY from 'vanta/dist/vanta.topology.min';
import p5 from 'p5';
// 辅助库
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/animations/FefferyTopologyBackground.react';

/**
 * 3D-Topology背景组件FefferyTopologyBackground
 */
const FefferyTopologyBackground = ({
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
    setProps
}) => {

    const [topologyEffect, setTopologyEffect] = useState(null);
    const topologyRef = useRef(null);

    useEffect(() => {
        if (!topologyEffect) {
            setTopologyEffect(TOPOLOGY({
                el: topologyRef.current,
                p5: p5,
                mouseControls: mouseControls,
                touchControls: touchControls,
                gyroControls: gyroControls,
                minHeight: minHeight,
                minWidth: minWidth,
                scale: scale,
                scaleMobile: scaleMobile,
                backgroundColor: backgroundColor,
                color: color
            }))
        }
        return () => {
            if (topologyEffect) topologyEffect.destroy()
        }
    }, [topologyEffect])

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
            ref={topologyRef}
            data-dash-is-loading={useLoading()}
        >
            {children}
        </div>
    );
}

export default FefferyTopologyBackground;

FefferyTopologyBackground.defaultProps = defaultProps;
FefferyTopologyBackground.propTypes = propTypes;