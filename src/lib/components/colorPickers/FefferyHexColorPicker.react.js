import PropTypes from 'prop-types';
import React, { Suspense } from 'react';

const LazyFefferyHexColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyHexColorPicker.react'));

const FefferyHexColorPicker = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyHexColorPicker {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyHexColorPicker.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 对应当前选中的16进制色彩字符串，默认为'#36a0f8'
    color: PropTypes.string,

    // 设置是否显示透明度选择控件，默认为false
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
FefferyHexColorPicker.defaultProps = {
    showAlpha: false,
    color: '#44cef6'
}

export default FefferyHexColorPicker;

export const propTypes = FefferyHexColorPicker.propTypes;
export const defaultProps = FefferyHexColorPicker.defaultProps;