import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyGlobeBackground = React.lazy(() => import(/* webpackChunkName: "feffery_animated_3d_background_three" */ '../../fragments/animations/FefferyGlobeBackground.react'));

/**
 * 3D-Globe背景组件FefferyGlobeBackground
 */
const FefferyGlobeBackground = ({
    mouseControls = true,
    touchControls = true,
    gyroControls = false,
    minHeight = 200.00,
    minWidth = 200.00,
    scale = 1.00,
    scaleMobile = 1.00,
    backgroundColor = '#23153c',
    color = '#ff3f81',
    color2 = '#ffffff',
    size = 1,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyGlobeBackground {
                ...{
                    mouseControls,
                    touchControls,
                    gyroControls,
                    minHeight,
                    minWidth,
                    scale,
                    scaleMobile,
                    backgroundColor,
                    color,
                    color2,
                    size,
                    ...others
                }
            } />
        </Suspense>
    );
}


FefferyGlobeBackground.propTypes = {
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
     * 设置背景颜色
     * 默认为`'#23153c'`
     */
    backgroundColor: PropTypes.string,

    /**
     * 设置globe颜色
     * 默认为`'#ff3f81'`
     */
    color: PropTypes.string,

    /**
     * 设置globe颜色2
     * 默认为`'#ffffff'`
     */
    color2: PropTypes.string,

    /**
     * 设置globe大小，范围`0.5`到`2`
     * 默认为`1`
     */
    size: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyGlobeBackground;

export const propTypes = FefferyGlobeBackground.propTypes;
export const defaultProps = FefferyGlobeBackground.defaultProps;