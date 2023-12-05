import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyEyeDropper = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyEyeDropper.react'));

const FefferyEyeDropper = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyEyeDropper {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyEyeDropper.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 设置是否启用色彩拾取模式，默认为false
    enable: PropTypes.bool,

    // 用于监听最近一次取色完成后得到的16进制色彩值
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
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

// 设置默认参数
FefferyEyeDropper.defaultProps = {
    enable: false
}

export default FefferyEyeDropper;

export const propTypes = FefferyEyeDropper.propTypes;
export const defaultProps = FefferyEyeDropper.defaultProps;