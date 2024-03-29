import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyRgbColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyRgbColorPicker.react'));

const FefferyRgbColorPicker = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyRgbColorPicker {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyRgbColorPicker.propTypes = {
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
     * 对应当前选中的rgb[a]色彩值字符串
     * 默认：'rgb(68, 206, 246)'
     */
    color: PropTypes.string,

    /**
     * 设置是否显示透明度选择控件
     * 默认：false
     */
    showAlpha: PropTypes.bool,

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
FefferyRgbColorPicker.defaultProps = {
    showAlpha: false,
    color: 'rgb(68, 206, 246)'
}

export default FefferyRgbColorPicker;

export const propTypes = FefferyRgbColorPicker.propTypes;
export const defaultProps = FefferyRgbColorPicker.defaultProps;