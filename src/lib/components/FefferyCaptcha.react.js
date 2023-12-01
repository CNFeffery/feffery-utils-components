import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyCaptcha = React.lazy(() => import(/* webpackChunkName: "feffery_captcha" */ '../fragments/FefferyCaptcha.react'));

const FefferyCaptcha = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyCaptcha {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyCaptcha.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 对应当前的验证码字符串
    captcha: PropTypes.string,

    // 设置验证码字符数量
    charNum: PropTypes.number,

    // 设置验证码的像素高度，默认为40
    height: PropTypes.number,

    // 设置验证码的像素宽度，默认为100
    width: PropTypes.number,

    // 设置验证码图片背景色，默认为'#DFF0D8'
    bgColor: PropTypes.string,

    // 设置验证码字体像素大小，默认为25
    fontSize: PropTypes.number,

    // 用于手动刷新验证码，当传入true时会强制刷新验证码，再自动重置为false
    refresh: PropTypes.bool,

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
    setProps: PropTypes.func
};

// 设置默认参数
FefferyCaptcha.defaultProps = {
    charNum: 4
}

export default FefferyCaptcha;

export const propTypes = FefferyCaptcha.propTypes;
export const defaultProps = FefferyCaptcha.defaultProps;