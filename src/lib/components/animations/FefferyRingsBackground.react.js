import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyRingsBackground = React.lazy(() => import(/* webpackChunkName: "feffery_animated_3d_background_three" */ '../../fragments/animations/FefferyRingsBackground.react'));

/**
 * 3D-Rings背景组件FefferyRingsBackground
 */
const FefferyRingsBackground = ({
    mouseControls = true,
    touchControls = true,
    gyroControls = false,
    minHeight = 200.00,
    minWidth = 200.00,
    scale = 1.00,
    scaleMobile = 1.00,
    color = '#88ff00',
    backgroundColor = '#202428',
    backgroundAlpha = 1,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyRingsBackground {
                ...{
                    mouseControls,
                    touchControls,
                    gyroControls,
                    minHeight,
                    minWidth,
                    scale,
                    scaleMobile,
                    color,
                    backgroundColor,
                    backgroundAlpha,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyRingsBackground.propTypes = {
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
     * 设置移动端比例
     * 默认为`1.00`
     */
    scaleMobile: PropTypes.number,

    /**
     * 设置`rings`颜色
     * 默认为`'#88ff00'`
     */
    color: PropTypes.string,

    /**
     * 设置背景颜色
     * 默认为`'#202428'`
     */
    backgroundColor: PropTypes.string,

    /**
     * 设置背景颜色透明度，范围`0`到`1`
     * 默认为`1`
     */
    backgroundAlpha: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyRingsBackground;

export const propTypes = FefferyRingsBackground.propTypes;
export const defaultProps = FefferyRingsBackground.defaultProps;