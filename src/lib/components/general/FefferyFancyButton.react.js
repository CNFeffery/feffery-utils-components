import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyFancyButton = React.lazy(() => import(/* webpackChunkName: "feffery_fancy_button" */ '../../fragments/general/FefferyFancyButton.react'));

/**
 * 美观按钮组件FefferyFancyButton
 */
const FefferyFancyButton = ({
    id,
    children,
    className,
    style,
    key,
    nClicks = 0,
    debounceWait = 0,
    type,
    disabled,
    href,
    target = '_blank',
    before,
    after,
    ripple,
    setProps,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyFancyButton {
                ...{
                    id,
                    children,
                    className,
                    style,
                    key,
                    nClicks,
                    debounceWait,
                    type,
                    disabled,
                    href,
                    target,
                    before,
                    after,
                    ripple,
                    setProps,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyFancyButton.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，内嵌元素
     */
    children: PropTypes.node,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 按钮累计点击次数，用于监听按钮点击行为
     * 默认值：`0`
     */
    nClicks: PropTypes.number,

    /**
     * 按钮点击事件监听防抖延时，单位：毫秒
     * 默认值：`0`
     */
    debounceWait: PropTypes.number,

    /**
     * 按钮类型，可选项有`'primary'`、`'secondary'`、`'danger'`
     * 默认值：`'primary'`
     */
    type: PropTypes.oneOf(['primary', 'secondary', 'danger']),

    /**
     * 是否禁用当前组件
     * 默认值：`false`
     */
    disabled: PropTypes.bool,

    /**
     * 按钮点击跳转链接地址
     */
    href: PropTypes.string,

    /**
     * 按钮点击跳转链接方式
     * 默认值：`'_blank'`
     */
    target: PropTypes.string,

    /**
     * 组件型，按钮前缀元素
     */
    before: PropTypes.node,

    /**
     * 组件型，按钮后缀元素
     */
    after: PropTypes.node,

    /**
     * 是否开启点击涟漪效果
     * 默认值：`false`
     */
    ripple: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyFancyButton;

export const propTypes = FefferyFancyButton.propTypes;
export const defaultProps = FefferyFancyButton.defaultProps;