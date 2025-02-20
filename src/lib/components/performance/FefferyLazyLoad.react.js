// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 组件核心
import LazyLoad from 'react-lazy-load';
// 辅助库
import { useLoading } from '../utils';

/**
 * 懒加载容器组件FefferyLazyLoad
 */
const FefferyLazyLoad = ({
    id,
    children,
    style,
    className,
    key,
    height,
    width,
    offset,
    throttle,
    visible = false,
    setProps
}) => {

    return (<LazyLoad
        id={id}
        style={style}
        className={className}
        key={key}
        height={height}
        width={width}
        throttle={throttle}
        offset={offset}
        onContentVisible={() => {
            setProps({
                visible: true
            })
        }}
        data-dash-is-loading={useLoading()} >
        {children}
    </ LazyLoad>);
}

FefferyLazyLoad.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，设置内嵌元素内容
     */
    children: PropTypes.node,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名，支持[动态css](/advanced-classname)
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 设置默认高度
     */
    height: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 设置默认宽度
     */
    width: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 设置元素距离浏览器下边界若干像素距离时开始预加载
     * 默认值：`0`
     */
    offset: PropTypes.number,

    /**
     * 监听容器是否已出现在用户视图中
     */
    visible: PropTypes.bool,

    /**
     * 设置节流所需的延时加载时长（单位：毫秒）
     * 默认值：`250`
     */
    throttle: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyLazyLoad;