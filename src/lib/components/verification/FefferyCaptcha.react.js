import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyCaptcha = React.lazy(() => import(/* webpackChunkName: "feffery_captcha" */ '../../fragments/verification/FefferyCaptcha.react'));

/**
 * 验证码组件FefferyCaptcha
 */
const FefferyCaptcha = ({
    charNum = 4,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyCaptcha {
                ...{
                    charNum,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyCaptcha.propTypes = {
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
     * 当前组件css类名，支持[动态css](/advanced-classname)
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 对应当前的验证码字符串
     */
    captcha: PropTypes.string,

    /**
     * 设置验证码字符数量
     */
    charNum: PropTypes.number,

    /**
     * 设置验证码的像素高度
     * 默认值：`40`
     */
    height: PropTypes.number,

    /**
     * 设置验证码的像素宽度
     * 默认值：`100`
     */
    width: PropTypes.number,

    /**
     * 设置验证码图片背景色
     * 默认值：`'#DFF0D8'`
     */
    bgColor: PropTypes.string,

    /**
     * 设置验证码字体像素大小
     * 默认值：`25`
     */
    fontSize: PropTypes.number,

    /**
     * 用于手动刷新验证码，当传入`true`时会强制刷新验证码，再自动重置为`false`
     */
    refresh: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyCaptcha;

export const propTypes = FefferyCaptcha.propTypes;
export const defaultProps = FefferyCaptcha.defaultProps;