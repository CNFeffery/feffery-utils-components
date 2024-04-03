import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferySliderCaptcha = React.lazy(() => import(/* webpackChunkName: "feffery_slider_captcha" */ '../fragments/FefferySliderCaptcha.react'));

const FefferySliderCaptcha = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferySliderCaptcha {...props} />
        </Suspense>
    );
}

FefferySliderCaptcha.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * css类名
     */
    className: PropTypes.string,

    /**
     * css样式
     */
    style: PropTypes.object,

    /**
     * 用于生成拼图的完整图片地址
     */
    imgSrc: PropTypes.string,

    /**
     * 声明用于生成拼图的完整图片像素宽度值
     */
    imgWidth: PropTypes.number,

    /**
     * 拼图合法验证像素偏移量
     * 默认值：`5`
     */
    xOffset: PropTypes.number,

    /**
     * 显示模式，可选项有`'embed'`、`'float'`、`'slider'`
     * 默认值：`'embed'`
     */
    mode: PropTypes.oneOf(['embed', 'float', 'slider']),

    /**
     * 配置相关文案提示内容
     */
    tipText: PropTypes.exact({
        /**
         * 默认提示内容
         */
        default: PropTypes.node,
        /**
         * 加载中提示内容
         */
        loading: PropTypes.node,
        /**
         * 移动中提示内容
         */
        moving: PropTypes.node,
        /**
         * 验证中提示内容
         */
        verifying: PropTypes.node,
        /**
         * 验证成功提示内容
         */
        success: PropTypes.node,
        /**
         * 验证失败提示内容
         */
        error: PropTypes.node
    }),

    /**
     * 显示右上角刷新按钮
     * 默认值：`true`
     */
    showRefreshIcon: PropTypes.bool,

    /**
     * 验证失败后是否自动刷新
     * 默认值：`true`
     */
    autoRefreshOnError: PropTypes.bool,

    /**
     * 当`autoRefreshOnError=True`时，每次验证失败后停顿多少毫秒自动刷新
     * 默认值：`500`
     */
    errorHoldDuration: PropTypes.number,

    /**
     * 拼图图片显示方位，可选项有`'top'`、`'bottom'`
     * 默认值：`'top'`
     */
    placement: PropTypes.oneOf(['top', 'bottom']),

    /**
     * 手动刷新用，每次更新为`True`时会主动触发刷新，每次成功刷新后会重置为`False`
     */
    refresh: PropTypes.bool,

    /**
     * 监听最近一次验证结果
     */
    verifyResult: PropTypes.exact({
        /**
         * 验证状态，`'success'`表示验证成功，`'error'`表示验证失败
         */
        status: PropTypes.oneOf(['success', 'error']),
        /**
         * 事件发生时间戳
         */
        timestamp: PropTypes.number
    }),

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
FefferySliderCaptcha.defaultProps = {
    xOffset: 5,
    mode: 'embed',
    showRefreshIcon: true,
    autoRefreshOnError: true,
    errorHoldDuration: 500,
    placement: 'top'
}

export default FefferySliderCaptcha;

export const propTypes = FefferySliderCaptcha.propTypes;
export const defaultProps = FefferySliderCaptcha.defaultProps;