// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useWebSocket } from 'ahooks';

const num2state = new Map([
    [0, 'connecting'],
    [1, 'open'],
    [2, 'closing'],
    [3, 'closed']
])

/**
 * WebSocket通信组件FefferyWebSocket
 */
const FefferyWebSocket = ({
    socketUrl,
    reconnectLimit,
    reconnectInterval,
    operation,
    message,
    setProps
}) => {

    const { readyState: _readyState, sendMessage, latestMessage: _latestMessage, disconnect, connect } = useWebSocket(
        socketUrl,
        {
            reconnectLimit,
            reconnectInterval
        }
    );

    // 监听服务器发送来的最新信息
    useEffect(() => {
        if (_latestMessage) {
            setProps({
                latestMessage: _latestMessage.data
            })
        }
    }, [_latestMessage])

    // 监听当前WebSocket连接的状态
    useEffect(() => {
        setProps({
            state: num2state.get(_readyState)
        })
    }, [_readyState])

    // 监听operation，从而执行不同操作
    useEffect(() => {
        if (operation) {
            // 断开连接操作
            if (operation === 'connect') {
                connect()
            } else if (operation === 'disconnect') {
                disconnect()
            } else if (operation === 'send') {
                sendMessage(message)
            }
            // 重置operation
            setProps({
                operation: null
            })
        }
    }, [operation])

    return <></>;
}

FefferyWebSocket.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置要建立连接的WebSocket服务`url`
     */
    socketUrl: PropTypes.string.isRequired,

    /**
     * 设置连接重试次数
     * 默认为`3`
     */
    reconnectLimit: PropTypes.number,

    /**
     * 设置连接重试间隔，单位：毫秒
     * 默认为`3000`
     */
    reconnectInterval: PropTypes.number,

    /**
     * 用于执行连接/断开连接/发送信息操作，可选项有`'connect'`、`'disconnect'`、`'send'`，每次新操作执行后，operation参数都会被重置为null
     */
    operation: PropTypes.oneOf(['connect', 'disconnect', 'send']),

    /**
     * 当operation更新为`'send'`时，用于设置要通过WebSocket服务向服务器发送的数据
     */
    message: PropTypes.string,

    /**
     * 监听从服务器传来的最新信息
     */
    latestMessage: PropTypes.string,

    /**
     * 用于监听当前此连接的状态，有`'connecting'`、`'open'`、`'closing'`、`'closed'`四种状态
     */
    state: PropTypes.oneOf(['connecting', 'open', 'closing', 'closed']),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyWebSocket;