import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyAutoAnimate = React.lazy(() => import(/* webpackChunkName: "feffery_auto_animate" */ '../../fragments/animations/FefferyAutoAnimate.react'));

/**
 * 自动动画组件FefferyAutoAnimate
 */
const FefferyAutoAnimate = ({
    id,
    children,
    style,
    className,
    duration = 0.25,
    easing = 'ease-in-out',
    setProps,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyAutoAnimate {
                ...{
                    id,
                    children,
                    style,
                    className,
                    duration,
                    easing,
                    setProps,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyAutoAnimate.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，要进行动画效果编排的目标元素
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
     * 配置动画时长，单位：秒
     * 默认为`0.25`
     */
    duration: PropTypes.number,

    /**
     * 设置过渡动画函数，同css中的`easing-function`
     * 默认为`'ease-in-out'`
     */
    easing: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyAutoAnimate;

export const propTypes = FefferyAutoAnimate.propTypes;
export const defaultProps = FefferyAutoAnimate.defaultProps;