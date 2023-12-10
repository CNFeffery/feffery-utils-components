import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyAutoFit = React.lazy(() => import(/* webpackChunkName: "feffery_auto_fit" */ '../../fragments/resizable/FefferyAutoFit.react'));

const FefferyAutoFit = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyAutoFit {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyAutoFit.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 要进行自适应的目标元素id，默认为'body'
     */
    containerId: PropTypes.string,

    /**
         * 设计稿的宽度，默认是1920
         */
    dw: PropTypes.number,
    /**
     * 设计稿的高度，默认是1080
     */
    dh: PropTypes.number,
    /**
     * 是否监听resize事件，默认是true
     */
    resize: PropTypes.bool,
    /**
     * 忽略缩放的元素列表（列表内的元素将反向缩放）
     */
    ignore: PropTypes.arrayOf(PropTypes.shape({
        /**
         * 要忽略缩放的元素的选择器名
         */
        el: PropTypes.string
    })),
    /**
     * 过渡时间，默认是0
     */
    transition: PropTypes.number,
    /**
     * 延迟时间，默认是0
     */
    delay: PropTypes.number,
    /**
     * 默认是 0.1,当缩放阈值不大于此值时不缩放，比如设置为0.1时，0.9-1.1的范围会被重置为1
     */
    limit: PropTypes.number,

    /**
     * 关闭自适应，设置为true执行完相应操作后会自动重置为false，默认为false
     */
    close: PropTypes.bool,

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
FefferyAutoFit.defaultProps = {
    containerId: 'body',
    dw: 1920,
    dh: 1080,
    resize: true,
    ignore: [],
    transition: 0,
    delay: 0,
    limit: 0.1,
    close: false
}

export default FefferyAutoFit;

export const propTypes = FefferyAutoFit.propTypes;
export const defaultProps = FefferyAutoFit.defaultProps;