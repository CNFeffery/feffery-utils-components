import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyBlockColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyBlockColorPicker.react'));

const FefferyBlockColorPicker = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyBlockColorPicker {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyBlockColorPicker.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置组件整体宽度，默认为'170px'
    width: PropTypes.string,

    // 对应当前选中的16进制色彩字符串
    color: PropTypes.string,

    // 设置可选的16进制色彩值数组，默认为['#D9E3F0', '#F47373', '#697689', '#37D67A', '#2CCCE4', '#555555', '#dce775', '#ff8a65', '#ba68c8']
    colors: PropTypes.arrayOf(PropTypes.string),

    // 设置顶部箭头的方位，可选的有'hide'、'top'，默认为'top'
    triangle: PropTypes.oneOf(['hide', 'top']),

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
FefferyBlockColorPicker.defaultProps = {
    triangle: 'top',
    width: '170px',
    colors: ['#D9E3F0', '#F47373', '#697689', '#37D67A', '#2CCCE4', '#555555', '#dce775', '#ff8a65', '#ba68c8']
}

export default FefferyBlockColorPicker;

export const propTypes = FefferyBlockColorPicker.propTypes;
export const defaultProps = FefferyBlockColorPicker.defaultProps;