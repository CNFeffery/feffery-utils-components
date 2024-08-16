import React, { useEffect } from 'react';
import PropTypes from 'prop-types';

// 定义跨iframe通信器FefferyIframeMessenger
const FefferyIframeMessenger = (props) => {
    // 取得必要属性或参数
    const {
        role,
        mode,
        targetIframeId,
        toSendMessage,
        setProps,
        loading_state
    } = props;

    // 处理不同模式下的收信行为
    useEffect(() => {
        // 若当前组件角色为收信者
        if (role === 'receiver') {
            // 事件监听函数
            if (mode === 'to-child') {
                const listenMessage = (e) => {
                    // 针对来自父级页面的消息
                    if (e.source === window.parent) {
                        setProps({
                            recivedMessage: e.data
                        })
                    }
                };
                // 绑定message事件
                window.addEventListener('message', listenMessage);
                // 组件卸载时销毁相关事件监听
                return () => {
                    window.removeEventListener('message', listenMessage);
                }
            } else if (mode === 'to-parent') {
                const listenMessage = (e) => {
                    // 针对来自子级目标iframe的消息
                    if (e.source === document.querySelector('#' + targetIframeId)?.contentWindow) {
                        setProps({
                            recivedMessage: e.data
                        })
                    }
                };
                // 绑定message事件
                window.addEventListener('message', listenMessage);
                // 组件卸载时销毁相关事件监听
                return () => {
                    window.removeEventListener('message', listenMessage);
                }
            }
        }
    }, [])

    // 处理不同模式下的发信行为
    useEffect(() => {
        if (role === 'sender' && toSendMessage) {
            if (mode === 'to-child' && targetIframeId) {
                // 发送消息
                let targetFrame = document.querySelector('#' + targetIframeId)
                targetFrame.contentWindow.postMessage(toSendMessage, targetFrame.src);
            } else if (mode === 'to-parent') {
                // 发送消息
                window.parent.postMessage(toSendMessage, '*');
            }
            // 重置toSendMessage
            setProps({
                toSendMessage: null
            })
        }
    }, [toSendMessage])

    return <></>;
}


// 定义参数或属性
FefferyIframeMessenger.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 强制刷新组件状态用
     */
    key: PropTypes.string,

    /**
     * 必填，声明当前组件所在标签页角色，可选的有'sender'和'receiver'
     */
    role: PropTypes.oneOf(['sender', 'receiver']).isRequired,

    /**
     * 必填，声明当前组件对应传递信息的模式，可选的有'to-parent'和'to-child'
     */
    mode: PropTypes.oneOf(['to-parent', 'to-child']).isRequired,

    /**
     * 当role为'sender'且mode为'to-child'时，用于定义需要发送消息的目标iframe组件的id
     */
    targetIframeId: PropTypes.string,

    /**
     * 当role为'sender'时，用于设置将要新发送的信息内容，每次成功发送后都会重置为空
     */
    toSendMessage: PropTypes.any,

    /**
     * 当role为'receiver'时，用于监听最近一次收到的信息内容
     */
    recivedMessage: PropTypes.any,

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
FefferyIframeMessenger.defaultProps = {
}

export default FefferyIframeMessenger;