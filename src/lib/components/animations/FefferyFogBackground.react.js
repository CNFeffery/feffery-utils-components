import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyFogBackground = React.lazy(() => import(/* webpackChunkName: "feffery_animated_3d_background_three" */ '../../fragments/animations/FefferyFogBackground.react'));

/**
 * 3D-Fog背景组件FefferyFogBackground
 */
const FefferyFogBackground = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyFogBackground {...props} />
        </Suspense>
    );
}


FefferyFogBackground.propTypes = {
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
     * 设置是否开启鼠标控制
     * `默认为true`
     */
    mouseControls: PropTypes.bool,

    /**
     * 设置是否开启触摸控制
     * 默认为`true`
     */
    touchControls: PropTypes.bool,

    /**
     * 设置是否开启陀螺仪控制
     * 默认为`false`
     */
    gyroControls: PropTypes.bool,

    /**
     * 设置最小高度
     * 默认为`200.00`
     */
    minHeight: PropTypes.number,

    /**
     * 设置最小宽度
     * 默认为`200.00`
     */
    minWidth: PropTypes.number,

    /**
     * 设置高亮颜色
     * 默认为`'#ffc300'`
     */
    highlightColor: PropTypes.string,

    /**
     * 设置中间调颜色
     * 默认为`'#ff1f00'`
     */
    midtoneColor: PropTypes.string,

    /**
     * 设置低亮颜色
     * 默认为`'#2d00ff'`
     */
    lowlightColor: PropTypes.string,

    /**
     * 设置基本颜色
     * 默认为`'#ffebeb'`
     */
    baseColor: PropTypes.string,

    /**
     * 设置模糊因子，范围`0.1`到`0.9`
     * 默认为`0.6`
     */
    blurFactor: PropTypes.number,

    /**
     * 设置缩放大小，范围`0.1`到`3`
     * 默认为`1`
     */
    zoom: PropTypes.number,

    /**
     * 设置动画速度，范围`0`到`5`
     * 默认为`1`
     */
    speed: PropTypes.number,

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
FefferyFogBackground.defaultProps = {
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    highlightColor: '#ffc300',
    midtoneColor: '#ff1f00',
    lowlightColor: '#2d00ff',
    baseColor: '#ffebeb',
    blurFactor: 0.6,
    zoom: 1,
    speed: 1
}

export default FefferyFogBackground;

export const propTypes = FefferyFogBackground.propTypes;
export const defaultProps = FefferyFogBackground.defaultProps;