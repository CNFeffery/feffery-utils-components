import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyLocalLargeStorage = React.lazy(() => import(/* webpackChunkName: "feffery_local_large_storage" */ '../../fragments/store/FefferyLocalLargeStorage.react'));

/**
 * 客户端大容量存储器FefferyLocalLargeStorage
 */
const FefferyLocalLargeStorage = ({
    initialSync = false,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyLocalLargeStorage {
                ...{
                    initialSync,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyLocalLargeStorage.propTypes = {
    /**
     * 用于定义当前存储器的唯一识别id
     */
    id: PropTypes.string.isRequired,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 定义当前存储器对应存储在浏览器本地的数据
     */
    data: PropTypes.any,

    /**
     * 设置初始化时是否从浏览器本地存储中尝试读取`id`对应的值并更新到`data`中
     * 默认值：`false`
     */
    initialSync: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default React.memo(FefferyLocalLargeStorage);

export const propTypes = FefferyLocalLargeStorage.propTypes;
export const defaultProps = FefferyLocalLargeStorage.defaultProps;