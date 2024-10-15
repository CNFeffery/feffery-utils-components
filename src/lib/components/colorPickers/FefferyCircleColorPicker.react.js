import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyCircleColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyCircleColorPicker.react'));

/**
 * Circle风格色彩选择器
 */
const FefferyCircleColorPicker = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyCircleColorPicker {...props} />
        </Suspense>
    );
}

FefferyCircleColorPicker.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

    /**
     * 整体宽度
     * 默认值：`'252px'`
     */
    width: PropTypes.string,

    /**
     * 圆圈像素大小
     * 默认值：`28`
     */
    circleSize: PropTypes.number,

    /**
     * 圆圈之间的像素间隔大小
     * 默认值：`14`
     */
    circleSpacing: PropTypes.number,

    /**
     * 监听或设置当前选中色彩对应16进制颜色值
     */
    color: PropTypes.string,

    /**
     * 设置可选色彩对应16进制颜色值数组
     * 默认值：`["#f44336", "#e91e63", "#9c27b0", "#673ab7", "#3f51b5", "#2196f3", "#03a9f4", "#00bcd4", "#009688", "#4caf50", "#8bc34a", "#cddc39", "#ffeb3b", "#ffc107", "#ff9800", "#ff5722", "#795548", "#607d8b"]`
     */
    colors: PropTypes.arrayOf(PropTypes.string),

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
    })
};

FefferyCircleColorPicker.defaultProps = {
    circleSpacing: 14,
    circleSize: 28,
    width: '252px',
    colors: ["#f44336", "#e91e63", "#9c27b0", "#673ab7", "#3f51b5", "#2196f3", "#03a9f4", "#00bcd4", "#009688", "#4caf50", "#8bc34a", "#cddc39", "#ffeb3b", "#ffc107", "#ff9800", "#ff5722", "#795548", "#607d8b"]
}

export default FefferyCircleColorPicker;

export const propTypes = FefferyCircleColorPicker.propTypes;
export const defaultProps = FefferyCircleColorPicker.defaultProps;