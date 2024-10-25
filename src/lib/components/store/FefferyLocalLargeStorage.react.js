import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyLocalLargeStorage = React.lazy(() => import(/* webpackChunkName: "feffery_local_large_storage" */ '../../fragments/store/FefferyLocalLargeStorage.react'));

/**
 * 客户端大容量存储器FefferyLocalLargeStorage
 */
const FefferyLocalLargeStorage = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyLocalLargeStorage {...props} />
        </Suspense>
    );
}

FefferyLocalLargeStorage.propTypes = {
    /**
     * 用于定义当前存储器的唯一识别id
     */
    id: PropTypes.string.isRequired,

    /**
     * 定义当前存储器对应存储在浏览器本地的数据
     */
    data: PropTypes.any,

    /**
     * 设置初始化时是否从浏览器本地存储中尝试读取`id`对应的值并更新到`data`中
     * 默认值：`false`
     */
    initialSync: PropTypes.bool,

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
FefferyLocalLargeStorage.defaultProps = {
    initialSync: false
}

export default React.memo(FefferyLocalLargeStorage);

export const propTypes = FefferyLocalLargeStorage.propTypes;
export const defaultProps = FefferyLocalLargeStorage.defaultProps;