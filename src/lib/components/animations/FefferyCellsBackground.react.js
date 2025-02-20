import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyCellsBackground = React.lazy(() => import(/* webpackChunkName: "feffery_animated_3d_background_three" */ '../../fragments/animations/FefferyCellsBackground.react'));

/**
 * 3D-Cells背景组件FefferyCellsBackground
 */
const FefferyCellsBackground = ({
    mouseControls = true,
    touchControls = true,
    gyroControls = false,
    minHeight = 200.00,
    minWidth = 200.00,
    scale = 1.00,
    color1 = '#109090',
    color2 = '#f2e735',
    size = 1.5,
    speed = 1,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyCellsBackground {
                ...{
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
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyCellsBackground.propTypes = {
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
     * 默认为`true`
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
     * 设置比例
     * 默认为`1.00`
     */
    scale: PropTypes.number,

    /**
     * 设置cells颜色1
     * 默认为`'#109090'`
     */
    color1: PropTypes.string,

    /**
     * 设置cells颜色2
     * 默认为`'#f2e735'`
     */
    color2: PropTypes.string,

    /**
     * 设置cells大小，范围`0.2`到`5`
     * 默认为`1.5`
     */
    size: PropTypes.number,

    /**
     * 设置cells动画速度，范围`0`到`5`
     * 默认为`1`
     */
    speed: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyCellsBackground;

export const propTypes = FefferyCellsBackground.propTypes;
export const defaultProps = FefferyCellsBackground.defaultProps;