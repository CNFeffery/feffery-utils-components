// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * 跨iframe通信组件FefferyIframeMessenger
 */
const FefferyIframeMessenger = ({
    role,
    mode,
    targetIframeId,
    toSendMessage,
    setProps
}) => {

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

FefferyIframeMessenger.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 必填，声明当前组件所在标签页角色，可选的有`'sender'`和`'receiver'`
     */
    role: PropTypes.oneOf(['sender', 'receiver']).isRequired,

    /**
     * 必填，声明当前组件对应传递信息的模式，可选的有`'to-parent'`和`'to-child'`
     */
    mode: PropTypes.oneOf(['to-parent', 'to-child']).isRequired,

    /**
     * 当`role='sender'`且`mode='to-child'`时，用于定义需要发送消息的目标iframe组件的`id`
     */
    targetIframeId: PropTypes.string,

    /**
     * 当`role='sender'`时，用于设置将要新发送的信息内容，每次成功发送后都会重置为空
     */
    toSendMessage: PropTypes.any,

    /**
     * 当`role='receiver'`时，用于监听最近一次收到的信息内容
     */
    recivedMessage: PropTypes.any,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyIframeMessenger;