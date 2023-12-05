import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyWheelColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyWheelColorPicker.react'));

const FefferyWheelColorPicker = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyWheelColorPicker {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyWheelColorPicker.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 对应当前选中的16进制色彩字符串
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

// 设置默认参数
FefferyWheelColorPicker.defaultProps = {
}

export default FefferyWheelColorPicker;

export const propTypes = FefferyWheelColorPicker.propTypes;
export const defaultProps = FefferyWheelColorPicker.defaultProps;