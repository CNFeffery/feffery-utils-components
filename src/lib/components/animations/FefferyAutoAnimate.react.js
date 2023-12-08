import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyAutoAnimate = React.lazy(() => import(/* webpackChunkName: "feffery_auto_animate" */ '../../fragments/animations/FefferyAutoAnimate.react'));

const FefferyAutoAnimate = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyAutoAnimate {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyAutoAnimate.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 要进行动画效果编排的目标元素
     */
    children: PropTypes.node,

    /**
     * css样式
     */
    style: PropTypes.object,

    /**
     * css类名
     */
    className: PropTypes.string,

    /**
     * 配置动画时长，单位：秒
     * 默认为0.25
     */
    duration: PropTypes.number,

    /**
     * 设置过渡动画函数，同css中的easing-function，默认为'ease-in-out'
     */
    easing: PropTypes.string,

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
FefferyAutoAnimate.defaultProps = {
    duration: 0.25,
    easing: 'ease-in-out'
}

export default FefferyAutoAnimate;

export const propTypes = FefferyAutoAnimate.propTypes;
export const defaultProps = FefferyAutoAnimate.defaultProps;