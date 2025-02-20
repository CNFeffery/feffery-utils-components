import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyHttpRequests = React.lazy(() => import(/* webpackChunkName: "feffery_http_requests" */ '../../fragments/communication/FefferyHttpRequests.react'));

/**
 * http请求组件FefferyHttpRequests
 */
const FefferyHttpRequests = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyHttpRequests {...props} />
        </Suspense>
    );
}

FefferyHttpRequests.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 构造新发起http请求对应的参数，每次更新为有效值后会发起相应的请求，每次请求完成（成功或失败）后会自动重置为空值
     */
    requestConfig: PropTypes.shape({
        /**
         * 请求类型，可选项有`'get'`、`'post'`、`'put'`、`'patch'`、`'delete'`
         * 默认值：`'get'`
         */
        method: PropTypes.oneOf(['get', 'post', 'put', 'patch', 'delete']),
        /**
         * 必填，请求目标url
         */
        url: PropTypes.string.isRequired,
        /**
         * 自定义请求头
         */
        headers: PropTypes.object,
        /**
         * 自定义请求参数
         */
        params: PropTypes.object,
        /**
         * 自定义请求体发送数据
         */
        data: PropTypes.object,
        /**
         * 请求超时时长，单位：毫秒，设置为`0`表示永不超时
         * 默认值：`0`
         */
        timeout: PropTypes.number,
        /**
         * 跨域请求时是否需要使用凭证
         * 默认值：`false`
         */
        withCredentials: PropTypes.bool,
        /**
         * 响应结果数据类型，可选项有`'json'`、`'text'`、`'document'`、`'stream'`、`'arraybuffer'`、`'blob'`
         * 默认值：`'json'`
         */
        responseType: PropTypes.oneOf(['json', 'text', 'document', 'stream', 'arraybuffer', 'blob'])
    }),

    /**
     * 监听最近一次请求任务执行结果相关信息
     */
    responseResult: PropTypes.shape({
        /**
         * 请求结果状态
         */
        status: PropTypes.number,
        /**
         * 请求结果状态描述
         */
        statusText: PropTypes.string,
        /**
         * 请求结果数据
         */
        data: PropTypes.any,
        /**
         * 请求地址
         */
        requestURL: PropTypes.string,
        /**
         * 请求任务完成时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 请求错误代码，仅任务失败时附带
         */
        errorCode: PropTypes.string,
        /**
         * 请求错误描述，仅任务失败时附带
         */
        message: PropTypes.string
    }),

    /**
     * 监听当前组件的状态，`'pending'`表示请求中，`'idle'`表示空闲状态
     */
    status: PropTypes.oneOf(['pending', 'idle']),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyHttpRequests;

export const propTypes = FefferyHttpRequests.propTypes;
export const defaultProps = FefferyHttpRequests.defaultProps;