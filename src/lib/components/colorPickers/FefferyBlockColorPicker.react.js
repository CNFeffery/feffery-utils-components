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
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * css样式
     */
    style: PropTypes.object,

    /**
     * css类名
     */
    className: PropTypes.string,

    /**
     * 设置组件整体宽度
     * 默认：'170px'
     */
    width: PropTypes.string,

    /**
     * 设置或监听当前选中色彩对应16进制颜色值
     */
    color: PropTypes.string,

    /**
     * 设置可选色彩对应16进制颜色值数组
     * 默认：['#D9E3F0', '#F47373', '#697689', '#37D67A', '#2CCCE4', '#555555', '#dce775', '#ff8a65', '#ba68c8']
     */
    colors: PropTypes.arrayOf(PropTypes.string),

    /**
     * 设置顶部箭头方位，可选的有'hide'、'top'
     * 默认：'top'
     */
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