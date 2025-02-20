import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyBirdsBackground = React.lazy(() => import(/* webpackChunkName: "feffery_animated_3d_background_three" */ '../../fragments/animations/FefferyBirdsBackground.react'));

/**
 * 3D-Birds背景组件FefferyBirdsBackground
 */
const FefferyBirdsBackground = ({
    mouseControls = true,
    touchControls = true,
    gyroControls = false,
    minHeight = 200.00,
    minWidth = 200.00,
    scale = 1.00,
    scaleMobile = 1.00,
    backgroundColor = '#000000',
    backgroundAlpha = 1,
    color1 = '#ff0000',
    color2 = '#13becf',
    colorMode = 'varianceGradient',
    quantity = 5,
    birdSize = 1,
    wingSpan = 30,
    speedLimit = 5,
    separation = 20,
    alignment = 20,
    cohesion = 20,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyBirdsBackground {
                ...{
                    mouseControls,
                    touchControls,
                    gyroControls,
                    minHeight,
                    minWidth,
                    scale,
                    scaleMobile,
                    backgroundColor,
                    backgroundAlpha,
                    color1,
                    color2,
                    colorMode,
                    quantity,
                    birdSize,
                    wingSpan,
                    speedLimit,
                    separation,
                    alignment,
                    cohesion,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyBirdsBackground.propTypes = {
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
     * 设置是否开启鼠标控
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
     * 设置移动端比例
     * 默认为`1.00`
     */
    scaleMobile: PropTypes.number,

    /**
     * 设置背景颜色
     * 默认为`'#000000'`
     */
    backgroundColor: PropTypes.string,

    /**
     * 设置背景颜色透明度，范围`0`到`1`
     * 默认为`1`
     */
    backgroundAlpha: PropTypes.number,

    /**
     * 设置birds颜色1
     * 默认为`'#ff0000'`
     */
    color1: PropTypes.string,

    /**
     * 设置birds颜色2
     * 默认为`'#13becf'`
     */
    color2: PropTypes.string,

    /**
     * 设置颜色模式，可选的有`'lerp'`、`'variance'`、`'lerpGradient'`、`'varianceGradient'`
     * 默认为`'varianceGradient'`
     */
    colorMode: PropTypes.oneOf(['lerp', 'variance', 'lerpGradient', 'varianceGradient']),

    /**
     * 设置背景质量，范围`1`到`5`
     * 默认为`5`
     */
    quantity: PropTypes.number,

    /**
     * 设置birds大小，范围`1`到`4`
     * 默认为`1`
     */
    birdSize: PropTypes.number,

    /**
     * 设置birds翼展，范围`10`到`40`
     * 默认为`30`
     */
    wingSpan: PropTypes.number,

    /**
     * 设置birds速度限制，范围`1`到`10`
     * 默认为`5`
     */
    speedLimit: PropTypes.number,

    /**
     * 设置birds分离大小，范围`1`到`100
     * 默认为`20`
     */
    separation: PropTypes.number,

    /**
     * 设置birds对齐大小，范围`1`到`100`
     * 默认为`20`
     */
    alignment: PropTypes.number,

    /**
     * 设置birds内聚大小，范围`1`到`100`
     * 默认为`20`
     */
    cohesion: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyBirdsBackground;

export const propTypes = FefferyBirdsBackground.propTypes;
export const defaultProps = FefferyBirdsBackground.defaultProps;