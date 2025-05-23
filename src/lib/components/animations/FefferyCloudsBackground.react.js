import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyCloudsBackground = React.lazy(() => import(/* webpackChunkName: "feffery_animated_3d_background_three" */ '../../fragments/animations/FefferyCloudsBackground.react'));

/**
 * 3D-Clouds背景组件FefferyCloudsBackground
 */
const FefferyCloudsBackground = ({
    mouseControls = true,
    touchControls = true,
    gyroControls = false,
    minHeight = 200.00,
    minWidth = 200.00,
    backgroundColor = '#ffffff',
    skyColor = '#68b8d7',
    cloudColor = '#adc1de',
    cloudShadowColor = '#183550',
    sunColor = '#ff9919',
    sunGlareColor = '#ff6633',
    sunlightColor = '#ff9933',
    speed = 1,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyCloudsBackground {
                ...{
                    mouseControls,
                    touchControls,
                    gyroControls,
                    minHeight,
                    minWidth,
                    backgroundColor,
                    skyColor,
                    cloudColor,
                    cloudShadowColor,
                    sunColor,
                    sunGlareColor,
                    sunlightColor,
                    speed,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyCloudsBackground.propTypes = {
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
     * 默认为`'#ffffff'`
     */
    backgroundColor: PropTypes.string,

    /**
     * 设置天空颜色
     * 默认为`'#68b8d7'`
     */
    skyColor: PropTypes.string,

    /**
     * 设置云颜色
     * 默认为`'#adc1de'`
     */
    cloudColor: PropTypes.string,

    /**
     * 设置云阴影颜色
     * 默认为`'#183550'`
     */
    cloudShadowColor: PropTypes.string,

    /**
     * 设置太阳颜色
     * 默认为`'#ff9919'`
     */
    sunColor: PropTypes.string,

    /**
     * 设置太阳炫光颜色
     * 默认为`'#ff6633'`
     */
    sunGlareColor: PropTypes.string,

    /**
     * 设置太阳光线颜色
     * 默认为`'#ff9933'`
     */
    sunlightColor: PropTypes.string,

    /**
     * 设置动画速度，范围`0`到`3`
     * 默认为`1`
     */
    speed: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyCloudsBackground;

export const propTypes = FefferyCloudsBackground.propTypes;
export const defaultProps = FefferyCloudsBackground.defaultProps;