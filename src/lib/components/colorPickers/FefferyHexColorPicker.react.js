import PropTypes from 'prop-types';
import React, { Suspense } from 'react';

const LazyFefferyHexColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyHexColorPicker.react'));

/**
 * 16进制色彩选择器FefferyHexColorPicker
 */
const FefferyHexColorPicker = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyHexColorPicker {...props} />
        </Suspense>
    );
}

FefferyHexColorPicker.propTypes = {
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
     * 监听或设置当前选中色彩对应16进制颜色值
     * 默认值：`'#36a0f8'`
     */
    color: PropTypes.string,

    /**
     * 是否显示透明度选择控件
     * 默认值：`false`
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

FefferyHexColorPicker.defaultProps = {
    showAlpha: false,
    color: '#44cef6'
}

export default FefferyHexColorPicker;

export const propTypes = FefferyHexColorPicker.propTypes;
export const defaultProps = FefferyHexColorPicker.defaultProps;