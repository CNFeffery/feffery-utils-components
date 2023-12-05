import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyCircleColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyCircleColorPicker.react'));

const FefferyCircleColorPicker = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyCircleColorPicker {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyCircleColorPicker.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置组件整体宽度，默认为'252px'
    width: PropTypes.string,

    // 设置圆圈的像素尺寸，默认为28
    circleSize: PropTypes.number,

    // 设置圆圈之间的像素间隔大小，默认为14
    circleSpacing: PropTypes.number,

    // 对应当前选中的16进制色彩字符串
    color: PropTypes.string,

    // 设置可选的16进制色彩值数组，默认为["#f44336", "#e91e63", "#9c27b0", "#673ab7", "#3f51b5", "#2196f3", "#03a9f4", "#00bcd4", "#009688", "#4caf50", "#8bc34a", "#cddc39", "#ffeb3b", "#ffc107", "#ff9800", "#ff5722", "#795548", "#607d8b"]
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

// 设置默认参数
FefferyCircleColorPicker.defaultProps = {
    circleSpacing: 14,
    circleSize: 28,
    width: '252px',
    colors: ["#f44336", "#e91e63", "#9c27b0", "#673ab7", "#3f51b5", "#2196f3", "#03a9f4", "#00bcd4", "#009688", "#4caf50", "#8bc34a", "#cddc39", "#ffeb3b", "#ffc107", "#ff9800", "#ff5722", "#795548", "#607d8b"]
}

export default FefferyCircleColorPicker;

export const propTypes = FefferyCircleColorPicker.propTypes;
export const defaultProps = FefferyCircleColorPicker.defaultProps;