import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyHaloBackground = React.lazy(() => import(/* webpackChunkName: "feffery_animated_3d_background_three" */ '../../fragments/animations/FefferyHaloBackground.react'));

/**
 * 3D-Halo背景组件FefferyHaloBackground
 */
const FefferyHaloBackground = ({
    mouseControls = true,
    touchControls = true,
    gyroControls = false,
    minHeight = 200.00,
    minWidth = 200.00,
    backgroundColor = '#131a43',
    baseColor = '#112966',
    size = 1,
    amplitudeFactor = 1,
    xOffset = 0,
    yOffset = 0,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyHaloBackground {
                ...{
                    mouseControls,
                    touchControls,
                    gyroControls,
                    minHeight,
                    minWidth,
                    backgroundColor,
                    baseColor,
                    size,
                    amplitudeFactor,
                    xOffset,
                    yOffset,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyHaloBackground.propTypes = {
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
     * 设置背景颜色
     * 默认为`'#131a43'`
     */
    backgroundColor: PropTypes.string,

    /**
     * 设置基本颜色
     * 默认为`'#112966'`
     */
    baseColor: PropTypes.string,

    /**
     * 设置动画大小，范围`0.1`到`3`
     * 默认为`1`
     */
    size: PropTypes.number,

    /**
     * 设置动画振幅因子，范围`0`到`3`
     * 默认为`1`
     */
    amplitudeFactor: PropTypes.number,

    /**
     * 设置x轴偏移量，范围为`-0.5`到`0.5`
     * 默认为`0`
     */
    xOffset: PropTypes.number,

    /**
     * 设置y轴偏移量，范围为`-0.5`到`0.5`
     * 默认为`0`
     */
    yOffset: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyHaloBackground;

export const propTypes = FefferyHaloBackground.propTypes;
export const defaultProps = FefferyHaloBackground.defaultProps;