import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyWavesBackground = React.lazy(() => import(/* webpackChunkName: "feffery_animated_3d_background_three" */ '../../fragments/animations/FefferyWavesBackground.react'));

/**
 * 3D-Waves背景组件FefferyWavesBackground
 */
const FefferyWavesBackground = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyWavesBackground {...props} />
        </Suspense>
    );
}


FefferyWavesBackground.propTypes = {
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
     * 设置wave颜色
     * 默认为`'#11619a'`
     */
    color: PropTypes.string,

    /**
     * 设置光泽度，范围`0`到`150`
     * 默认为`30`
     */
    shininess: PropTypes.number,

    /**
     * 设置wave高度，范围`0`到`40`
     * 默认为`15`
     */
    waveHeight: PropTypes.number,

    /**
     * 设置wave速度，范围`0`到`2`
     * 默认为`1`
     */
    waveSpeed: PropTypes.number,

    /**
     * 设置缩放大小，范围`0.7`到`1.8`
     * 默认为`1`
     */
    zoom: PropTypes.number,

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
FefferyWavesBackground.defaultProps = {
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    scale: 1.00,
    scaleMobile: 1.00,
    color: '#11619a',
    shininess: 30,
    waveHeight: 15,
    waveSpeed: 1,
    zoom: 1
}

export default FefferyWavesBackground;

export const propTypes = FefferyWavesBackground.propTypes;
export const defaultProps = FefferyWavesBackground.defaultProps;