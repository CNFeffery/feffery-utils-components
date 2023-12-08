import { useEffect } from 'react';
import { useWebSocket } from 'ahooks';
import PropTypes from 'prop-types';

const num2state = new Map([
    [0, 'connecting'],
    [1, 'open'],
    [2, 'closing'],
    [3, 'closed']
])

// 定义WebSocket通信组件FefferyWebSocket
const FefferyWebSocket = (props) => {

    const {
        id,
        socketUrl,
        reconnectLimit,
        reconnectInterval,
        operation,
        message,
        setProps,
        loading_state
    } = props;

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

// 定义参数或属性
FefferyWebSocket.propTypes = {
    // 组件id
    id: PropTypes.string,

    // 设置要建立连接的WebSocket服务url
    socketUrl: PropTypes.string.isRequired,

    // 设置连接重试次数，默认为3
    reconnectLimit: PropTypes.number,

    // 设置连接重试间隔，默认为3000，单位：毫秒
    reconnectInterval: PropTypes.number,

    // 用于执行连接/断开连接/发送信息操作，可选项有'connect'、'disconnect'、'send'
    // 每次新操作执行后，operation参数都会被重置为null
    operation: PropTypes.oneOf(['connect', 'disconnect', 'send']),

    // 当operation更新为'send'时，用于设置要通过WebSocket服务向服务器发送的数据
    message: PropTypes.string,

    // 监听从服务器传来的最新信息
    latestMessage: PropTypes.string,

    // 用于监听当前此连接的状态，有'connecting'、'open'、'closing'、'closed'四种状态
    state: PropTypes.oneOf(['connecting', 'open', 'closing', 'closed']),

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
FefferyWebSocket.defaultProps = {
}

export default FefferyWebSocket;