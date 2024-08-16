import Sticky from 'react-stickynode';
import React from 'react';
import PropTypes from 'prop-types';

// 定义粘性布局组件FefferySticky，api参数参考：https://github.com/yahoo/react-stickynode
const FefferySticky = (props) => {
    // 取得必要属性或参数
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

// 定义参数或属性
FefferySticky.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 辅助刷新用唯一标识key值
     */
    key: PropTypes.string,

    /**
     * 组件子元素
     */
    children: PropTypes.node,

    /**
     * 设置是否启用粘性布局效果，默认为true
     */
    enabled: PropTypes.bool,

    /**
     * 用于设置触发粘性布局效果对应的顶部距离阈值，
     * 当传入字符型时，字符应为css选择器规则，则此时的顶部距离阈值
     * 默认为0，
     * 为选择器对应目标元素的高度
     */
    top: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 设置粘性布局元素底部距离文档顶部的像素距离阈值，
     * 当超出这个阈值范围时，粘性状态会被解除；
     * 当传入字符型时，字符应为css选择器规则，则此时当目标元素底部
     * 到达粘性布局元素底部时，粘性状态会被解除
     */
    bottomBoundary: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 设置粘性布局元素的z-index属性
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

// 设置默认参数
FefferySticky.defaultProps = {
    enabled: true,
    top: 0
}

export default FefferySticky;