import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyCloudsTwoBackground = React.lazy(() => import(/* webpackChunkName: "feffery_animated_3d_background_three" */ '../../fragments/animations/FefferyCloudsTwoBackground.react'));

/**
 * 3D-CloudsTwo背景组件FefferyCloudsTwoBackground
 */
const FefferyCloudsTwoBackground = ({
    mouseControls = true,
    touchControls = true,
    gyroControls = false,
    minHeight = 200.00,
    minWidth = 200.00,
    scale = 1.00,
    backgroundColor = '#000000',
    skyColor = '#5ca6ca',
    cloudColor = '#334d80',
    lightColor = '#ffffff',
    speed = 1,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyCloudsTwoBackground {
                ...{
                    mouseControls,
                    touchControls,
                    gyroControls,
                    minHeight,
                    minWidth,
                    scale,
                    backgroundColor,
                    skyColor,
                    cloudColor,
                    lightColor,
                    speed,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyCloudsTwoBackground.propTypes = {
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
     * 设置纹理图片的`url`，支持`base64`编码的字符串
     */
    texturePath: PropTypes.string,

    /**
     * 设置背景颜色
     * 默认为`'#000000'`
     */
    backgroundColor: PropTypes.string,

    /**
     * 设置天空颜色
     * 默认为`'#5ca6ca'`
     */
    skyColor: PropTypes.string,

    /**
     * 设置云颜色
     * 默认为`'#334d80'`
     */
    cloudColor: PropTypes.string,

    /**
     * 设置光线颜色
     * 默认为`'#ffffff'`
     */
    lightColor: PropTypes.string,

    /**
     * 设置动画速度，范围`0`到`5`
     * 默认为`1`
     */
    speed: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyCloudsTwoBackground;

export const propTypes = FefferyCloudsTwoBackground.propTypes;
export const defaultProps = FefferyCloudsTwoBackground.defaultProps;