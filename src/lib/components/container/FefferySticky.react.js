// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 组件核心
import Sticky from 'react-stickynode';

/**
 * 粘性布局组件FefferySticky
 */
const FefferySticky = (props) => {
    const {
        id,
        key,
        children,
        enabled,
        top,
        bottomBoundary,
        zIndex,
        setProps,
        loading_state
    } = props;

    return <Sticky
        id={id}
        key={key}
        enabled={enabled}
        top={top}
        bottomBoundary={bottomBoundary}
        innerZ={zIndex}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } >
        {children}
    </ Sticky>;
}

FefferySticky.propTypes = {
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
     * 是否启用粘性布局效果
     * 默认值：`true`
     */
    enabled: PropTypes.bool,

    /**
     * 用于设置触发粘性布局效果对应的顶部距离阈值，当当前元素距离窗口顶部达到此阈值时会触发粘性布局状态，
     * 当传入数值型时，用于设置窗口顶端到当前元素顶部的像素距离阈值，
     * 当传入字符型时，用于定义`css`选择器规则，被此选择器规则匹配到的元素的高度会被作为阈值所使用
     */
    top: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 用于设置解除粘性布局效果对应的底部距离阈值，
     * 当传入数值型时，用于设置页面顶端到当前元素顶部的像素距离阈值，
     * 当传入字符型时，用于定义`css`选择器规则，当该规则匹配到的目标元素底部到达粘性布局元素底部时，粘性状态会被解除
     */
    bottomBoundary: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 粘性布局元素对应`z-index`属性
     */
    zIndex: PropTypes.number,

    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

FefferySticky.defaultProps = {
    enabled: true,
    top: 0
}

export default FefferySticky;