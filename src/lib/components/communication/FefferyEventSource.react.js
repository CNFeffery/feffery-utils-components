// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useEventSource } from '@reactuses/core';

/**
 * EventSource通信组件FefferyEventSource
 */
const FefferyEventSource = ({
    url,
    events = [],
    immediate = true,
    autoReconnect = false,
    operation,
    setProps
}) => {

    const { status: _status, data: _data, event: _event, close, open, error: _error } = useEventSource(
        url,
        events,
        {
            immediate,
            autoReconnect,
        }
    );

    useEffect(() => {
        if (!autoReconnect && _status === 'DISCONNECTED' && _data) {
            close();
        }
        setProps({ status: _status })
    }, [_status])

    useEffect(() => {
        setProps({ data: _data })
    }, [_data])

    useEffect(() => {
        setProps({ event: _event })
    }, [_event])

    useEffect(() => {
        if (operation) {
            if (operation === 'close') {
                close();
            } else if (operation === 'open') {
                open();
            }
            // 重置operation
            setProps({ operation: null })
        }
    }, [operation])

    useEffect(() => {
        if (_error) {
            setProps({
                errorEvent: {
                    timestamp: Date.now()
                }
            })
        }
    }, [_error])

    return <></>;
}

FefferyEventSource.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 必填，目标服务地址
     */
    url: PropTypes.string.isRequired,

    /**
     * 目标事件名称列表
     */
    events: PropTypes.arrayOf(PropTypes.string),

    /**
     * 是否立即建立连接
     * 默认：`true`
     */
    immediate: PropTypes.bool,

    /**
     * 配置连接断开自动重连相关参数，设置为`false`时将不会自动重连
     * 默认：`false`
     */
    autoReconnect: PropTypes.oneOfType([
        PropTypes.shape({
            /**
             * 重试次数
             */
            retries: PropTypes.number,
            /**
             * 重试前的延时时长，单位：毫秒
             */
            delay: PropTypes.number
        }),
        PropTypes.bool
    ]),

    /**
     * 监听最新的连接状态
     */
    status: PropTypes.string,

    /**
     * 监听最新的返回数据
     */
    data: PropTypes.any,

    /**
     * 监听最新的事件名称
     */
    event: PropTypes.string,

    /**
     * 控制要立即执行的操作，可选项有`'open'`、`'close'`，每次新的操作执行完成后都会重置为空值
     */
    operation: PropTypes.oneOf(['open', 'close']),

    /**
     * 监听最新的异常错误事件
     */
    errorEvent: PropTypes.shape({
        /**
         * 错误事件时间戳
         */
        timestamp: PropTypes.number
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyEventSource;