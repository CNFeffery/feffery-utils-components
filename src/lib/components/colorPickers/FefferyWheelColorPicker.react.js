import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyWheelColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyWheelColorPicker.react'));

/**
 * Wheel风格色彩选择器FefferyWheelColorPicker
 */
const FefferyWheelColorPicker = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyWheelColorPicker {...props} />
        </Suspense>
    );
}

FefferyWheelColorPicker.propTypes = {
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
     */
    color: PropTypes.string,

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

FefferyWheelColorPicker.defaultProps = {
}

export default FefferyWheelColorPicker;

export const propTypes = FefferyWheelColorPicker.propTypes;
export const defaultProps = FefferyWheelColorPicker.defaultProps;