import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyCloudsBackground = React.lazy(() => import(/* webpackChunkName: "feffery_animated_3d_background_three" */ '../../fragments/animations/FefferyCloudsBackground.react'));

const FefferyCloudsBackground = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyCloudsBackground {...props} />
        </Suspense>
    );
}


// 定义参数或属性
FefferyCloudsBackground.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 设置内嵌元素内容
     */
    children: PropTypes.node,

    /**
     * css类名
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 自定义css字典
     */
    style: PropTypes.object,

    /**
     * 辅助刷新用唯一标识key值
     */
    key: PropTypes.string,

    /**
     * 设置是否开启鼠标控制，默认为true
     */
    mouseControls: PropTypes.bool,

    /**
     * 设置是否开启触摸控制，默认为true
     */
    touchControls: PropTypes.bool,

    /**
     * 设置是否开启陀螺仪控制，默认为false
     */
    gyroControls: PropTypes.bool,

    /**
     * 设置最小高度，默认为200.00
     */
    minHeight: PropTypes.number,

    /**
     * 设置最小宽度，默认为200.00
     */
    minWidth: PropTypes.number,

    /**
     * 设置背景颜色，默认为'#ffffff'
     */
    backgroundColor: PropTypes.string,

    /**
     * 设置天空颜色，默认为'#68b8d7'
     */
    skyColor: PropTypes.string,

    /**
     * 设置云颜色，默认为'#adc1de'
     */
    cloudColor: PropTypes.string,

    /**
     * 设置云阴影颜色，默认为'#183550'
     */
    cloudShadowColor: PropTypes.string,

    /**
     * 设置太阳颜色，默认为'#ff9919'
     */
    sunColor: PropTypes.string,

    /**
     * 设置太阳炫光颜色，默认为'#ff6633'
     */
    sunGlareColor: PropTypes.string,

    /**
     * 设置太阳光线颜色，默认为'#ff9933'
     */
    sunlightColor: PropTypes.string,

    /**
     * 设置动画速度，范围0到3，默认为1
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
FefferyCloudsBackground.defaultProps = {
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    backgroundColor: '#ffffff',
    skyColor: '#68b8d7',
    cloudColor: '#adc1de',
    cloudShadowColor: '#183550',
    sunColor: '#ff9919',
    sunGlareColor: '#ff6633',
    sunlightColor: '#ff9933',
    speed: 1
}

export default FefferyCloudsBackground;

export const propTypes = FefferyCloudsBackground.propTypes;
export const defaultProps = FefferyCloudsBackground.defaultProps;