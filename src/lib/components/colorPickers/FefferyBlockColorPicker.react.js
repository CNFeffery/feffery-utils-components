import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyBlockColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyBlockColorPicker.react'));

/**
 * Block风格色彩选择器
 */
const FefferyBlockColorPicker = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyBlockColorPicker {...props} />
        </Suspense>
    );
}

FefferyBlockColorPicker.propTypes = {
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
     * 默认值：`'170px'`
     */
    width: PropTypes.string,

    /**
     * 监听或设置当前选中色彩对应16进制颜色值
     */
    color: PropTypes.string,

    /**
     * 设置可选色彩对应16进制颜色值数组
     * 默认值：`['#D9E3F0', '#F47373', '#697689', '#37D67A', '#2CCCE4', '#555555', '#dce775', '#ff8a65', '#ba68c8']`
     */
    colors: PropTypes.arrayOf(PropTypes.string),

    /**
     * 顶部箭头方位，可选项有`'hide'`、`'top'`
     * 默认值：`'top'`
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

FefferyBlockColorPicker.defaultProps = {
    triangle: 'top',
    width: '170px',
    colors: ['#D9E3F0', '#F47373', '#697689', '#37D67A', '#2CCCE4', '#555555', '#dce775', '#ff8a65', '#ba68c8']
}

export default FefferyBlockColorPicker;

export const propTypes = FefferyBlockColorPicker.propTypes;
export const defaultProps = FefferyBlockColorPicker.defaultProps;