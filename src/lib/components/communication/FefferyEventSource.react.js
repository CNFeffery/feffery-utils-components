import { useEffect } from 'react';
import { useEventSource } from '@reactuses/core';
import PropTypes from 'prop-types';

/**
 * EventSource通信组件FefferyEventSource
 */
const FefferyEventSource = (props) => {
    const {
        url,
        events,
        immediate,
        autoReconnect,
        operation,
        setProps,
        loading_state
    } = props;

    const { status: _status, data: _data, event: _event, close, open } = useEventSource(
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

    return <></>;
}

FefferyEventSource.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 强制刷新用唯一标识key值
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
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

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
    })
};

// 设置默认参数
FefferyEventSource.defaultProps = {
    immediate: true,
    autoReconnect: false,
    events: []
}

export default FefferyEventSource;