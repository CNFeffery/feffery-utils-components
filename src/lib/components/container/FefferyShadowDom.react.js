// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 组件核心
import root from 'react-shadow';
// 辅助库
import { useLoading } from '../utils';

/**
 * Shadow DOM组件FefferyShadowDom
 */
const FefferyShadowDom = ({
    id,
    key,
    children,
    className,
    style,
    setProps
}) => {

    return (
        <root.div
            id={id}
            key={key}
            className={className}
            style={style}
            data-dash-is-loading={useLoading()} >
            {children}
        </ root.div>
    );
}

FefferyShadowDom.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，内嵌元素
     */
    children: PropTypes.node,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyShadowDom;